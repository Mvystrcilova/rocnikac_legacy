from django.urls import path
from songRecommender import views


urlpatterns = [
    path('', views.index, name='index')

]