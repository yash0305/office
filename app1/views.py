from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    
    if serializer.is_valid():
        client = serializer.save(commit=False)
        client._created_by_instance = request.user  # Pass the user instance to the model
        client.save()
        return Response(ClientSerializer(client).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def client_detail(request, id):
    try:
        client = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_client(request, id):
    try:
        client = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_client(request, id):
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return Response({"status code" : "204"}, status=status.HTTP_204_NO_CONTENT)
    except Client.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_project(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    data['client'] = client.id
    data['created_by'] = request.user.id

    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_projects(request):
    projects = Project.objects.all()
    
    # Serialize the projects
    serializer = ProjectSerializer(projects, many=True)
    
    # Return the serialized data
    return Response(serializer.data)