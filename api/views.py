from rest_framework import viewsets
from .models import Beverage
from .serializers import BeverageSerializer

class BeverageViewSet(viewsets.ModelViewSet):
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer
