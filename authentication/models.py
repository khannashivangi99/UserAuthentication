from django.db import models
from common_utils.models import BaseModel
# Create your models here.

class User(BaseModel):

    class Meta:
        db_table = 'user'
    
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    country_code = models.CharField(max_length=3)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)

class UserAddress(BaseModel):

    class Meta:
        db_table='user_address'

    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    address=models.CharField(max_length=20)
    pin_code=models.CharField(max_length=6)

class UserType(models.Model):
    class Meta:
        db_table='user_type'
    u_type=models.CharField(max_length=20)

