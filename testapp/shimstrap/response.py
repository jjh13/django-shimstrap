from shimstrap.urls import AjaxTracker


# decorator
def decorate_for_ajax(function):
    def new_function(*args, **kwargs):
        response = function(*args, **kwargs)
        if 'ss_cache' in kwargs and kwargs['ss_cache']:
            if response.type != 'ajax':
                pass #raise exception
            return response.data
        return response
    return new_function