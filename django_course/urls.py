"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
import debug_toolbar
from website import views
from django.http.response import HttpResponseRedirect
# from django.contrib.auth.urls
from django.urls import re_path
from django.conf import settings
from django.views.generic.base import TemplateView
sitemaps = {
    "static": StaticViewSitemap,
    'blog':BlogSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('blog/',include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('summernote/',include('django_summernote.urls')),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
    path('robots.txt',include('robots.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('captcha/', include('captcha.urls')),
    # re_path(r'^', TemplateView.as_view(template_name='../templates/website/coming_soon'), name='maintenance'),
    path("accounts/", include("django.contrib.auth.urls")),

    # re_path(r'^', views.maintenance, name='maintenance')
    # urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='../path/maintenance.html'), name='maintenance'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = 'website.views.handler404'


#-----------------------------------------------------------------------------------------
#  404 page   MAINTENANCE_MODE


# if settings.MAINTENANCE_MODE:
#     urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='../templates/website/coming_soon.html'), name='maintenance'))