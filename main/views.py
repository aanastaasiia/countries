from django.shortcuts import render
from django.http import HttpResponse
import requests
import sqlite3
# Create your views here.

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()



def index(request):
    page = request.GET.get('page', 1)
    return render(request=request, template_name='index.html')

def country(request):
    coun = request.GET.get('id', 1)
    filtr = request.GET.get('filter', 'ASC')
    if request.method == 'GET':
        cursor.execute('FROM Country SELECT * WHERE id = ?', (coun ,))
        context = cursor.fetchall
        return render(request=request, template_name='country.html')
    
connection.close()
