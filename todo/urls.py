from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'todo.views.home'),
    url(r'^add_task$', 'todo.views.add_task'),
    url(r'^complete_task$', 'todo.views.complete_task'),
    url(r'^uncomplete_task$', 'todo.views.uncomplete_task'),
    url(r'^delete_task$', 'todo.views.delete_task'),
    url(r'^update_task$', 'todo.views.update_task')
)
