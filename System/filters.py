import django_filters
from django_filters import DateFilter,CharFilter

from .models import*

class UploadFilter(django_filters.FilterSet):
    Batch=CharFilter(field_name='Batch',lookup_expr='icontains')
    class Meta:
        model=Upload
        fields=['Batch','div']
class FacultyFilter(django_filters.FilterSet):
    fname=CharFilter(field_name='fname',lookup_expr='icontains')
    fsub=CharFilter(field_name='fsub',lookup_expr='icontains')
    subtype=CharFilter(field_name='subtype',lookup_expr='icontains')
    # div=CharFilter(field_name='div',i)
    # total=Interg
    batch=CharFilter(field_name='Batch',lookup_expr='icontains')

    class Meta:
        Meta=faculty
        fields='__all__'

