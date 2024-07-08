from django.urls import path

from backend import views

urlpatterns=[
    path('main_page/',views.main_page,name="main_page"),
    path('new_page/', views.new_page, name="new_page"),
    path('details_page/', views.details_page, name="details_page"),
    path('Show_product/', views.Show_product, name="Show_product"),
    path('edit_page/<int:proid>/', views.edit_page, name="edit_page"),
    path('update_product/<int:proid>/', views.update_product, name="update_product"),
    path('delete_product/<int:proid>/', views.delete_product, name="delete_product"),
    path('login_page/',views.login_page,name="login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('car_page/', views.car_page, name="car_page"),
    path('cdetails_page/', views.cdetails_page, name="cdetails_page"),
    path('show_cars/', views.show_cars, name="show_cars"),
    path('edit_cars/<int:carid>/', views.edit_cars, name="edit_cars"),
    path('update_cars/<int:carid>/', views.update_cars, name="update_cars"),
    path('delete_cars/<int:carid>/', views.delete_cars, name="delete_cars"),
]