from . import views
from django.urls import path
app_name='brainwaveapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('service',views.service,name='service')
]