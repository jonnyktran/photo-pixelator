
# A very simple Flask Hello World app for you to get started with...
from main_flask import pixelator
from flask import Flask, request
import os

UPLOAD_FOLDER = '/home/wlnguyen/mysite/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])

def image_input():
    if request.method == "POST":
        image = request.files['img']
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(img_path)

        final_img = pixelator(img_path, request.form['pixel_size'])
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], "pixelated_" + image.filename)
        final_img.save(img_path)

    return '''
        <html>
            <body>
                <form method="post" action="." enctype="multipart/form-data">
                    <p>Provide an image: <br>
                    <input type="file" id='img' name='img'
                    accept="image/png, image/jpeg, image/jpg"> </p>
                    <p>Enter pixel size: <br> <input name="pixel_size" /></p>
                    <p><input type="submit" value="Pixelate image" /></p>
                </form>
            </body>
        </html>
    '''
