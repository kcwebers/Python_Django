from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.success_log),
    url(r'^register$', views.success_reg),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]