from django.conf.urls import patterns, url

from readthedocs.projects.views.private import AliasList, ProjectDashboard, ImportView
from readthedocs.projects.backends.views import ImportWizardView, ImportDemoView


urlpatterns = patterns(
    # base view, flake8 complains if it is on the previous line.
    '',
    url(r'^$',
        ProjectDashboard.as_view(),
        name='projects_dashboard'),

    url(r'^import/$',
        ImportView.as_view(wizard_class=ImportWizardView),
        {'wizard': ImportWizardView},
        name='projects_import'),

    url(r'^import/manual/$',
        ImportWizardView.as_view(),
        name='projects_import_manual'),

    url(r'^import/manual/demo/$',
        ImportDemoView.as_view(),
        name='projects_import_demo'),

    url(r'^import/github/$',
        'readthedocs.projects.views.private.project_import_github',
        name='projects_import_github'),

    url(r'^import/bitbucket/$',
        'readthedocs.projects.views.private.project_import_bitbucket',
        name='projects_import_bitbucket'),

    url(r'^(?P<project_slug>[-\w]+)/$',
        'readthedocs.projects.views.private.project_manage',
        name='projects_manage'),

    url(r'^(?P<project_slug>[-\w]+)/alias/(?P<id>\d+)/',
        'readthedocs.projects.views.private.edit_alias',
        name='projects_alias_edit'),

    url(r'^(?P<project_slug>[-\w]+)/alias/$',
        'readthedocs.projects.views.private.edit_alias',
        name='projects_alias_create'),

    url(r'^(?P<project_slug>[-\w]+)/alias/list/$',
        AliasList.as_view(),
        name='projects_alias_list'),

    url(r'^(?P<project_slug>[-\w]+)/comments_moderation/$',
        'readthedocs.projects.views.private.project_comments_moderation',
        name='projects_comments_moderation'),

    url(r'^(?P<project_slug>[-\w]+)/edit/$',
        'readthedocs.projects.views.private.project_edit',
        name='projects_edit'),

    url(r'^(?P<project_slug>[-\w]+)/advanced/$',
        'readthedocs.projects.views.private.project_advanced',
        name='projects_advanced'),

    url(r'^(?P<project_slug>[-\w]+)/version/(?P<version_slug>[^/]+)/delete_html/$',
        'readthedocs.projects.views.private.project_version_delete_html',
        name='project_version_delete_html'),

    url(r'^(?P<project_slug>[-\w]+)/version/(?P<version_slug>[^/]+)/$',
        'readthedocs.projects.views.private.project_version_detail',
        name='project_version_detail'),

    url(r'^(?P<project_slug>[-\w]+)/versions/$',
        'readthedocs.projects.views.private.project_versions',
        name='projects_versions'),

    url(r'^(?P<project_slug>[-\w]+)/delete/$',
        'readthedocs.projects.views.private.project_delete',
        name='projects_delete'),

    url(r'^(?P<project_slug>[-\w]+)/subprojects/delete/(?P<child_slug>[-\w]+)/$',  # noqa
        'readthedocs.projects.views.private.project_subprojects_delete',
        name='projects_subprojects_delete'),

    url(r'^(?P<project_slug>[-\w]+)/subprojects/$',
        'readthedocs.projects.views.private.project_subprojects',
        name='projects_subprojects'),

    url(r'^(?P<project_slug>[-\w]+)/users/$',
        'readthedocs.projects.views.private.project_users',
        name='projects_users'),

    url(r'^(?P<project_slug>[-\w]+)/users/delete/$',
        'readthedocs.projects.views.private.project_users_delete',
        name='projects_users_delete'),

    url(r'^(?P<project_slug>[-\w]+)/notifications/$',
        'readthedocs.projects.views.private.project_notifications',
        name='projects_notifications'),

    url(r'^(?P<project_slug>[-\w]+)/comments/$',
        'readthedocs.projects.views.private.project_comments_settings',
        name='projects_comments'),

    url(r'^(?P<project_slug>[-\w]+)/notifications/delete/$',
        'readthedocs.projects.views.private.project_notifications_delete',
        name='projects_notification_delete'),

    url(r'^(?P<project_slug>[-\w]+)/translations/$',
        'readthedocs.projects.views.private.project_translations',
        name='projects_translations'),

    url(r'^(?P<project_slug>[-\w]+)/translations/delete/(?P<child_slug>[-\w]+)/$',  # noqa
        'readthedocs.projects.views.private.project_translations_delete',
        name='projects_translations_delete'),

    url(r'^(?P<project_slug>[-\w]+)/redirects/$',
        'readthedocs.projects.views.private.project_redirects',
        name='projects_redirects'),

    url(r'^(?P<project_slug>[-\w]+)/redirects/delete/$',
        'readthedocs.projects.views.private.project_redirects_delete',
        name='projects_redirects_delete'),
)
