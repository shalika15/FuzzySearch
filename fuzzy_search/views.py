from django.shortcuts import render, redirect
import csv
import os
from .models import WordData
import json
from django.http import HttpResponse


def import_data(request):
    path = '/Users/shalikanigam/Desktop/assignments/ockypock/FuzzySearch'
    os.chdir(path)
    with open('test.csv') as f:
        reader = csv.reader(f)
        for row in reader:
                p = WordData(word_id=row[1], name=row[0])
                p.save()
    return render(request, 'DataSearch.html')
    # return redirect('search_data')


def search_data(request):
    if request.is_ajax():
        qs = request.GET.get('term', '')
        words = WordData.objects.filter(name__icontains=qs)[:20]
        results = []
        for word in words:
            word_json = {}
            word_json['id'] = word.word_id
            word_json['label'] = word.name
            word_json['value'] = word.name
            results.append(word_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    type_m = 'application/json'
    return HttpResponse(data, type_m)

