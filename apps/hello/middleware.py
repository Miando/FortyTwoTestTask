from . models import RequestModel


class PersonMiddleware(object):

    def process_request(self, request):
        request_info = RequestModel(
            url=request.path,
            method=request.method,
        )
        request_info.save()
