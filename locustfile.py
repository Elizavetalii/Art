import os
import random
from faker import Faker
from locust import HttpUser, task, constant_throughput, SequentialTaskSet, TaskSet

fake = Faker("ru_RU")

class UserFlow(SequentialTaskSet):
    @task
    def open_admin_dashboard(self):
        self.client.get("/dashboard/admin/")

    @task
    def open_admin_panel(self):
        self.client.get("/admin-panel/")

    @task
    def open_admin_users(self):
        self.client.get("/admin-panel/users/")

    @task
    def open_admin_roles(self):
        self.client.get("/admin-panel/roles/")

    @task
    def open_admin_backups(self):
        self.client.get("/admin-panel/backups/")


class RandomAct(TaskSet):
    def on_start(self):
        self.api_headers = {"Accept": "application/json"}
        self.client_ids = []
        self.created_clients = 0
        self._auth()

    def _auth(self):
        if "Authorization" in self.api_headers:
            return True
        username = os.getenv("LOCUST_USERNAME", "admin_demo")
        password = os.getenv("LOCUST_PASSWORD", "AdminDemo123!")
        resp = self.client.post(
            "/api/token/",
            json={"username": username, "password": password},
            name="/api/token/",
        )
        if resp.status_code != 200:
            return False
        try:
            token = resp.json().get("access")
        except ValueError:
            return False
        if not token:
            return False
        self.api_headers["Authorization"] = f"Bearer {token}"
        return True

    def _fetch_client_ids(self):
        if not self._auth():
            return
        resp = self.client.get("/api/clients/", headers=self.api_headers, name="/api/clients/")
        if resp.status_code != 200:
            return
        try:
            data = resp.json()
        except ValueError:
            return
        ids = [item.get("id") for item in data.get("results", []) if item.get("id")]
        self.client_ids = ids[:5]

    @task(10)
    def get_clients(self):
        if not self._auth():
            return
        self.client.get("/api/clients/", headers=self.api_headers)

    @task(10)
    def get_client_detail(self):
        if not self._auth():
            return
        if not self.client_ids:
            self._fetch_client_ids()
        if not self.client_ids:
            return
        client_id = random.choice(self.client_ids)
        self.client.get(f"/api/clients/{client_id}/", headers=self.api_headers)

    @task(10)
    def get_orders(self):
        if not self._auth():
            return
        self.client.get("/api/orders/", headers=self.api_headers)

    @task(1)
    def create_client(self):
        if not self._auth():
            return
        if self.created_clients >= 1:
            return
        payload = {
            "name": fake.company()[:255],
            "client_type": random.choice(["store", "cafe", "restaurant", "distributor", "other"]),
            "inn": str(fake.random_number(digits=10, fix_len=True)),
            "kpp": str(fake.random_number(digits=9, fix_len=True)),
            "default_delivery_address": fake.street_address()[:255],
            "email": fake.email(),
            "phone": fake.msisdn()[:15],
            "status": random.choice(["prospect", "active", "paused", "lost"]),
        }
        resp = self.client.post("/api/clients/", json=payload, headers=self.api_headers)
        if resp.status_code == 201:
            self.created_clients += 1
            try:
                new_id = resp.json().get("id")
            except ValueError:
                new_id = None
            if new_id:
                self.client_ids.append(new_id)



class WebsiteUser(HttpUser):
    wait_time = constant_throughput(5)
    tasks = [UserFlow, RandomAct]
