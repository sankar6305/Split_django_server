from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from .models import EmailGroup
import json


def Home(request):
    print(request.POST)
    dc = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4}
    return JsonResponse(dc)


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)
    def post(self, request):
        content = request.post
        print(content)
        return Response(content)

@csrf_exempt
def Register(request):
    if(request.method == 'POST'):
        content = json.loads(request.body)
        print(content)
        name = content['data']['name']
        username = content['data']['username']
        password = content['data']['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("notunique")
        print(content['data'])
        user = User.objects.create_user(username, username, password)
        print("Creating is ok")
        user.save() 

        return HttpResponse("ok")
    else:
        return HttpResponse("ok")
        


class FormGroup(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            print(request.data['grpname'])
            group1, created1 = Group.objects.get_or_create(name=request.data['grpname'])
            print(group1)
            print(created1)

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        getAllGroups = Group.objects.values_list('name', flat=True)
        print(getAllGroups)
        li = []
        for name in getAllGroups:
            print(name)
            li.append(name)
        return JsonResponse({'data' : json.dumps(li)})

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

