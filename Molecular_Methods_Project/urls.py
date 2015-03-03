from django.conf.urls import patterns, include, url
from yawdadmin import admin_site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#admin_site._registry.update(admin.site._registry)

#Add any extra urls to applications or maybe log-in screen
urlpatterns = patterns('',
    # Examples:

    # url(r'^$', 'Molecular_Methods_Project.views.home', name='home'),
    # url(r'^Molecular_Methods_Project/', include('Molecular_Methods_Project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^desktop/', include('desktop.urls', namespace='desktop')),
    url(r'', include('desktop.urls', namespace='desktop')),
)
