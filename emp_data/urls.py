from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("user_login",views.user_login,name='user_login'),
    path("user_data",views.user_data,name='user_data'),
    path('register',views.register,name="register"),
    path("index",views.show_all_data,name='show_all_data'),
    path("signin",views.signin,name='signin'),
    path("edit/<int:pk>", views.edit, name='edit'), 
    path("delete/<int:pk>",views.delete,name='delete'),
    path("logout",views.logout,name='logout'),
]