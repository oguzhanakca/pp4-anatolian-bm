from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("home.urls"), name='home-urls'),
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls"), name='blog-urls'),
    path("booking/", include("booking.urls"), name='booking-urls'),
    path("shop/", include("shop.urls"), name='shop-urls'),
    path('summernote/', include("django_summernote.urls")),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
