from django.conf.urls.defaults import patterns, url

from easy_profiles import views

urlpatterns = patterns('',

    url(regex=r'^$',
        view=views.profile_list,
        name='profile_list',
    ),

    url(
        regex = r"^edit/$",
        view = views.profile_edit,
        name="profile_edit"
    ),
    url(
        regex=r'^(?P<username>[-\w]+)/$',
        view=views.profile_detail,
        name='profile_detail',
    ),

)


