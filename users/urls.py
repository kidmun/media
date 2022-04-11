from django.urls import path
from . import views

urlpatterns=[
    path('',views.front,name="front"),
    path('account/<str:pk>/',views.account,name="account"),
    path('projects/',views.projects,name="projects"),
    path('add_project/',views.addProject,name="add_project"),
    path('edit_project/<str:pk>/',views.editProject,name="edit_project"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('groups/',views.groupPage,name="groups"),
    path('each_group/<str:pk>/',views.eachGroup,name="each_group"),
    path('user_account/<str:pk>/',views.userAccount,name="user_account"),
    path('users/',views.usersPage,name="users"),
    path('edit_account/<str:pk>/',views.editAccount,name="edit_account"),
    path('followers/<str:pk>/',views.follwersPage,name="followers"),
    path('following/<str:pk>/',views.followingPage,name="following")
]
