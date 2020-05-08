"""ClowningAround URL Configuration."""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views import defaults as default_views

admin.site.site_header = "ClowningAround Admin"
admin.site.site_title = "ClowningAround Admin Portal"
admin.site.index_title = "Welcome to Clowning Around Portal"

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
