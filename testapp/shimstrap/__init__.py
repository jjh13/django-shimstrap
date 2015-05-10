from shimstrap.urls import AjaxTracker


def cache_object(request, name, dictionary_or_response):

    # Check to see if name corresponds to
    if not AjaxTracker.Instance().has_name(name):
        return

    # Create a cache on this response if none exists
    if not hasattr(request, '_ss_cached_objects'):
        request._ss_cached_objects = {}
