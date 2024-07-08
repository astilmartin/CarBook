from django.urls import path


from webapp import views

urlpatterns=[
    path('',views.homepage,name="home"),
    path('About', views.aboutpage, name="About"),
    path('contact', views.contactpage, name="contact"),
    path('vehicles',views.carspage,name="vehicles"),
    path('services',views.servicepage,name="services"),
    path('pricing',views.pricepage,name="pricing"),
    path('filtered_brands/<car_name>/', views.filtered_brands, name="filtered_brands"),
    path('singlepage/<int:carid>/', views.singlepage, name="singlepage"),
    path('register_page/', views.register_page, name="register_page"),
    path('save_register/', views.save_register, name="save_register"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('user_login_page/', views.user_login_page, name="user_login_page"),
    path('booking_page/<int:carid>/', views.booking_page, name="booking_page"),
    path('save_booking/<int:carid>/', views.save_booking, name="save_booking"),
    path('bookpage/', views.bookpage, name="bookpage"),

]