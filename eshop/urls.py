from django.contrib import admin
from django.forms.fields import URLField
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from shop.views import accounts, changePasswordView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('contact/', include('contact.urls', namespace='contactPage')),
    path('accounts/', accounts.as_view(), name='accountPage'),
    path('accounts/logout/', LogoutView.as_view(), name='logoutPage'),
    path('accounts/password-change/', changePasswordView.as_view(), name = 'passwordChange'),


    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(
        template_name = 'accounts/passwordReset.html'
    ), name = 'password_reset'),

    path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'accounts/passwordResetConfirm.html',
    ), name='password_reset_confirm'),

    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'accounts/passwordResetDone.html'
    ), name='password_reset_done'),

    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'accounts/passwordResetComplete.html'
    ), name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)