from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'content',
            'is_owner', 'profile_id', 'profile_image', 'post'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for editing a comment
    automatically references the Post Id which the comment is associated with.
    """

    post = serializers.ReadOnlyField(source='post.id')