from rest_framework import serializers

from django.db.models import Count

from courses.models import Subject, Course, Module, Content


class SubjectSerializer(serializers.ModelSerializer):
    total_courses = serializers.IntegerField()
    popular_courses = serializers.SerializerMethodField()
    
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug', 'total_courses', 'popular_courses']

    def get_popular_courses(self, obj):
        courses = obj.courses.annotate(
            total_students = Count('students')
        ).order_by('total_students')[0:3]
        return [
            f'{c.title} ({c.total_students})' for c in courses
        ]


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'subject',
            'title',
            'slug',
            'overview',
            'created',
            'owner',
            'modules',
        ]


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']


class ModuleWithContentsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'contents']


class CourseWithContentsSerializer(serializers.ModelSerializer):
    module = ModuleWithContentsSerializer(many=True)    

    class Meta:
        model = Course
        fields = [
            'id',
            'subject',
            'title',
            'slug',
            'overview',
            'created',
            'owner',
            'modules'
        ]
