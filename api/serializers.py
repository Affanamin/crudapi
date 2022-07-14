from attr import fields
from .models import Task
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		# db_table = 'notesdata'
		fields ='__all__'


class GetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'
