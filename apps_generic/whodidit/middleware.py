""" Middleware to provide current request user """
from threading import current_thread

from django.utils.deprecation import MiddlewareMixin


_requests = {}


def current_request():
    return _requests.get(current_thread().ident, None)


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        _requests[current_thread().ident] = request

    def process_response(self, request, response):
        _requests.pop(current_thread().ident, None)
        return response

    def process_exception(self, request, exception):
        _requests.pop(current_thread().ident, None)
        raise exception
