"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views as v1
from Ticket_Booking import views as v2
from Admin import views as v3

urlpatterns = [
    path('',v1.home),
    path('admin', admin.site.urls),
    path('bms',v1.home),
    path('signup',v1.signup, name='signup'),
    path('Sign',v1.Sign),
    path('forpass',v1.forpass, name='forpass'),
    path('Forpass',v1.Forpass),
    path('login',v1.login,name='login'),
    path('logout',v2.logout),
    path('ticbook',v2.ticbook),
    path('search',v2.search),
    path('book',v2.book),
    path('pay',v2.pay),
    path('profile',v2.profile),
    path('cancel',v2.cancel),
    path('cancelticket',v2.cancelticket),
    path('bus',v3.bus),
    path('bank',v3.bank),
    path('aprofile',v3.aprofile),
    path('addbus',v3.addbus),
    path('add',v3.add),
    path('delbus',v3.delbus),
    path('delete',v3.delete),
    path('addacc',v3.addacc),
    path('addaccount',v3.addaccount),
    path('delacc',v3.delacc),
    path('deleteacc',v3.deleteacc),
    path('tb',v2.tb),
    path('ctr',v2.ctic),
    path('as',v3.about_us,name='about_us'),
    path('edit',v3.edit),
    path('editbus',v3.editbus),
    path('editacc',v3.editacc),
    path('editaccount',v3.editaccount),
    path('cav',v2.cav)
]

