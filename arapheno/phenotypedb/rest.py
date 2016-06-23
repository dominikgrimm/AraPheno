from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from phenotypedb.models import Phenotype, Study
from phenotypedb.serializers import PhenotypeListSerializer, StudyListSerializer
from phenotypedb.serializers import PhenotypeDetailSerializer

'''
List all phenotypes 
'''
@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def phenotype_list(request,format=None):
    """
    List all available phenotypes
    Read-Only Response Supported
    """
    if request.method == "GET":
        phenotypes = Phenotype.objects.all()
        serializer = PhenotypeListSerializer(phenotypes,many=True)
        return Response(serializer.data)

'''
Detailed phenotype list via id
'''
@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def phenotype_detail(request,pk=None,format=None):
    """
    Details of phenotype
    Read-Only Response Supported
    """
    try:
        phenotype = Phenotype.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PhenotypeDetailSerializer(phenotype)
        return Response(serializer.data)

'''
List all studies
'''
@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def study_list(request,format=None):
    """
    List all available studies
    Read-Only Response Supported
    """
    if request.method == "GET":
        studies = Study.objects.all()
        serializer = StudyListSerializer(studies,many=True)
        return Response(serializer.data)
