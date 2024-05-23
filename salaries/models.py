from django.db import models

class SalaryData(models.Model):
    year = models.IntegerField()
    job_title = models.CharField(max_length=255)
    salary = models.FloatField()

    def __str__(self):
        return f"{self.year} - {self.job_title} - {self.salary}"

