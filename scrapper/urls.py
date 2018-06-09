from django.urls import path

from scrapper import views

urlpatterns = [
    path('', views.toy_list, name='toy_list'),
    path('view/<int:pk>', views.toy_view, name='toy_view'),
    path('new', views.toy_create, name='toy_new'),
    path('edit/<int:pk>', views.toy_update, name='toy_edit'),
    path('delete/<int:pk>', views.toy_delete, name='toy_delete'),
]