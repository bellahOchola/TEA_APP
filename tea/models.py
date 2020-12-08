from django.db import models
# from pyuploadcare.dj.models import ImageField


# Create your models here.

class Variety(models.Model):

    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 100, default=True)
    # pic = ImageField(manual_crop='', blank=True)
    
    def save_variety(self):
        self.save()

    def delete_variety(self):
        self.delete()
   
    


class newProduct(models.Model):
    gradeId = models.CharField(max_length = 30)
    gradeName = models.CharField(max_length = 30)
    employeeName = models.CharField(max_length = 30)
    quantity = models.CharField(max_length = 30)
    description = models.TextField(max_length = 300)
    varieties = models.ForeignKey(Variety, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.gradeName

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()

class Suppliers(models.Model):
    name = models.CharField(max_length = 30)
    contact = models.CharField(max_length = 30)
    grade_supplied = models.ForeignKey(Variety, on_delete=models.CASCADE, null=True)
    Location = models.CharField(max_length = 30, default = True)