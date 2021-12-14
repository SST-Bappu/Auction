from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('',userlogin,name='login'),
    path('home/',home,name='home'),
    path('userauction/',userAuctions,name='userauction'),
    path('logout/',userlogout,name='logout'),
    path('addauction/',AddAuction,name='addauction'),
    path('bid/<str:id>/',bid,name="bid"),
    path('admindash/',admin_dash,name="admin_dash"),
]
