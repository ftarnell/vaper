# vim:set sw=4 ts=4 et:
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
import vaper.views
import vaper.views.flavour
import vaper.views.api
import vaper.views.ui
import vaper.views.user
import vaper.views.manufacturer
import vaper.views.ledger
import vaper.views.admin.user

app_name = 'vaper'

vaper_urlpatterns = [
    url(r'^$',                          vaper.views.index, name='index'),

    url(r'^manufacturer/', include(vaper.views.manufacturer)),

    # Recipes
    url(r'^recipe/(?P<id>[0-9]+)/$',    vaper.views.recipe, name='recipe'),

    # Flavours
    url(r'^flavour/(?P<id>[0-9]+)/$',
        vaper.views.flavour.view,
        name='flavour/view'),

    # Ledger
    url(r'^ledger/', include(vaper.views.ledger)),

    # Admin
    url(r'^admin/user/', include(vaper.views.admin.user)),

    # UI
    url(r'^ui/flavour', include(vaper.views.ui.flavour)),
    url(r'^ui/recipe/', include(vaper.views.ui.recipe)),

    # API
    url(r'^api/flavour/', include(vaper.views.api.flavour)),
    url(r'^api/recipe/', include(vaper.views.api.recipe)),

    url(r'^api/stock/mix/$',
        vaper.views.api_stock_mix,
        name='api_stock_mix'),

    url(r'^api/manufacturer/autocomplete/$',
        vaper.views.api.manufacturer.autocomplete,
        name='api/manufacturer/autocomplete'),

    url(r'stock/$',                     vaper.views.stock, name='stock'),

    # User
    url(r'^login/$',    login, name='user/login', kwargs = {
        'template_name': 'vaper/login.html',
    }),
    url(r'^logout/$',   logout, name='user/logout', kwargs = {
        'next_page': '/',
    }),
    url(r'^user/', include(vaper.views.user)),
]

urlpatterns = [
    url(r'', include(vaper_urlpatterns, namespace='vaper')),
]
