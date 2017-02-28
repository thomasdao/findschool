from django.db import models

class School(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    school_type = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    country = models.CharField(db_index=True, max_length=100)
    country_code = models.CharField(db_index=True, max_length=10)
    state = models.CharField(db_index=True, max_length=200)
    city = models.CharField(db_index=True, max_length=200)
    website = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    area_of_study = models.TextField()
    programme = models.TextField()

    def __str__(self):
        return self.programme

class Enquiry(models.Model):
    interest = models.CharField(max_length=200)
    question = models.TextField(blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    def __str__(self):
        return "{}: {}".format(self.name, self.question)
