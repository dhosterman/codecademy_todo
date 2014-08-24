from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'todo.views.home'),
    url(r'^add_task$', 'todo.views.add_task'),
    url(r'^complete_task$', 'todo.views.complete_task')
)
