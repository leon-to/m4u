from django.shortcuts import render, get_list_or_404
from movie.models import Movie
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
def calendar(request):
    query = request.GET.get('month_query')
    if query:
        date = datetime.strptime(query, '%Y-%m').date()
        if request.GET.get('prev'):
            date = date + relativedelta(months=-1)
        elif request.GET.get('next'):
            date = date + relativedelta(months=+1)
    else:
        date = datetime.now().date()
        
    month = {}
    month['month_info'] = date
    month['days'] = []
    iter_day = first_day_of_month = month['month_info'].replace(day=1)
    last_day_of_month = month['month_info'] + relativedelta(day=31)
    week_day = first_day_of_month.weekday()
    
    for day_idx in range(6*7):
        day = {}
        if day_idx >= week_day  and iter_day <= last_day_of_month:
            day['day_info'] = iter_day
            day['movies'] = Movie.objects.filter(release=iter_day)
            iter_day = iter_day + relativedelta(days=+1) 
            
        month['days'].append(day)


    return render(request, 'calendar.html', 
        {
            'Movie': Movie, 
            'month': month
        }
    )
