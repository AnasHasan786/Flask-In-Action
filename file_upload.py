from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Define the folder where uploaded files will be saved
app.config["UPLOAD_FOLDER"] = "uploads"  # The folder to store uploaded files
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # Limit the file size to 16MB

# Allowed file extensions for security
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf"}


# Function to check if the file type is allowed
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Route to display the upload form
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Get the file from the form
        file = request.files["file"]

        # Check if the file is selected
        if file and allowed_file(file.filename):
            # Secure the filename to prevent unsafe characters
            filename = secure_filename(file.filename)

            # Save the file to the specified folder
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            # Redirect to show the uploaded file
            return redirect(url_for("uploaded_file", filename=filename))

    # Render the file upload form
    return render_template("upload_form.html")


# Route to display the uploaded file
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    # Serve the uploaded file from the 'uploads' directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
