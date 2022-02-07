from django.shortcuts import render
from datetime import datetime

current_task = [
    'Create a simple Django Project',
    'Learn about the various template functions django provides',
    'Learn to deploy the project'
]


# Create your views here.
def index_page(request):
    return render(request, 'index.html',
                  context={
                      'cur_date': str(datetime.now()),
                      'tasks': current_task,
                  })
