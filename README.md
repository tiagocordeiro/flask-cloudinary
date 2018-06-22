Cloudinary Flask sample project
===============================

A simple Flask application that performs image upload and generates on the transformations of the uploaded image.

## Installing and running
```
$ git clone https://github.com/tiagocordeiro/flask-cloudinary.git
$ cd flask-cloudinary
$ python3 -m venv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```
* Get [a cloudinary account](https://cloudinary.com/users/register/free)
* Copy the `CLOUDINARY_URL` environment variable from the [Management Console](https://cloudinary.com/console):
```
(venv)$ export CLOUDINARY_URL=cloudinary://API-Key:API-Secret@Cloud-name
(venv)$ flask run
```
* Browse to http://127.0.0.1:5000/

# TODO
[ ] Melhorar documentação

Good luck!