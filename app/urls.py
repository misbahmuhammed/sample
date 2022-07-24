from django.urls import path
from app import views
from .forms import MyPasswordChangeForm
from django.conf import settings
from app import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm,MyPasswordResetForm
urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    path('mobile/', views.mobile, name='mobile'),
    path('app/login/',auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name='login.html'),name='logout'),
    path('checkout/',views.checkout,name='checkout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm),name='passwordchange'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('registration/',views.CustomerRegistarionView.as_view(),name= 'customerregistration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
