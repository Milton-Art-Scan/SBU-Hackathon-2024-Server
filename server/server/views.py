from django.http import JsonResponse
from .models import Art
from .serializers import ArtSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def art_list(request, format=None):
    """
    API endpoint for retrieving a list of art or creating a new art.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The HTTP response object containing the serialized art data.

    Methods:
        GET: Retrieves a list of art objects.
        POST: Creates a new art object.

    Raises:
        N/A
    """
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
    """
    Retrieve, update or delete an art object.

    Parameters:
    - request: The HTTP request object.
    - id: The ID of the art object to retrieve, update or delete.
    - format: The format of the response data (optional).

    Returns:
    - If the request method is GET:
        - A JSON response containing the serialized art object and the URL of the art image.
    - If the request method is PUT:
        - If the serializer is valid, a response with the updated serialized art object.
        - If the serializer is invalid, a response with the serializer errors and status code 400.
    - If the request method is DELETE:
        - A response with status code 204 indicating successful deletion.
    - If the art object with the specified ID does not exist:
        - A response with status code 404 indicating not found.
    """
    try:
        art = Art.objects.get(pk=id)
    except Art.DoesNotExist:
        return Response(status=404)

    base_url = request.build_absolute_uri('/')[:-1]

    if request.method == 'GET':
        serializer = ArtSerializer(art)
        return JsonResponse({"data": serializer.data, "image": "".join((base_url, art.image.url))})
    elif request.method == 'PUT':
        serializer = ArtSerializer(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        art.delete()
        return Response(status=204)
