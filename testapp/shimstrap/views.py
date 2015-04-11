from django.http import HttpResponse


def serve_shim(request):
    return HttpResponse("Hello, world. You're at the polls index.")