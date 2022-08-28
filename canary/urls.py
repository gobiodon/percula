from django.urls import path
from . import views

urlpatterns = [
    path('<str:urlstr>/login/', views.loginpage, name='loginpage'),
    path('<str:urlstr>/files/<str:filename>', views.files, name='files'),
    path('<str:urlstr>/docfile.png', views.docfile, name='docfile'),
]