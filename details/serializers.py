from rest_framework import serializers
from details.models import Details


class DetailsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Details
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'price', 'title',
            'location', 'location_filter'
        ]
