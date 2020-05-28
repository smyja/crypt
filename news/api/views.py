from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.models import Headline
from news.api.serializers import HeadlineSerializer

@api_view(['GET',])
def api_detail(request, any):
    try:
        qs = Headline.objects.get(slug=any)
    except Headline.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = HeadlineSerializer(qs)
        return Response(serializer.data)


