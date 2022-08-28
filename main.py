from flask import Flask, flash, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os
from color_extractor import Extractor


app = Flask(__name__)
Bootstrap(app)
WTF_CSRF_SECRET_KEY = 'a random string'
app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY


class ImageForm(FlaskForm):
    image = FileField(validators=[FileRequired()])


@app.route("/", methods=['POST', 'GET'])
def home():
    form = ImageForm()
    colors = None
    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'image', filename
        ))
        image_path = f'instance/image/{filename}'
        extractor = Extractor(image_path)
        colors = extractor.top10_colors_hex
        return render_template('index.html', form=form, colors=colors)
    return render_template('index.html', form=form, colors=colors)


@app.route("/show-colors")
def show_colors():
    pass


if __name__ == "__main__":
    app.run(debug=True)