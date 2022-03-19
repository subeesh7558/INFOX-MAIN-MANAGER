from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^$', views.index_new, name='index'),
    re_path(r'^MAN_profiledash_new$', views.MAN_profiledash_new,name='MAN_profiledash_new'),
    re_path(r'^MAN_employees_new$', views.MAN_employees_new, name='MAN_employees_new'),
    re_path(r'^MAN_python_new$', views.MAN_python_new, name='MAN_python_new'),
    re_path(r'^MAN_projects_new/(?P<id>\d+)$', views.MAN_projects_new, name='MAN_projects_new'),
    re_path(r'^MAN_proj_cmpltd_new/(?P<id>\d+)$', views.MAN_proj_cmpltd_new, name='MAN_proj_cmpltd_new'),
    # re_path(r'^BRadmin_proj_det$', views.BRadmin_proj_det, name='BRadmin_proj_det'),
    re_path(r'^MAN_cmpltd_proj_det_new/(?P<id>\d+)/$', views.MAN_cmpltd_proj_det_new, name='MAN_cmpltd_proj_det_new'),
    re_path(r'^MAN_proj_mngrs_new/(?P<id>\d+)/$', views.MAN_proj_mngrs_new, name='MAN_proj_mngrs_new'),
    re_path(r'^MAN_proj_mangrs1_new/(?P<id>\d+)/$', views.MAN_proj_mangrs1_new, name='MAN_proj_mangrs1_new'),
    re_path(r'^MAN_proj_mangrs2_new/(?P<id>\d+)/$', views.MAN_proj_mangrs2_new, name='MAN_proj_mangrs2_new'),
    re_path(r'^MAN_developers_new/(?P<id>\d+)/$', views.MAN_developers_new, name='MAN_developers_new'),
    re_path(r'^MAN_daily_report_new/(?P<id>\d+)/$', views.MAN_daily_report_new, name='MAN_daily_report_new'),


]