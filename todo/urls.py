from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'todo.views.home'),
    url(r'^add_task$', 'todo.views.add_task'),
    url(r'^complete_task$', 'todo.views.complete_task'),
    url(r'^uncomplete_task$', 'todo.views.uncomplete_task'),
    url(r'^delete_task$', 'todo.views.delete_task'),
    url(r'^edit_task$', 'todo.views.edit_task'),
    url(r'^login$', 'todo.views.login'),
    url(r'^logout$', 'todo.views.logout'),
    url(r'^register$', 'todo.views.register')
)
