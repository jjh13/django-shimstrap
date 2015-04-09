from django.core.urlresolvers import RegexURLResolver
from django.core.exceptions import ImproperlyConfigured


def ajax_url(regex, view, ajax_name, default=None, group=None, kwargs=None):
    if isinstance(view, (list, tuple)):
        # For include(...) processing.
        urlconf_module, app_name, namespace = view

        # Check default is none
        # if it is
        #      strip out ^ and $ from regex
        #      if that's still a regex, then fail
        #      otherwise set default to that

        # make a map from
        # globalMap[group] = default_url

        return RegexURLResolver(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace)

    raise ImproperlyConfigured('Invalid view specified (%s). Are you passing the callable?' % view)
