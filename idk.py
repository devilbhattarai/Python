class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        print(f"I am {name}. I live in {address}")
    def talk(self):
        print("Hey")

a=Person("Ram", "Aakashedhara")
b= Person("Hari", "Kapan")
Person.talk(a)