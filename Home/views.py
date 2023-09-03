from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from .models import EmailGroup, MemberInGroups, Expenses
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
        

class AddingUsers(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            groupname = request.data["groupname"]
            print(groupname)
            email = request.data['username']
            group1, created1 = Group.objects.get_or_create(name=request.data['groupname'])
            print(group1)
            #saving the groups emails and group admin
            user = User.objects.get(username = email)
            user.groups.add(group1)
            user.save()

            #add the user included groups 
            user1 = User.objects.get(username = email)
            if MemberInGroups.objects.filter(user = user1).exists():
                user_groups = MemberInGroups.objects.get(user = user1)
            else:
                user_groups = MemberInGroups.objects.create(user = user)
            user_groups.GroupsInIt.add(group1)
            user_groups.save()
            print(email)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AddingExpenses(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            email = request.data['email']
            expense = request.data['expense']
            groupname = request.data['groupname']
            txt = email + "  added " + expense
            if Expenses.objects.filter(group_name = groupname).exists():
                group_instance = Expenses.objects.get(group_name = groupname)
                list_item = group_instance.listofExpenses
                list_item.append(txt)
                group_instance.save()
            else:
                new_list = Expenses(group_name = groupname, listofExpenses= [txt])
                new_list.save()

            return Response(status=status.HTTP_205_RESET_CONTENT)
            
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EachGroupList(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            groupname = request.data['groupname']
            ans = []
            if Expenses.objects.filter(group_name = groupname).exists():
                group_instance = Expenses.objects.get(group_name = groupname)
                list_item = group_instance.listofExpenses
                #print(list_item)
                ans = list_item

            return Response(ans)
            
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GroupMembersList(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            groupname = request.data['groupname']
            print(groupname)
            ans = []
            group_instance = Group.objects.get(name = groupname)
            users_group = User.objects.filter(groups = group_instance)
            ans = [user.username for user in users_group]

            return Response(ans)
            
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FormGroup(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            print(request.data['grpname'])
            email = request.data['email']
            group1, created1 = Group.objects.get_or_create(name=request.data['grpname'])
            print(group1)
            #saving the groups emails and group admin
            user = User.objects.get(username = email)
            user.groups.add(group1)
            user.save()

            #add the user included groups 
            user1 = User.objects.get(username = email)
            if MemberInGroups.objects.filter(user = user1).exists():
                user_groups = MemberInGroups.objects.get(user = user1)
            else:
                user_groups = MemberInGroups.objects.create(user = user)
            user_groups.GroupsInIt.add(group1)
            user_groups.save()
            print(created1)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class GetTheGroups(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            email = request.data['email']

            #add the user included groups 
            user1 = User.objects.get(username = email)
            if MemberInGroups.objects.filter(user = user1).exists():
                user_groups = MemberInGroups.objects.get(user = user1)
            else:
                return Response([])
            print(email)
            print(user_groups.user)
            data = user_groups.GroupsInIt.all()
            data_li = []
            for i in data:
                data_li.append(i.name)
            print(data_li)
            return Response(data_li)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

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

