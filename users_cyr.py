class User:
    def __init__(self, number, age, first_name, last_name):
        self.age = age
        
        self.number = number
        
        self.first_name = first_name
        
        self.last_name = last_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and is {self.number} feet tall.")

    def greet_user(self):
        print(f"Hello, how are you doing, {self.first_name} {self.last_name}.")

        
user = User("six", "fifteen", "Linus", "Cyr")
user.greet_user()
user.describe_user()

attributes = User("five", "fourteen", "Sam", "Trares")
attributes.describe_user()
attributes.greet_user()


person = User("six", "fourteen", "Colby", "Arnold")
person.describe_user()
person.greet_user()



# print(f"The user is {user.age}")
# print(f"The user is {user.number}")




