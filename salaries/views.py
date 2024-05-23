from django.shortcuts import render
from django.db.models import Count, Avg
from .models import SalaryData

def salary_table(request):
    sort_by = request.GET.get('sort_by', 'year')
    order = request.GET.get('order', 'asc')
    
    if order == 'asc':
        data = SalaryData.objects.values('year').annotate(
            total_jobs=Count('id'),
            average_salary=Avg('salary')
        ).order_by(sort_by)
    else:
        data = SalaryData.objects.values('year').annotate(
            total_jobs=Count('id'),
            average_salary=Avg('salary')
        ).order_by(f'-{sort_by}')

    # Prepare data for the line chart
    chart_data = SalaryData.objects.values('year').annotate(
        total_jobs=Count('id')
    ).order_by('year')

    years = [entry['year'] for entry in chart_data]
    total_jobs = [entry['total_jobs'] for entry in chart_data]

    return render(request, 'salaries/salary_table.html', {
        'data': data,
        'sort_by': sort_by,
        'order': order,
        'years': years,
        'total_jobs': total_jobs
    })

def job_titles(request, year):
    job_data = SalaryData.objects.filter(year=year).values('job_title').annotate(
        count=Count('job_title')
    ).order_by('-count')
    return render(request, 'salaries/job_titles.html', {'year': year, 'job_data': job_data})
