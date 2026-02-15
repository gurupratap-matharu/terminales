from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

from base.views import favicon, robots
from search import views as search_views


urlpatterns = [
    path("dj-admin/", admin.site.urls),
    path("private/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("favicon.ico", favicon, name="favicon"),
    path("robots.txt", robots, name="robots"),
    path("sitemap.xml", sitemap),
    path("search/", search_views.search, name="search"),
    path("servicio/", TemplateView.as_view(template_name="servicio.html")),
    path("libro/", TemplateView.as_view(template_name="libro.html")),
    path("styleguide/", TemplateView.as_view(template_name="styleguide.html")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    # Add routes to test error templates
    urlpatterns += [
        path("test404/", TemplateView.as_view(template_name="404.html")),
        path("test500/", TemplateView.as_view(template_name="500.html")),
    ]


urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
