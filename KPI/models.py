from django.db import models



class Department(models.Model):
    id = models.AutoField("id",auto_created=True,unique=True,primary_key=True)
    name = models.CharField("name",max_length=255)
    number_of_employees = models.IntegerField("number of employees",null=True,blank=True)
    
    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.AutoField("id",auto_created=True,unique=True,primary_key=True)
    name = models.CharField("name",max_length=255)
    department = models.ForeignKey(Department,max_length=255,default="CC INBOUND",on_delete=models.CASCADE)
    tone_of_voice = models.FloatField("tone of voice",null=True,blank=True)
    starting_script = models.FloatField("starting script",null=True,blank=True)
    ending_script = models.FloatField("ending script",null=True,blank=True)
    solution_time = models.FloatField("solution time",null=True,blank=True)
    choice_of_words = models.FloatField("choice of words",null=True,blank=True)
    monthly_rating = models.FloatField("monthly rating",null=True,blank=True)
    prediction = models.FloatField("prediction",null=True,blank=True)
    last_month_rating = models.FloatField("last month", null=True,blank=True)
    
    def __str__(self):
        return self.name
