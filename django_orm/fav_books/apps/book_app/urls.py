from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.success_log),
    url(r'^register$', views.success_reg),
    url(r'^books$', views.books),
    url(r'^logout$', views.logout),
    url(r'^add_book$', views.add_book),
    url(r'^update_book$', views.update_book),
    url(r'^books/(?P<book_id>\d+)$', views.show),
    url(r'^books/(?P<book_id>\d+)/delete$', views.delete),
    url(r'^books/(?P<book_id>\d+)/favorite$', views.favorite),
    url(r'^books/(?P<book_id>\d+)/un_favorite$', views.delete),
]