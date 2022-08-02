from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerialrizer
from django.http import QueryDict
# Create your views here.

@api_view(['GET'])
def index(request):
    api_urls = {
        "List" : '/boardlist/',
        "Detail" : '/boardview/<str:pk>',
        "Create" : '/boardinsert/',
        "Update" : '/boardupdate<str:pk>/',
        "Delete" : '/boarddelete<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def UserList(request):
    boards = User.objects.all()

    serializer = UserSerialrizer(boards, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def register(request):

    serializer = UserSerialrizer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print('vailed data..')
    else:
        print('invalied data...')
    print(serializer.data)
    return Response(serializer.data)

def sign_up(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')