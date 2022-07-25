from django.db import models

# Create your models here.
class Testimonial(models.Model):
	testimonial_id = models.BigAutoField(primary_key=True,unique=True)
	testimonial_title = models.CharField(max_length=100, blank=False, null=False)
	testimonial_date = models.DateTimeField(null=False)
	testimonial_description = models.CharField(max_length=1000,null=False)
	thanks_count = models.IntegerField(null=False)
