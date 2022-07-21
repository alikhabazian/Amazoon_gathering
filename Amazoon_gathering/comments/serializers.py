from rest_framework import serializers
from .models import *

class Link_serial(serializers.ModelSerializer):
    class Meta:
        model= Link
        fields='__all__'


class Comment_serial(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields='__all__'