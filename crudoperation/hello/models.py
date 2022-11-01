from django.db import models

GENDER_CHOICES = (
    ('1', "Male"),
    ('2', "Female"),

)
    
degree_CHOICES = (
    ('1','bsc'),
    ('2', 'bcom'),
)
class Details(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=255)
    gender=models.CharField(max_length=255,choices=GENDER_CHOICES)
    degree=models.CharField(max_length=20,choices=degree_CHOICES)
    date_field=models.DateField()
    # image_user=models.ImageField(upload_to='media/pics',default=None)
    