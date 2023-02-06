from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.models import Person
from .serializers import PersonSerializer

@api_view(['GET'])
def getPeople(request):
    person = dict(name="roman", age=52)
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPeople(request):
    serializer = PersonSerializer(data = request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



