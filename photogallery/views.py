from django.shortcuts import render

from django.http  import HttpResponse

import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Photo Gallery')

def photo(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)