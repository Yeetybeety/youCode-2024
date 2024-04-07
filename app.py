from flask import Flask, request, jsonify
import openai
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
openai.api_key = os.getenv("")

# Ensure there is a folder to save uploaded images temporarily
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-form')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Now that we have the image saved, we can send it to the CLIP model
        response = openai.CLIP.search(
            images=[open(file_path, 'rb')],
            queries=["A description of the image"]
        )
        
        # Remove the image after processing
        os.remove(file_path)
        
        # Return the model's response
        description = response['data'][0]['text']
        return jsonify(description=description)

    return jsonify(error="Invalid file"), 400

if __name__ == '__main__':
    app.run(debug=True)