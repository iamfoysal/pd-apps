from django.db import models

# Create your models here.
class Asgard(models.Model):
    #id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    instruments = models.CharField(max_length=100)

    # class Meta: 
    #     db_table = "asgard" # this meta class change database table name 

    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    #id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Asgard, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    
    rating=(
        (1, "Good"),
        (2, "Very good"),
        (3, "Not Good"),
        (4, "Excellent"),
        (5, "Ultra Excellent")
    )
    num_stars = models.IntegerField(choices=rating)
    # class Meta:
    #     db_table = "album"

    def __str__(self) :
        return self.name + ", Rating: " + str(self.num_stars)

