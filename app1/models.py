from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=30)
    def __str__(self):
        return self.category_name

class products(models.Model):
    category_name = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    Order_date = models.DateField()
    Rating = models.TextField()
    del_date = models.DateField()

    def __str__(self):
        return self.name



class signup(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=8,default='')
    Password1 = models.CharField(max_length=8,default='')
    forgot_ans = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.Username

class login(models.Model):
    Email = models.EmailField(default='')
    Password = models.CharField(max_length=8,default='')

    def __str__(self):
        return self.Email

class items(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.IntegerField()   
    image = models.ImageField(upload_to='pro_img',blank=True)

    def __str__(self):
        return self.Title

class Mycart(models.Model):
    person = models.ForeignKey(signup,on_delete=models.CASCADE)
    Item = models.ForeignKey(items,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on= models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.person.Username

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(signup,on_delete=models.CASCADE)
    Bitem = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=80)
    ordered_on = models.DateTimeField(auto_now_add=True,null=True)
    qrimage = models.ImageField(upload_to='media',blank=True,null=True)
    invoice = models.FileField(default='')

    def __str__(self):
        return self.Bitem