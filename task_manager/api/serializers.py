from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TaskSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(read_only=True)
    assignee_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assignee', write_only=True, required=True, allow_null=True
    )
    created_at = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id', 'project', 'title', 'description', 'due_date', 'status', 'assignee', 'assignee_id', 'created_by', 'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at', 'created_by')

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
        return super().create(validated_data)
    
class ProjectListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'owner', 'created_at', 'updated_at')

class ProjectDetailSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        fields = ProjectListSerializer.Meta.fields + ('tasks',)