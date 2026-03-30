import os
import random
import string
from locust import HttpUser, task, between

class PhotoAlbumFullTest(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        self.username = f"user_{suffix}"
        self.password = "TestPassword123!"

    
        reg_page = self.client.get("/users/register/")
        csrftoken = reg_page.cookies.get('csrftoken', '')

    
        self.client.post("/users/register", {
            "username": self.username,
            "password": self.password,
            "password_confirm": self.password,
            "csrfmiddlewaretoken": csrftoken
        }, headers={"Referer": self.host + "/users/register/"})

    
        self.client.post("/users/login", {
            "username": self.username,
            "password": self.password,
            "csrfmiddlewaretoken": csrftoken
        }, headers={"Referer": self.host + "/users/login/"})

    @task(5)
    def view_gallery(self):
        self.client.get("/")


    @task(1)
    def simulate_sort(self):
        self.client.get("/?sort=title") 

    @task(3)
    def upload_and_delete(self):
        response = self.client.get("/new_photo/")
        csrftoken = response.cookies.get('csrftoken', '')

        title = f"LocustFoto{random.randint(1, 9999)}"

        self.client.post("/new_photo/", {
            "title": title,
            "csrfmiddlewaretoken": csrftoken
        }, headers={"Referer": self.host + "/new_photo/"})

        self.client.post(f"/{title}/delete/", {
            "csrfmiddlewaretoken": csrftoken
        }, name="/[slug]/delete/")

    @task(1)
    def view_random_photo_detail(self):
        self.client.get("/rzs/")
