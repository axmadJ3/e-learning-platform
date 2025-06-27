from django.db.models import Count
from rest_framework import viewsets

from courses.models import Subject, Course
from courses.api.pagination import StandartPagination
from courses.api.serializers import SubjectSerializer, CourseSerializer


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer
    pagination_class = StandartPagination


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer
    pagination_class = StandartPagination
