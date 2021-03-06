import base64

from locust import HttpUser, TaskSet, task
from random import randint, choice


class WebTasks(TaskSet):

    @task
    def load(self):
        base64string = base64.encodebytes(('%s:%s' % ('user', 'password')).encode()).decode().strip()

        catalogue = self.client.get("/catalogue").json()
        category_item = choice(catalogue)
        item_id = category_item["id"]

        self.client.get("/")
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))
        self.client.get("/basket.html")


class Web(HttpUser):
    tasks = [WebTasks]
    min_wait = 0
    max_wait = 0
