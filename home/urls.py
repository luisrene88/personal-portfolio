from django.conf.urls import url
from .views import IndexView, PortfolioView, AboutView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^portfolio/$', PortfolioView.as_view(), name='portfolio'),
    url(r'^aboutme/$', AboutView.as_view(), name='aboutme'),
    
]