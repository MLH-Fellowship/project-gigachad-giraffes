import os
# test_app.py

import unittest
import os

os.environ['TESTING'] = 'true'

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert '<html lang="en">' in html
        assert '<meta charset="utf-8">' in html
        assert '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' in html

    def test_timeline(self):
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    def test_timeline_page(self):
        response = self.client.get("http://127.0.0.1:5000/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<label for="name">Name:</label>' in html
        assert '<input type="text" name="name" id="name" placeholder="Name" required />' in html
        assert '<label for="email">Email:</label>' in html
        assert '<input type="text" name="email" id="email" placeholder="Email" required />' in html
        assert '<label for="content">Message:</label>' in html

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post",
                                    data={"name": "", "email": "john@example.com",
                                          "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post",
                                    data={"name": "John Doe", "email": "john@example.com",
                                          "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post",
                                    data={"name": "John Doe", "email": "not-an-email",
                                          "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

    def post_sucess(self):
        response = self.client.post("/api/timeline_post",
                                    data={"name": "test", "email": "john@example.com",
                                          "content": "Hello world, I'm John!"})
        assert response.status_code == 200
        assert response.is_json
