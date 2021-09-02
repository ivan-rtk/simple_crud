from rest_framework.viewsets import ModelViewSet

from simple_crud.measurements.models import Project, Measurement
from simple_crud.measurements.serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.select_related('project').all()
    serializer_class = MeasurementSerializer
