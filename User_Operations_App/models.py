from django.db import models

# Personals N-worksFor->1 Bureau
# Personals 1-represents->1 Bureau
# Bureau 1-has->N Customers_of_Bureau

def set_inactive_on_delete(instance, using, keep_parents):
    instance.is_active = False
    instance.save()

# Create your models here.
class Personals(models.Model):
    id	 = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # Active or Inactive
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #created_by = 
    #updated_by =
    bureau_id = models.ForeignKey('Bureau', null=True, blank=True, on_delete=set_inactive_on_delete)

class Bureau(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    #address = models.CharField(max_length=255, null=True, blank=True)
    #city = models.CharField(max_length=100, null=True, blank=True)
    #country = models.CharField(max_length=100, null=True, blank=True)
    #postal_code = models.CharField(max_length=20, null=True, blank=True)
    #tax_office = models.CharField(max_length=100, null=True, blank=True)
    #registration_number = models.CharField(max_length=100, null=True, blank=True)
    #TODO upload_to Logos nasıl açlışır öğren
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    #phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Active or Inactive
    #personal_limit = models.IntegerField(default=5)
    #payed_date = models.DateField(null=True, blank=True)
    #next_payment_date = models.DateField(null=True, blank=True)
    #valid_until = models.DateField(null=True, blank=True) # Expiration date of the bureau's subscription !!! Derived from next_payment_date and payed_date
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #created_by =
    #updated_by =

    #TODO on_delete düzelt
    representative_id = models.OneToOneField('Personals', on_delete=models.CASCADE)

    
class Customer_of_Bureau(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    #logo nasıl olacak araştır
    logo = models.ImageField(upload_to='customer_logos/', null=True, blank=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # Active or Inactive
    #contact_gender = models.CharField(max_length=10, null=True, blank=True)
    #contact_name = models.CharField(max_length=100, null=True, blank=True)
    #contact_surname = models.CharField(max_length=100, null=True, blank=True)
    #contact_email = models.EmailField(null=True, blank=True)
    #contact_phone = models.CharField(max_length=20, null=True, blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #created_by =
    #updated_by =
    bureau_id = models.ForeignKey('Bureau', on_delete=set_inactive_on_delete, related_name="customers")