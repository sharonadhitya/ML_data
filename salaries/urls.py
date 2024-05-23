from django.urls import path
from .views import salary_table,job_titles

urlpatterns = [
    path('', salary_table, name='salary_table'),
    path('<int:year>/', job_titles, name='job_titles'),
]
