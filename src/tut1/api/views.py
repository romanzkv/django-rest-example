from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.models import Person
from .serializers import PersonSerializer

# these are function based views, they are working well
# bug out project uses class based views so i have to
# implement bulk insert using class based views
#
#@api_view(['GET'])
#def getPeople(request):
#    person = dict(name="roman", age=52)
#    people = Person.objects.all()
#    serializer = PersonSerializer(people, many=True)
#    return Response(serializer.data)
#
#@api_view(['POST'])
#def addPeople(request):
#    serializer = PersonSerializer(data = request.data, many=True)
#    if serializer.is_valid():
#        serializer.save()
#    return Response(serializer.data)

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # all REST operations are implemented in the base class, 
    # however they only handle single objects. To handle arrays, 
    # I have overridden the 'create' method (which handles the POST verb) 
    # to check if the data is an array. If it is, I handle it myself. 
    # If the data is not an array, I pass it to the base class for processing
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return super().create(request, *args, **kwargs)
