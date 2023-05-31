from django.db import models
class user1(models.Model) :
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField(max_length=254)
    user_contact=models.CharField(max_length=10)
    user_password=models.CharField(max_length=6)
    user_city=models.CharField(max_length=20)
    user_state=models.CharField(max_length=25)
    user_pincode=models.DecimalField(max_digits=6,decimal_places=0)

class Category(models.Model):
    categoryname = models.CharField(max_length=200)
    img=models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryname
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img=models.ImageField(upload_to='product')
    price = models.IntegerField()
    description = models.TextField()
    quantity=models.IntegerField()



# Create your models here.
