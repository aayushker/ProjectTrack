from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Progress
from .serializers import ProjectSerializer, ProgressSerializer

class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class AcceptProjectView(APIView):
    def post(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.status = 'Accepted'
            project.save()
            return Response({'message': 'Project accepted'}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

class UpdateProgressView(APIView):
    def put(self, request, pk):
        try:
            progress = Progress.objects.get(project_id=pk)
            progress.completion_percentage = request.data.get('completion_percentage', progress.completion_percentage)
            progress.score = request.data.get('score', progress.score)
            progress.save()
            return Response({'message': 'Progress updated'}, status=status.HTTP_200_OK)
        except Progress.DoesNotExist:
            return Response({'error': 'Progress not found'}, status=status.HTTP_404_NOT_FOUND)