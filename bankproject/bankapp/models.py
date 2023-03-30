
from django.db import models

# Create your models here.
from django.db import models

# class District(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Branch(models.Model):
#     name = models.CharField(max_length=100)
#     district = models.ForeignKey(District, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name




class Registration(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    mail_id = models.EmailField(max_length=100)
    address = models.TextField(max_length=100)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    # district = models.ForeignKey(District, on_delete=models.CASCADE)
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    district= models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20)
    materials_provide = models.CharField(max_length=100)



    def __str__(self):
        return self.name


#
# class Person(models.Model):
#     name = models.CharField(max_length=124)
#     country = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
#     city = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name



