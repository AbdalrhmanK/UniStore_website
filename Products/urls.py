from django.urls import path
from . import views

urlpatterns = [
     path('', views.Login, name='login'),
    path('signup/',views.Signup, name='signup'),
    path('base', views.base, name='base'),
    path('add' , views.add , name='add'),
    path('home',views.home , name='home'),
    path('logout', views.logout_view, name='logout'),
    path('Cart', views.Cart, name='Cart'),
    path('<int:product_id>' ,views.view , name="view" ),
    path('userAdd/<int:product_id>' ,views.userAdd , name="userAdd" ),
    path('edit/<int:product_id>' ,views.edit , name="edit" ),
    path('cart/increase/<int:product_id>', views.increase_quantity, name='increase'),
    path('cart/decrease/<int:product_id>', views.decrease_quantity, name='decrease'),
    path('update/<int:product_id>' ,views.update , name="update" )

]