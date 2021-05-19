from django.db import models

# Create your models here.

gen = (('f', 'Female'), ('m', 'Male'))
class StudentRecords(models.Model):
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100, default=None)
    mname = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=6, choices=gen, default=None)
    clas = models.CharField(max_length=10)
    roll = models.IntegerField(primary_key=True)
    paper1 = models.IntegerField()
    paper2 = models.IntegerField()
    paper3 = models.IntegerField()
    paper4=models.IntegerField()
    paper5 = models.IntegerField()

    def __str__(self):
        return f"{self.sname}-{self.gender}-{self.clas}-{self.roll}-{self.paper1}-{self.paper2}-{self.paper3}-{self.paper4}-{self.paper5}"
