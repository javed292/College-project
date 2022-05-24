from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    subject= models.CharField(max_length=20)
    desc = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    # teacher_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="webb/images",default="")

    def __str__(self):
        return self.product_name

