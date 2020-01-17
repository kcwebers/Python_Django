from django.conf.urls import url
from . import views
        
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.success_log),
    url(r'^register$', views.success_reg),
    url(r'^wishes$', views.wishes),
    url(r'^logout$', views.logout),
    url(r'^wishes/(?P<wish_id>\d+)/remove$', views.remove),
    url(r'^wishes/new$', views.new_wish),
    url(r'^wishes/add_wish$', views.add_wish),
    url(r'^wishes/edit_wish/(?P<wish_id>\d+)$', views.edit_wish),
    url(r'^wishes/update_wish/(?P<wish_id>\d+)$', views.update_wish),
    url(r'^wishes/(?P<wish_id>\d+)/granted$', views.granted),
    url(r'^wishes/like/(?P<wish_id>\d+)$', views.like),
    url(r'^wishes/stats$', views.stats),

]