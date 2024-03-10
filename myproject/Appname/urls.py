from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mainpage),
    path('login',views.login,name="Login"),
    path('signUp', views.sign,name="SignUp"),
    path('forget',views.forget,name="Forget"),
    path('dashboard/',views.dashboard,name="Dashboard"),
    path('dashboard/AddtoCart/cart',views.Cart,name="Cart"),
    path('location/dashboard',views.dashboard),
    path('location/',views.Location,name="Location"),
    path('dashboard/cart',views.Cart,name="Cart"),
    path('location/cart',views.Cart,name="Cart"),
    path('dashboard/AddtoCart/',views.AddToCart,name="AddtoCart"),
    path('dashboard/Groceries',views.Groceries,name="Groceries"),
    path('location/AddtoCart/',views.AddToCart,name="AddtoCart"),
    path('location/AddtoCart/cart', views.Cart, name="Cart"),
    path('location/Groceries',views.Groceries,name="Groceries"),
    path('Admin',views.Admin),
    path('dashboard/Electronics',views.Electronics,name="Electronics"),
    path('location/Electronics',views.Electronics,name="Electronics"),
    path('dashboard/Clothes',views.Clothes,name="Clothes"),
    path('location/Clothes',views.Clothes,name="Clothes"),
    path('dashboard/Books', views.Books, name="Books"),
    path('location/Books', views.Books, name="Books"),
    path('AdminLogin', views.AdminLogin, name="AdminLogin"),
    path('dashboard/Payment',views.Payment,name="Payment"),
    path('location/Payment',views.Payment,name="Payment"),
    path('dashboard/AddtoCart/Payment',views.Payment,name="Payment"),
    path('location/AddtoCart/Payment',views.Payment,name="Payment"),
    path('dashboard/NetBanking',views.NetworkBank,name="NetBanking"),
    path('AboutUs',views.Aboutus,name="AboutUs"),
    path('checklogin',views.checklogin),
    path('Otpcheck/',views.OTP,name="Otpcheck"),
    path('OTPGenerate',views.OTP,name="OTPGenerate"),
    path('ValidateOTP',views.validateOTP,name="ValidateOTP"),
    path('VerifyOTP/',views.verify,name="VerifyOTP"),
]
