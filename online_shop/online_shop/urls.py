from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from userapp.views import *
from sotuvapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name="home1"),
    path('home2/', Home2View.as_view(), name='home2'),
    path('all-categories/', AllCategories.as_view(), name='all_category'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('all-products/', AllProducts.as_view(), name='all_products'),
    path('product/<int:a>/', SingleProduct.as_view(), name='single_product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order/<int:a>/', OrderSingleProduct.as_view(), name='order_single_product'),
    path('profile-orders/', ProfileOrders.as_view(), name='profile_orders'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

















