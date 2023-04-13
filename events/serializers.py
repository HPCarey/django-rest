from rest_framework import serializers
from events.models import Event


"""
Serializer for Events model
"""


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    """
    Raises error if image file size, width or height is too high
    """

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Lists all the filds to be included in
        the data returned by this api
        """
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'event_title',
            'event_description', 'image', 'is_owner', 'profile_id',
            'profile_image', 'image_filter', 'date', 'time', 'country',
            'location', 'email', 'phone', 'difficulty', 'rating'
        ]
