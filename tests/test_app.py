from flask import url_for
from flaskcloudinary.app import create_app


def test_status_code(client):
    assert client.get(url_for('upload_file')).status_code == 200

def test_upload_file_page(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Upload new Image" in response.data
    assert b"input type" in response.data
    assert b"submit" in response.data