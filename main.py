# In command prompt:
# 1. run python main.py
# 2. It will show a http link, run it


from flask import Flask, flash, request, redirect, url_for, render_template	
from werkzeug.utils import secure_filename
from photo_restorer import predict_image
import os

UPLOAD_FOLDER = 'static/images'  # Folder relative to your project root
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.secret_key = 'supersecretkey'  # For flash messages (optional)


@app.route("/")
def home():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Full path to save the file
            file.save(file_path)  # Save the file

            # Call the predict_image function with the full path
            predicted_img_url = predict_image(file_path)

            # Return the rendered template with the original image and the restored image URL
            return render_template("index.html", filename=filename, restored_img_url=predicted_img_url)

    flash("File type not allowed")  # This message will be shown if file extension is not allowed
    return redirect(request.url)


if __name__ == "__main__":
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
