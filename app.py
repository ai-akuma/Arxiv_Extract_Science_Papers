from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import generate_multiple_reports as reporter
import os
import glob

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    input_files = glob.glob("input/*")
    for f in input_files:
        os.remove(f)
    output_files = glob.glob("output/*")
    for f in output_files:
        os.remove(f)

    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(f"input/{filename}")
    return redirect("/display/" + filename, code=302)


@app.route("/display/<filename>")
def display_result(filename):
    # Insert your processing code here
    # You can read the PDF, process it, and generate the resultant HTML

    # Assuming 'result' is the HTML string generated after processing the PDF
    return reporter.main(filename)


if __name__ == "__main__":
    app.run(debug=True)
