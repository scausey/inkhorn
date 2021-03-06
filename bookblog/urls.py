from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^bookreview/(?P<pk>\d+)/$', views.review_detail, name='review_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^allreviews/$', views.all_reviews, name='all_reviews'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
