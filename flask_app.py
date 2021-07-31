
# A very simple Flask Hello World app for you to get started with...
from main_flask import pixelator
from flask import Flask, request, render_template
import os
import base64
import io

UPLOAD_FOLDER = '/home/wlnguyen/mysite/static/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def image_input():
    if request.method == "POST":
        image = request.files['img']
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(img_path)

        final_img = pixelator(img_path, request.form['pixel_size'])
        os.remove(img_path)

        data = io.BytesIO()
        final_img.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        return render_template("display.html", img_data=encoded_img_data.decode('utf-8'))

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
