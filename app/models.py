from django.db import models



class Categories(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
    return self.name
         

class Brand(models.Model):
    name = models.CharField(max_length=100) 
    category = models.ForeignKey(Categories,on_delete= models.CASCADE)
    company =  models.CharField(max_length=100) 
    quantity1 = models.CharField(max_length=100) 
   
    keyfeatures4 =  models.CharField(max_length=1000)
    custemail =  models.CharField(max_length=100)
    custnumber=  models.CharField(max_length=100)
    seller =  models.CharField(max_length=100)
    description =  models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'eshop/static/images')
def __str__(self):
    return self.name
            
# Create your models here.
