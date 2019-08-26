from django.utils.deprecation import  MiddlewareMixin
from django.shortcuts import redirect

class MyMiddleAware2(MiddlewareMixin):
    def __init__(self,get_response):
        super().__init__(get_response)
    def process_request(self, request):
        if "login" not in request.path or "regist" in request.path:
            pass
        else:
            seession=request.seession.get("login")
            if seession:
                pass
            else:
                return redirect("login:login")
