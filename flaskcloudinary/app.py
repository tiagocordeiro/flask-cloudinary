import os

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from flask import Flask, render_template, request

def create_app():
    application = Flask(__name__)

    @application.route('/', methods=['GET', 'POST'])
    def upload_file():
        upload_result = None
        thumbnail_url1 = None
        thumbnail_url2 = None
        thumbnail_pixelate = None
        if request.method == 'POST':
            file_to_upload = request.files['file']
            if file_to_upload:
                upload_result = upload(file_to_upload)
                thumbnail_url1, options = cloudinary_url(
                    upload_result['public_id'],
                    format="jpg",
                    crop="fill",
                    width=100,
                    height=100)
                thumbnail_url2, options = cloudinary_url(
                    upload_result['public_id'],
                    format="jpg",
                    crop="fill",
                    width=200,
                    height=100,
                    radius=20,
                    effect="sepia")
                thumbnail_pixelate, options = cloudinary_url(
                    upload_result['public_id'],
                    format="jpg",
                    crop="fill",
                    width=200,
                    height=300,
                    radius=20,
                    effect="pixelate_faces:9",
                    gravity="face")
        return render_template('upload_form.html', upload_result=upload_result,
                            thumbnail_url1=thumbnail_url1,
                            thumbnail_url2=thumbnail_url2,
                            thumbnail_pixelate=thumbnail_pixelate)

    return application
