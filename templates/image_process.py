from flask import Flask, request, render_template
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('image_test.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    # Read uploaded image
    image = Image.open(request.files['image'])

    # Perform OCR (Optical Character Recognition)
    text = pytesseract.image_to_string(image)

    return text

if __name__ == '__main__':
    app.run(debug=True)