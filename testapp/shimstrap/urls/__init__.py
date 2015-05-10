from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
import re


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    Source: http://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons-in-python

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class AjaxTracker(object):
    def __init__(self):
        self.url_map = {}
        self.group_map = {}
        self.url_regex = re.compile(r'[a-zA-Z0-9\\/]')

    def has_name(self, name):
        return name in self.url_map

    def add_ajax_url(self, url, ajax_name, default, group):
        if default is None:
            default = url

            if default[0] == '^':
                default = default[1:]

            if default[-1] == '$':
                default = default[:-1]

            if not self.url_regex.match(default):
                raise ImproperlyConfigured("Couldn't construct default url from regex, please specify default url")

        self.url_map[ajax_name] = default
        if group is not None:
            if group not in self.group_map:
                self.group_map[group] = {}
            self.group_map[group][ajax_name] = default


def ajax_url(regex, view, ajax_name, default=None, group=None, kwargs=None):
    if isinstance(view, (list, tuple)):
        urlconf_module, app_name, namespace = view
        AjaxTracker.Instance().add_ajax_url(regex, ajax_name, default, group)
        return RegexURLResolver(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace)

    if isinstance(view, six.string_types):
        raise ImproperlyConfigured('Invalid view specified (%s). Are you passing the callable?' % view)

    AjaxTracker.Instance().add_ajax_url(regex, ajax_name, default, group)
    return RegexURLPattern(regex, view, kwargs, ajax_name)
