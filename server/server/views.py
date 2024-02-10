from django.http import JsonResponse
from .models import Art
from .serializers import ArtSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def art_list(request, format=None):
    if request.method == 'GET':
        art = Art.objects.all()
        serializer = ArtSerializer(art, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # create art
        serializer = ArtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def art_detail(request, id, format=None):
    try:
        art = Art.objects.get(pk=id)
        print(art.image.url)
    except Art.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = ArtSerializer(art)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtSerializer(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        art.delete()
        return Response(status=204)
