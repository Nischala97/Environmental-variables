from django.db import models

# Create your models here.
class data(models.Model):
	#Environmental variables
	temp=models.IntegerField()
	humd=models.IntergerField()

	#area
	latitude = models.FloatField()
	longitude= models.FloatField()

    #Time
    year = models.IntegerField(default=2017)
    month= models.IntegerField(default=11)


    def __str__(self):
    	return str(self.latitude) + " " + str(self.longitude)