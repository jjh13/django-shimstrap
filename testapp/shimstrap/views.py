from django.http import HttpResponse
from django.shortcuts import render
from shimstrap.urls import AjaxTracker


def serve_shim(request):
    tracker = AjaxTracker.Instance()

    return render(request, 'shimstrap/loader.js', {'urlmap': [(k,tracker.url_map[k]) for k in tracker.url_map]})