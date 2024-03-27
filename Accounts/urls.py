from django.urls import path
from Accounts.views import *

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
]

app_name = 'Accounts'