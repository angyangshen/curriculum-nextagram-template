from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin


class User_(UserMixin,BaseModel):
    username = pw.CharField(unique=False)
    password = pw.CharField()
    email = pw.CharField()

    # def validate(self):
    #     if len(self.password)<6:
    #         self.errors.append('Password length needs to be at least 6 characters long.')
    #     else   
