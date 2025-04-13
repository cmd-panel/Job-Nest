from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GeneralInfo(models.Model):
    #creating attribute means creating column with attribute name
    company_name = models.CharField(max_length=255,default="company")
    company_location = models.CharField(max_length=255,)
    email= models.EmailField()
    phone= models.CharField(max_length=30,blank=True, null=True)
    #blank= true and null= true means this field is optional, data dileo
    #hoy na dileo hoy but email,company_name etc aisob e value na dile nibe na

    def __str__(self):
        return self.company_name
        #this will display the data as company name in database


#post table

class UserMadePost(models.Model):
    #creating attribute means creating column with attribute name
    title = models.CharField(max_length=255,default="post")
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now_add=True means this field will be automatically set to now when the object is created.
    #auto_now=True means this field will be updated to now every time the object is saved.

