from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer, AccountSerializer
from .models import UserProfile, Account
import json
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def ApiView(request):
    json_data = request.body
    print(json_data)
    python_data = json.loads(json_data)
    print(python_data)
    id = python_data.get('id', None)
    obj = User.objects.get(id = id)
    if obj!= None:
        serializer = UserSerializer(obj)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')  
    HttpResponse('error')

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer