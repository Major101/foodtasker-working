"""FoodtaskerAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from foodtaskerapp import views, apis
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # Sign in / Sign out /  Sign up
    path('restaurant/sign-in/', auth_views.LoginView.as_view(template_name='restaurant/sign_in.html'),
         name='restaurant-sign-in'),
    path('restaurant/sign-up/', views.restaurant_sign_up, name='restaurant-sign-up'),
    path('restaurant/sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='restaurant-sign-out'),
    # Home Page
    path('restaurant/', views.restaurant_home, name='restaurant-home'),
    # FACEBOOK AUTHORIZATION URL
    path('api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign in/ sign up)
    # /revoke-token (sign out)

    # Restaurant pages
    path('restaurant/account/', views.restaurant_account, name='restaurant-account'),
    path('restaurant/meal/', views.restaurant_meal, name='restaurant-meal'),
    path('restaurant/meal/add/', views.restaurant_add_meal, name='restaurant-add-meal'),
    path('restaurant/meal/edit/<int:meal_id>', views.restaurant_edit_meal, name='restaurant-edit-meal'),
    path('restaurant/order/', views.restaurant_order, name='restaurant-order'),
    path('restaurant/report/', views.restaurant_report, name='restaurant-report'),

    # APIs for CUSTOMERS
    path('api/customer/restaurants/', apis.customer_get_restaurants),
    path('api/customer/meals/<int:restaurant_id>', apis.customer_get_meals),
    path('api/customer/order/add/', apis.customer_add_order),
    path('api/customer/order/latest/', apis.customer_get_latest_order),
    path('api/restaurant/order/notification/<str:last_request_time>/', apis.restaurant_order_notification),

    # APIs for DRIVERS
    path('api/driver/orders/ready/', apis.driver_get_ready_orders),
    path('api/driver/order/pick/', apis.driver_pick_order),
    path('api/driver/order/latest/', apis.driver_get_latest_order),
    path('api/driver/order/complete/', apis.driver_complete_order),
    path('api/driver/revenue/', apis.driver_get_revenue),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
