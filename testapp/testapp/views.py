from django.http import HttpResponse


def test_ajax_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")