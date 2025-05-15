from locust import HttpUser, task

class ApiUser(HttpUser):
    @task
    def login(self):
        self.client.post("/login", json={"username":"test", "password":"test"})
