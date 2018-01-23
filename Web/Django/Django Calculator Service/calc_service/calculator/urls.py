from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import user_detail, calc_home


urlpatterns = [
    # url(r'^$', auth_views.login, {'next_page': 'user_detail'}, name='login'),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'calculator:login'}, name='logout'),
    url(r'^user_detail/$', user_detail, name='user_detail'),
    url(r'^calc/$', calc_home, name='calc_home'),
]