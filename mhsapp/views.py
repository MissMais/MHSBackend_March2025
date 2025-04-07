from django.shortcuts import render

# Create your views here.


@api_view(["GET"])
def home(request):
    return Response("hello world")