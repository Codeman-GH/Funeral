from django.conf.urls import url, include
from . import views as tributeviews



urlpatterns =[


            url(r'^$', tributeviews.homepage, name='homepage'),
            url(r'^biography$', tributeviews.biography, name='biography'),            


            url(r'^tribute_list$', tributeviews.tribute_list, name='tribute_list'),
            url(r'^memory_list$', tributeviews.memory_list, name='memory_list'),
            url(r'^photo_list$', tributeviews.photo_list, name='photo_list'),

            url(r'^tribute_details/(?P<id>\d+)/$', tributeviews.tribute_details, name='tribute_details'),
            url(r'^memory_details/(?P<id>\d+)/$', tributeviews.memory_details, name='memory_details'),
            url(r'^photo_details/(?P<id>\d+)/$', tributeviews.photo_details, name='photo_details'),

           # url(r'^tribute_add/$', tributeviews.tribute_add, name='tribute_add'),
           # url(r'^memory_add/$', tributeviews.memory_add, name='memory_add'),
            #url(r'^photo_add/$', tributeviews.photo_add, name='photo_add'),

            
            


    ]





