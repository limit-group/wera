from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from form_mtaani.models import FormMtaani
from wera.models import Wera


class WeraSiteMap(Sitemap):
    def items(self):
        return Wera.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class FormMtaaniSiteMap(Sitemap):
    def items(self):
        return FormMtaani.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["advertising", "report_a_problem", "privacy_policy", "terms_of_service"]

    def location(self, item):
        return reverse(item)
