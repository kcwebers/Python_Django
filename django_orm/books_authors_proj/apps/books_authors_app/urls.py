from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_title$', views.add_title),
    url(r'^authors$', views.authors),
    url(r'^add_author$', views.add_author),
    url(r'^books/(?P<book_id>\d+)$', views.book_info),
    url(r'^authors/(?P<auth_id>\d+)$', views.author_info),
    url(r'^attribute_author$', views.attribute_author),
    url(r'^attribute_title$', views.attribute_title),
]