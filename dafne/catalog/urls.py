from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bags', views.BagListView.as_view(), name='bags'),
    re_path(r'^bag/(?P<pk>\d+)$', views.BagDetailView.as_view(), name='bag-detail'),
    path('corp', views.corp, name='corp'),
]