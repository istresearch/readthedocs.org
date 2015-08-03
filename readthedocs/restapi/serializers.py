from rest_framework import serializers

from readthedocs.builds.models import Build, Version
from readthedocs.projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id',
            'name', 'slug', 'description', 'language',
            'repo', 'repo_type',
            'default_version', 'default_branch',
            'documentation_type',
            'users',
        )


class ProjectFullSerializer(ProjectSerializer):
    '''Serializer for all fields on project model'''

    class Meta:
        model = Project


class VersionSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    downloads = serializers.DictField(source='get_downloads', read_only=True)

    class Meta:
        model = Version
        fields = (
            'id',
            'project', 'slug',
            'identifier', 'verbose_name',
            'active', 'built',
            'downloads',
        )


class BuildSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Build
        fields = (
            'id',
            'project',
            'commit',
            'type',
            'date',
            'success',

        )


class VersionFullSerializer(VersionSerializer):
    '''Serializer for all fields on version model'''

    project = ProjectFullSerializer()

    class Meta:
        model = Version


class SearchIndexSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=500)
    project = serializers.CharField(max_length=500, required=False)
    version = serializers.CharField(max_length=500, required=False)
    page = serializers.CharField(max_length=500, required=False)
