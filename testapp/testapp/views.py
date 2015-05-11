from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render
from shimstrap import cache_object

import json


def test_ajax_page(request):
    t = get_template('shimstrap/test.html')
    c = template.Context({'name': 'Adrian'})

    cache_object(c, "request-for-id", kwargs={'request_id': 5})
    cache_object(c, "request-for-id", kwargs={'request_id': 6})
    cache_object(c, "request-for-id", kwargs={'request_id': 7})

    html = t.render(c)
    return HttpResponse(html)


def test_request(request, request_id=0):
    return HttpResponse(json.dumps({'hey': request_id}), content_type="application/json")