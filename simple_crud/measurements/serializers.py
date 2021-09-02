# TODO: опишите сериализаторы
from rest_framework import serializers
from simple_crud.measurements.models import Project, Measurement

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = ('id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at')

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('id', 'value', 'project', 'created_at', 'updated_at')