from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='root'),
    # url(r'^method_designs/', include('method_designs.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
  )


"""
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template
from tastypie.api import Api

from apps.package.api import (PackageResource, AttributeResource, 
                              ValueResource) 

from apps.package.views import (filter_packages, values_as_json, 
                                packages_as_json, attributes_as_json,
                                attributes_for_dynatree, search, 
                                search_results, most_recent_database_mod,
                                package_keywords_as_json
                                )

admin.autodiscover()


urlpatterns = patterns('',
    url(r"^admin/", include(admin.site.urls)),
    url(r'^packages/', include('apps.package.urls')),
    url(r'^attributes/$', include('apps.package.attribute_urls')),
    url(r'^$', direct_to_template, {'template': 'pages/home.html'}, name='root'),
    url(r'^home/$', direct_to_template, {'template': 'pages/home.html'}, name='home'),
    url(r'^about/$', direct_to_template, {'template': 'pages/about.html'}, name='about'),
    url(r'^contact/$', direct_to_template, {'template': 'pages/contact.html'}, name='contact'),
    url(r'^api/v1/values/$', values_as_json, name="api_values"),
    url(r'^api/v1/packages/$', packages_as_json, name="api_packages"),
    url(r'^api/v1/package-keywords/$', package_keywords_as_json),
    url(r'^api/v1/attributes/$', attributes_for_dynatree, name="api_attributes"),
    url(r'^api/v1/most-recent-modification/$', most_recent_database_mod),
    url(r'^search/$', search, name='search'),
    url(r'^search/results/(?P<query>[\w-]+)/$', search_results, name='search_results'),
    url(r'^tests/$', direct_to_template, {'template': 'SpecRunner.html'}),
    url(r'^404error/$', direct_to_template, {'template': '404.html'}, name='404error'),
    url(r'^oldbrowser/$', direct_to_template, {'template': 'oldbrowser.html'}, name='oldbrowser'),
    url(r'^sitemap/$', direct_to_template, {'template': 'sitemap.xml'})

)

urlpatterns += staticfiles_urlpatterns()

# TASTY-PIE
package_resource = PackageResource()
attribute_resource = AttributeResource()
value_resource = ValueResource()

v1_api = Api(api_name='v1')
v1_api.register(package_resource)
v1_api.register(attribute_resource)
v1_api.register(value_resource)

urlpatterns += patterns('',
    (r'^api/', include(v1_api.urls)),
)
"""




