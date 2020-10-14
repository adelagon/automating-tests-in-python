import random
from locust import HttpUser, between, task
from faker import Faker

class APIPerfTest(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.user_ids = []
        self.faker = Faker()
    
    def create_profile(self):
        
        return {
            "name": self.faker.name(),
            "username": self.faker.email().split('@')[0],
            "email": self.faker.company_email(),
            "phone": self.faker.phone_number(),
            "website": self.faker.domain_name(),
            "address": {
                "street": self.faker.street_address(),
                "suite": self.faker.building_number(),
                "city": self.faker.city(),
                "zipcode": self.faker.postcode()
            },
            "company": {
                "name": self.faker.company(),
                "catchPhrase": self.faker.catch_phrase(),
                "bs": self.faker.bs()
            }
        }
    
    @task
    def get_users(self):
        self.client.get("/users")

    @task
    def add_user(self):
        r = self.client.post("/users", self.create_profile())
        self.user_ids.append(r.json()['id'])

    @task
    def get_user(self):
        if self.user_ids:
            id = random.choice(self.user_ids)
            self.client.get("/users/{}".format(id))

    @task
    def update_user(self):
        if self.user_ids:
            id = random.choice(self.user_ids)
            self.client.put("/users/{}".format(id), self.create_profile())

    @task
    def delete_user(self):
        if self.user_ids:
            id =  random.choice(self.user_ids)
            self.client.delete("/users/{}".format(id))

