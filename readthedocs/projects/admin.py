"""Django administration interface for `~projects.models.Project`
and related models.
"""

from readthedocs.builds.models import Version
from django.contrib import admin
from readthedocs.redirects.models import Redirect
from readthedocs.projects.models import (Project, ImportedFile, ProjectRelationship, EmailHook, WebHook)
from guardian.admin import GuardedModelAdmin


class ProjectRelationshipInline(admin.TabularInline):
    model = ProjectRelationship
    fk_name = 'parent'
    raw_id_fields = ('child',)


class VersionInline(admin.TabularInline):
    model = Version


class RedirectInline(admin.TabularInline):
    model = Redirect


class ProjectAdmin(GuardedModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'repo', 'repo_type', 'allow_comments', 'featured', 'theme')
    list_filter = ('repo_type', 'allow_comments', 'featured', 'privacy_level', 'documentation_type', 'programming_language')
    list_editable = ('featured',)
    search_fields = ('slug', 'repo')
    inlines = [ProjectRelationshipInline, RedirectInline, VersionInline]
    raw_id_fields = ('users', 'main_language_project')


class ImportedFileAdmin(admin.ModelAdmin):
    list_display = ('path', 'name', 'version')
    list_filter = ('project',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ImportedFile, ImportedFileAdmin)
admin.site.register(EmailHook)
admin.site.register(WebHook)
