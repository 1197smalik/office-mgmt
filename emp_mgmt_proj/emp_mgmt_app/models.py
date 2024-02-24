from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.department}"
