from django.db import models



class Department(models.Model):
    name = models.CharField("name",max_length=255)
    number_of_employees = models.IntegerField("number of employees",null=True,blank=True)
    
    def __str__(self):
        return self.name
class Employee(models.Model):
    name = models.CharField("name",max_length=255, null=True, blank=True)
    department = models.ForeignKey(Department,max_length=255,default="CC INBOUND",on_delete=models.CASCADE)
    
    tone_of_voice = models.FloatField("tone of voice",null=False,blank=False, default=0.0)
    starting_script = models.FloatField("starting script",null=False,blank=False, default=0.0)
    ending_script = models.FloatField("ending script",null=False,blank=False, default=0.0)
    resolution_time = models.FloatField("solution time",null=False,blank=False, default=0.0)
    choice_of_words = models.FloatField("choice of words",null=False,blank=False, default=0.0)
    clarity = models.FloatField("clarity", null=False, blank=False, default=0.0)
    onCallComplaintChecking = models.FloatField("on call complaint checking", null=False, blank=False, default=0.0)
    handlingUnderPressure = models.FloatField("handling under pressure", null=False, blank=False, default=0.0)
    ticketRaising = models.FloatField("ticket raising", null=False, blank=False, default=0.0)
    billableTime = models.FloatField("billable time", null=False, blank=False, default=0.0)

    monthly_rating = models.FloatField("monthly rating",null=False,blank=False, default=0.0)
    last_month_rating = models.FloatField("last month", null=False,blank=False, default=0.0)
    time_of_eval = models.DateTimeField("time of evaluation", auto_now=True)
    
    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField("name", max_length=255, null=False, blank=False)
    user = models.ForeignKey(Employee,max_length=255,on_delete=models.CASCADE)
    Address1 = models.CharField("address1", max_length=255, null=False, blank=True)
    Address2 = models.CharField("address2", max_length=255, null=False, blank=True)
    houseNumber = models.CharField("houseNumber", max_length=255, null=True, blank=True)


    