from django.conf.urls import patterns,include, url
from desktop import views
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^index/$', views.index, name='index'),
        url(r'^glossary/$', views.glossary, name='glossary'),
        url(r'^labs/$', views.labs, name='labs'),
        url(r'^admin/$', include(admin.site.urls)),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^videos/$', views.videos, name='videos'),
        url(r'^primersquizzes/$', views.primersquizzes, name='primersquizzes'),
        url(r'^checkans/$', views.checkans, name='checkans'),
        url(r'^generalquizzes/$', views.generalquizzes, name='generalquizzes'),
        url(r'^restrictionquizzes/$', views.restrictionquizzes, name='restrictionquizzes'),
        url(r'^dataquizzes/$', views.dataquizzes, name='dataquizzes'),
        url(r'^pcrlab/$', views.pcrlab, name='pcrlab'),
        url(r'^ligation/$', views.ligation, name='ligation'),
        url(r'^bwscreening/$', views.bwscreening, name='bwscreening'),
        url(r'^plasmid/$', views.plasmid, name='plasmid'),
        url(r'^dna/$', views.dna, name='dna'),
        url(r'^quantpcr/$', views.quantpcr, name='quantpcr'),
        url(r'^revision/$', views.revision, name='revision'),
        url(r'^converterconcentration/$', views.converterconcentration, name='converterconcentration'),
        url(r'^converterdilutions/$', views.converterdilutions, name='converterdilutions'),
        url(r'^convertermass/$', views.convertermass, name='convertermass'),
        url(r'^convertermolarity/$', views.convertermolarity, name='convertermolarity'),
        url(r'^convertervolume/$', views.convertervolume, name='convertervolume'),
        url(r'^mapping/(?P<question_num>\w+)/$', views.mapping, name='mapping'),
        url(r'^pcrlabpdf/$', views.pcr_pdf_view, name='pcrlabpdf'),
        url(r'^ligationlabpdf/$', views.ligation_pdf_view, name='ligationlabpdf'),
        url(r'^bwslabpdf/$', views.bws_pdf_view, name='bwslabpdf'),
        url(r'^plasmidlabpdf/$', views.plasmid_pdf_view, name='plasmidlabpdf'),
        url(r'^dnalabpdf/$', views.dna_pdf_view, name='dnalabpdf'),
        url(r'^qpcrlabpdf/$', views.qpcr_pdf_view, name='qpcrlabpdf'),
        url(r'^Electrophoresis/$', views.electro_pdf_view, name='Electrophoresis'),
        url(r'^Sequence_Analysis/$', views.sa_pdf_view, name='Sequence_Analysis'),
        url(r'^Ligation_Calculations/$', views.lc_pdf_view, name='Ligation_Calculations'),
        url(r'^QPCR_Exercises/$', views.qpcrexer_pdf_view, name='QPCR_Exercises'),
        url(r'^Primer_Design_Exercise/$', views.pdexer_pdf_view, name='Primer_Design_Exercise'),
        url(r'^Restriction_Mapping_Exercise/$', views.rmexer_pdf_view, name='Restriction_Mapping_Exercise'),
        url(r'^lab_manual_pdf/$', views.lab_manual_pdf_view, name='lab_manual_pdf'),
        # end pdfs
        url(r'^searchResult/$', views.search, name='searchResult'),
        url(r'^resetConfirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/',views.reset_confirm, name='resetConfirm'),
        url(r'^pwdReset/', views.reset, name='pwdReset'),

)


if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )