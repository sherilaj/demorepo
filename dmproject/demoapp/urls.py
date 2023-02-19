
from . import views
from django.urls import path
app_name='demoapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('about',views.about,name='about')
    # path('add/',views.addition,name='addition')
    # path('about/',views.about,name='ab'),
    # path('contact/',views.contact,name='contact'),
    # path('detail/',views.detail,name='detail'),
    # path('thanx/',views.thanx,name='than')
]