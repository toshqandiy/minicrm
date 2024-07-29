from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from core.views import index
from userprofile.views import signup
from customer.views import CustomerListCreateAPIView, CustomerDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/customers/', include('customer.urls')),
    # path('customer/', CustomerListCreateAPIView.as_view()),
    # path('customer/<int:pk>/', CustomerDetailView.as_view())
]

