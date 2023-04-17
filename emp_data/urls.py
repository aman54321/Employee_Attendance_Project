from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("show",views.show,name='show'),
    path("atten",views.atten,name='atten'),
    path("user_login",views.user_login,name='user_login'),
    path("user_data",views.user_data,name='user_data'),
    # path('register',views.register,name="register"),
    path('create',views.create,name="create"),
    path("index",views.show_all_data,name='show_all_data'),
    path("signin",views.signin,name='signin'),
    path("edit/<int:pk>", views.edit, name='edit'), 
    path("delete/<int:pk>",views.delete,name='delete'),
    path("logout",views.logout,name='logout'),
    path('register', views.user_register, name='user_register'),
    path('show1', views.show1, name='show1'),
    path('accept/<int:pk>', views.accept, name='accept'),
    path('decline/<int:pk>', views.decline, name='decline')
]