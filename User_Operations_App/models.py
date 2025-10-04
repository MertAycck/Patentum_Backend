from django.db import models



# Personals N-worksFor->1 Bureau
# Personals 1-represents->1 Bureau
# Bureau 1-has->N Customers_of_Bureau

# Create your models here.
class Personals(models.Model):
    id	 = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, unique=True)
    password = models.CharField(max_length=100)
    bureau = models.ForeignKey('Bureau', null=False, blank=False)
    status = models.BooleanField(default=True)  # Active or Inactive

class Bureau(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    #TODO upload_to Logos nasıl açlışır öğren
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    personal_limit = models.IntegerField(default=5)
    representative = models.OneToOneField('Personals')
    status = models.BooleanField(default=True)  # Active or Inactive
    
class Customer_of_Bureau(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='customer_logos/', null=True, blank=True)
    bureau = models.ForeignKey('Bureau', null=False, blank=False)
    status = models.BooleanField(default=True)  # Active or Inactive