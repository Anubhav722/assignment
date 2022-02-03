
from deals.models import Deal
from rest_framework import serializers


class DealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deal
        fields = '__all__'


class ClaimDealSerializer(serializers.Serializer):

    id = serializers.IntegerField(label='ID', read_only=True)
    user_id = serializers.IntegerField(label='ID', read_only=True)
