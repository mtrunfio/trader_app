from django.urls import path

from . import views

app_name = 'exchanges'
urlpatterns = [
    #/exchanges/
    path('', views.index, name='index'),
    #ex: /exchanges/1/
    path('<int:exchange_id>/', views.detail, name='detail')
]