import string
import random


class PasswordGenerator:
    def __init__(self, admin_length, user_length):
        self.admin_length = admin_length
        self.user_length = user_length
        

    def generate_password(self,role):
        if role == "admin" :
            return ''.join(random.choices(string.ascii_letters + string.digits, k=self.admin_length))
        elif role == "user":
            return ''.join(random.choices(string.ascii_letters + string.digits, k=self.user_length))
        else:
            return "Invalid role"

class Authenticator:
    def __init__(self, admin_password, user_password):
        self.admin_password = admin_password
        self.user_password = user_password

    def authenticate(self, role, password):
        if role == "admin" and password == self.admin_password:
            return True
        else:
            return False

password_generator = PasswordGenerator(5, 6)
role = input("What is your role(role):" )
admin_password = password_generator.generate_password("admin")
user_password = password_generator.generate_password("user")
password = password_generator.generate_password(role)
print(password)
authenticator = Authenticator(admin_password, user_password)  