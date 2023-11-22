from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class employeeform(models.Model):
    name = models.CharField(max_length=50)
    case_number = models.BigIntegerField()
    region = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title

    def __repr__(self):
        return str(self)

class employeeevalution(models.Model):
    overall_score = models.BigIntegerField()
    customer_score = models.BigIntegerField()
    knowledge_score = models.BigIntegerField()
    note = models.CharField(max_length=1000, null=True, blank=True)
    deep_flag = models.CharField(max_length=10)
    reason_deep = models.CharField(max_length=1000, null=True, blank=True)
    exemplary_flag = models.CharField(max_length=10)
    reason_exemplary = models.CharField(max_length=1000, null=True, blank=True)
    additionalnote = models.CharField(max_length=1000, null=True, blank=True)


    # def __str__(self) -> str:
    #     return self.title

    # def __repr__(self):
    #     return str(self)