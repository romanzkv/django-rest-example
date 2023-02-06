from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getPesons(request):
    person = dict(name="roman", age=52)
    return Response(person)






