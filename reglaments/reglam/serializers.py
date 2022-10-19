from rest_framework import serializers
from .models import *


class Reglam_Serizalizer(serializers.ModelSerializer):
    class Meta:
        model = Reglaments
        fields = '__all__'


class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AnoTasks
        fields = "__all__"
