from django.db import models
from django.contrib.auth.models import User

# Create your models here.
category_choices = (
    ('MC', 'Mac'),
    ('ID', 'IPad'),
    ('IP', 'IPhone'),
    ('WT', 'Watch'),
    ('AP', 'Airpods'),
    ('TV', 'TV & Home'),
    ('ET', 'Entertainment'),
    ('AC', 'Accessories'),
)
class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default='1'
    )
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=50, default='xyz')
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=500, 
                                default='''Lorem, ipsum dolor sit amet consectetur adipisicing elit. A nam voluptate assumenda recusandae officia et consequatur, 
    nobis voluptatem incidunt laborum harum doloribus aspernatur iure aperiam adipisci quas alias ea delectus!''')
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://assets.website-files.com/61ed56ae9da9fd7e0ef0a967/61f12e3a57bdb3717fbf9cec_Product_Default.svg"
    )
    
    category=models.CharField(choices=category_choices, max_length=2, null=True)
    
    def __str__(self):
        return self.item_name
    

class History(models.Model):

    user_name = models.CharField(max_length=100)
    prod_ref = models.IntegerField(default=100)
    item_name  = models.CharField(max_length=200)
    op_type = models.CharField(max_length=100)

    def __str__(self):
        return str(
            (
                self.prod_ref,
                self.user_name,
                self.item_name,
                self.op_type
            )
        )
        
