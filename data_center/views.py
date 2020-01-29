from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from celery.decorators import task

@task(name="print_hello")
def print_hello():
    print("hello")

class Home(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        return render(request,"data_center/home.html")

    def post(self,request):
        print_hello.apply_async( countdown=10)
        return render(request, "data_center/home.html")