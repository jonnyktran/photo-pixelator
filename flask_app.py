
from main import pixelator
from flask import Flask, request, render_template
from markupsafe import Markup
import os
import base64
import io

UPLOAD_FOLDER = 'mysite/static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def image_input():
    # Image, integer pixel > 0
    if request.method == "POST" and request.form['pixel_size'].isnumeric() and request.form['pixel_size'] != "0" \
            and not request.files['img'].filename == "":
        image = request.files['img']
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(img_path)

        final_img = pixelator(img_path, request.form['pixel_size'])
        os.remove(img_path)

        data = io.BytesIO()
        final_img.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        return render_template("display.html", img_data=encoded_img_data.decode('utf-8'))

    # Image, non-integer pixel or 0
    elif request.method == "POST" and (request.form['pixel_size'] == '0' or not request.form['pixel_size'].isnumeric()) \
            and not request.files['img'].filename == "":
        return render_template("homepage.html", image_error=Markup('<span id="error"> Please upload the image again! </span> <span class="brsmall"></span>'),
            pixel_error=Markup('<span id="error"> Please enter a positive integer! </span><span class="brsmall"></span>'))

    # No image, non-zero integer pixel
    elif request.method == "POST" and (request.form['pixel_size'] != '0' and request.form['pixel_size'].isnumeric()) \
            and request.files['img'].filename == "":
        return render_template("homepage.html", image_error=Markup('<span id="error"> Please select an image! </span> <span class="brsmall"></span>'),
            pixel_error=Markup('<span id="error"> Please re-enter the pixel size! </span><span class="brsmall"></span>'))

    # No image, no pixel
    elif request.method == "POST":
        return render_template("homepage.html", image_error=Markup('<span id="error"> Please select an image! </span> <span class="brsmall"></span>'),
            pixel_error=Markup('<span id="error"> Please enter a positive integer! </span><span class="brsmall"></span>'))

    return render_template("homepage.html")
