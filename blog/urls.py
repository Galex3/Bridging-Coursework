from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from blog.models import Post
from . import views
from .views import SearchResultsView

info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'published_date',
}

urlpatterns = [
                  path('', views.PostList.as_view(), name='home'),
                  path('search/', SearchResultsView.as_view(), name='search_results'),
                  path('<slug:slug>/', views.post_detail, name='post_detail'),
                  # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
                  path('sitemap.xml', sitemap,
                       {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
                       name='django.contrib.sitemaps.views.sitemap'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
