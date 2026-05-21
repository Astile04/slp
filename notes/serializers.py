from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = ['id','user','title','body','is_pinned','created_at']
