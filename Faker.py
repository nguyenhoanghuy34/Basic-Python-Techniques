from faker import Faker

class Person:
    def __init__(self):
        fake = Faker()
        self.name = fake.name() 
        self.age = fake.random_int(min=18, max=100) 
        self.email = fake.email() 
        self.address = fake.address() 
        self.phone_number = fake.phone_number() 
        self.job = fake.job() 
        self.country = fake.country()

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}\nAddress: {self.address}\nPhone: {self.phone_number}\nJob: {self.job}\nCountry: {self.country}"


people = [Person() for _ in range(10)] 

for person in people:
    print(person)
    print("-" * 50)
