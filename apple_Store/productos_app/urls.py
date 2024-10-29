from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lambda request: redirect('producto_list')),
    path('inicio/', views.producto_list, name='producto_list'),  
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),  
    path('comprar/', views.realizar_compra, name='realizar_compra'),  
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'), 
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('ver-pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('login/', LoginView.as_view(template_name='productos_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
