from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.decorators.csrf import csrf_exempt

from main.views import GetPost

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_states.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^first_view/$', 'main.views.first_view'),
    url(r'^city_search/(?P<city>\w+)/(?P<state>\w+)/$', 'main.views.city_search'),
    url(r'^get_view/$', 'main.views.get_view'),
    url(r'^get_city_state/$', 'main.views.get_city_state'),
    url(r'^post_city_state/$', 'main.views.post_city_state'),
    url(r'^get_post/$', csrf_exempt(GetPost.as_view())),
)
