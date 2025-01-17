try:
    from django.conf.urls.defaults import patterns, include, url
except ImportError:  # Django > 1.4
    from django.conf.urls import patterns, include, url


urlpatterns = patterns('locking.views',
    # verwijst naar een ajax-view voor het lockingmechanisme
    (r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/lock/$', 'lock'),
    (r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/unlock/$', 'unlock'),
    (r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/is_locked/$', 'is_locked'),
    (r'variables\.js$', 'js_variables', {}, 'locking_variables'),
    )

urlpatterns += patterns('',
    (r'jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': 'locking'}),
    )
