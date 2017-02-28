from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^Reg$', Reg, name = 'Reg'),
    url(r'^SignIn$', SignIn, name = 'SignIn'),
    url(r'^clear$', clear, name = 'clear'),
    url(r'^quotes$', quotes, name = 'quotes'),
    url(r'^quote_addon$', quote_addon, name = 'quote_addon'),
    url(r'^quote_show$', quote_show, name = 'quote_show'),
    url(r'^favorites/(?P<quotes_id>\d+)$', favorites, name = 'favorites'),
    url(r'^delete/(?P<favorite_id>\d+)$', delete, name = 'delete')
]
