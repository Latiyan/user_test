from django.db import models
from django.contrib.auth.models import User

# Define Constants which will be used below in model classes.
STATES_CHOICES = (
    ('AN','Andaman and Nicobar Islands'),
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CH','Chandigarh'),
    ('CT','Chhattisgarh'),
    ('DD','Daman and Diu'),
    ('DL','Delhi'),
    ('DN','Dadra and nagar Haveli'),
    ('GA','Goa'),
    ('GJ','Gujarat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JK','Jammu and Kashmir'),
    ('JH','Jharkhand'),
    ('KA','Karnataka'),
    ('KL','Kerala'),
    ('LD','Lakshadeep'),
    ('MP','Madhya Pradesh'),
    ('MH','Maharashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland'),
    ('OR','Orissa'),
    ('PB','Punjab'),
    ('PY','Pondicherry (Puducherry)'),
    ('RJ','Rajasthan'),
    ('SK','Sikkim'),
    ('TN','Tamil Nadu'),
    ('TS','Telangana'),
    ('TR','Tripura'),
    ('UK','Uttarakhand'),
    ('UP','Uttar Pradesh'),
    ('WB','West Bengal'),
)
CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)
STATUS_CHOICES = (
    ('pending','Pending'),
    ('accepted','Accepted'),
    ('packed','Packed'),
    ('on_the_way','On The Way'),
    ('delivered','Delivered'),
    ('cancelled','Cencelled'),
)


# Customer Model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    state = models.CharField(choices=STATES_CHOICES, max_length=2)
    
    def __str__(self):
        return self.id


# Product Model
class Product(models.Model):
    title = models.CharField(max_length=100)
    regular_price = models.FloatField()
    sale_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image = models.ImageField(upload_to='ProductImg')
    
    def __str__(self):
        return self.id
    
# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.id
    
# Orders Model
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=50,default='pending')
    
    def __str__(self):
        return self.id
