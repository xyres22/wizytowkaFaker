from faker import Faker
fake = Faker('pl_PL')

class BaseContact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}'
    
    def contact(self):
        print(f'Wybieram numer {self.phone} i dzwonie do {self.name}')

    @property
    def label_length(self):
        return len(self.name)

x = BaseContact(name="jan koko", phone= '1234', email="asd@op.pl")
print(x)

    
class BusinessContact(BaseContact):
    def __init__(self,job,company,work_phone, *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_phone = work_phone

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}, {self.job}, {self.company}, {self.work_phone}'

    def contact(self):
        print(f'Wybieram numer {self.work_phone} i dzwonie do {self.name}')

    @property
    def label_length(self):
        return len(self.name)

b = BusinessContact(name='Pawel Sroka', phone='999', email='przyklad@wp.pl', job='elektryk', company='PZU', work_phone='888222')
print(b)

def create_contact(rodzaj, numer):
    if rodzaj == BaseContact:
        for i in range(0,numer):
            i = BaseContact(name=fake.name(),phone=fake.phone_number(), email=fake.email())
            print(i)
    if rodzaj == BusinessContact:
        for i in range (0, numer):
            i = BusinessContact(name=fake.name(),phone=fake.phone_number(), email=fake.email(), job=fake.job(),company=fake.company(),work_phone=fake.phone_number())
            print(i)

create_contact(BusinessContact, 5)

        










  
    

