from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('home/', views.HomeView.as_view(), name ='homeView'),
    path('register/', views.Register, name ='register'),
    path('formgroup/', views.FormGroup.as_view(), name ='formgroup'),
    path('addingusers/', views.AddingUsers.as_view(), name ='AddingUsers'),
    path('addingexpenses/', views.AddingExpenses.as_view(), name ='AddingExpenses'),
    path('eachgrouplist/', views.EachGroupList.as_view(), name ='EachGroupList'),
    path('UsersList/', views.GroupMembersList.as_view(), name ='GroupMembersList'),
    path('getthegroups/', views.GetTheGroups.as_view(), name ='GetTheGroups'),
]
