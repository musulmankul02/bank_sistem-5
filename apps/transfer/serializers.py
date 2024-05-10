from rest_framework import serializers

from apps.transfer.models import HistoryTransfer

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ['id', 'from_user', 'to_user', 'is_completed', 'created_at', 'amount']
        # extra_kwargs = {
        #     'from_user': {'write_only': True},
        #     'to_user': {'write_only': True}
        # }
        
    def validate(self, attrs):
        if attrs['amount'] > attrs['from_user'].balance:
            raise serializers.ValidationError("Недостаточно средств!")
        
        return attrs