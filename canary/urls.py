from django.urls import path
from . import views

urlpatterns = [
    path('<slug:urlstr>/login/', views.loginpage, name='loginpage'),
    path('<slug:urlstr>/files/<str:filename>', views.files, name='files'),
    path('<slug:urlstr>/docfile.png', views.docfile, name='docfile'),
]