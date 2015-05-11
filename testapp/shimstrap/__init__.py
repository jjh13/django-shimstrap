from django.core.urlresolvers import reverse, resolve
from django.test import RequestFactory
import hashlib


def cache_object(context, name, user=None, method="GET", kwargs=None, post_data=None):
    factory = RequestFactory()
    request = None

    # Find the view
    url = reverse(name, kwargs=kwargs)
    view, args, kargs = resolve(url)

    # Create a dummy request
    if method == "POST":
        request = factory.post(url, data=post_data)
    else:
        request = factory.get(url)

    # Pass in the user
    if user is not None:
        request.user = user

    # Call the view
    response = view(request, *args, **kwargs)

    # Create the cache if it doesn't exist
    if 'ss_cache___' not in context:
        context['ss_cache___'] = []

    context['ss_cache___'] += [{
        'hash_id': hashlib.sha1(url).hexdigest(),
        'url': url,
        'method': method,
        'cached_data': response.content,
        'name': name,
        'type': response['Content-Type'],
    }]

    return context
