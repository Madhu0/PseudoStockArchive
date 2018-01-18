class HeadersMiddleware:
    def __init__(self, getResponse):
        self.getResponse = getResponse

    def __call__(self, request):
        response = self.getResponse(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['X-Frame-Options'] = 'Allow'
        return response
