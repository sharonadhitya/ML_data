import csv
from salaries.models import SalaryData
from django.conf import settings

def run():
    csv_path = settings.BASE_DIR / 'salaries' / 'ml_salaries.csv'
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            year = row['work_year']
            job_title = row['job_title']
            salary = row['salary']
            SalaryData.objects.create(year=int(year), job_title=job_title, salary=float(salary))
