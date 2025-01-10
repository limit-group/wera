"""
URL configuration for wera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap

from common.sitemap import FormMtaaniSiteMap, StaticViewSitemap, WeraSiteMap

sitemaps = {
    "weras": WeraSiteMap,
    "form_mtaani": FormMtaaniSiteMap,
    "static": StaticViewSitemap,
}


handler404 = "wera.views.error_404"
handler500 = "wera.views.error_500"

urlpatterns = [
    path("", include("wera.urls")),
    path("", include("contact.urls")),
    path("", include("form_mtaani.urls")),
    path("", include("pwa.urls")),
    path("favicon.ico", RedirectView.as_view(url="/staticfiles/images/favicon.ico")),
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("accounts/", include("allauth.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
