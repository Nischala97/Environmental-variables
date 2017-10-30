from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index , name='index'),
#redirect to the same page

	url(r'redirect/(?P<lat>\d+\.\d+)/(?P<lng>\d+\.\d+)/', views.redirect, name="redirect"),

	url(r'^show_data/', views.show_data, name="show_data"),
    url(r'^insert/', views.insert.as_view(), name="insert"),
    url(r'^login/', views.login.as_view(), name="login"),
    url(r'^logout/', views.logout_user, name="logout"),
    url(r'^administrator/', views.administrator, name="administrator"),
    url(r'current_data/(?P<lat>\d+\.\d+)/(?P<lng>\d+\.\d+)/(?P<temp>\d+)/(?P<humid>\d+)/(?P<carbon>\d+)', views.current_data, name="data"),

]
