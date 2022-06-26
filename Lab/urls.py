from django.urls import path
from . import views
urlpatterns = [
     path('',views.home, name ="home"),
     path('<int:year>/<str:month>/',views.home, name = 'home'),
     path('add_malzeme',views.add_malzeme, name = 'add-malzeme'),
     path('add_deneyi',views.add_deneyi, name = 'add-deneyi' ),
     path('malzeme_listesi',views.malzeme_listesi, name = 'malzeme-listesi'),
     path('update_items/<str:pk>/', views.update_malzeme, name="update-malzeme"),
     path('update_deneyi/<str:pk>/', views.update_deneyi, name="update-deneyi"),
     path('delete_malzeme/<str:pk>/', views.delete_malzeme, name="delete_malzeme"),
     path('delete_deneyi/<str:pk>/', views.delete_deneyi, name="delete_deneyi"),
    path('Denyiler', views.deneyiler_listesi,name= 'deneyi-listesi' ),

]
