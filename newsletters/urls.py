from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import newsletter_signup, newsletter_unsubscribe, home_newsletters

app_name="newsletters"

urlpatterns = [
    path('', home_newsletters.as_view(), name="home"),
    path('signup/', newsletter_signup.as_view(), name="optin"),
    path('unsubscribe/', newsletter_unsubscribe, name='unsubscribe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)