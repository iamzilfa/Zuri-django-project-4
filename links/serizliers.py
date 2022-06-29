from rest_framework import serializers
from .models import Link

# Create a model serializer 
class LinkSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Link
        fields = "__all__"
