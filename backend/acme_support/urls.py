from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='Register'),
    path('register/<int:pk>', UserRegistrationView.as_view(), name='user delete'),
    path('department/', DepartmentView.as_view(), name='Department'),
    path('departmentupdate/<int:pk>', DepartmentUpdateView.as_view(), name='Department Update'),
    path('login/', UserLoginView.as_view(), name='Login'),
    path('userlist/', UserListView.as_view(), name='User List'),
    path('user/', UserView.as_view(), name='User '),
    path('tickets/', TicketView.as_view(), name='Tickets'),
    path('singleusertickets/', TicketsingleView.as_view(), name='Tickets'),
    path('tickets/<int:pk>', TicketView.as_view(), name='Tickets'),

]