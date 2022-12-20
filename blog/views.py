from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer, AccountSerializer, OrderSerializer, HighScoreSerializer, ProductSerializer
from .models import UserProfile, Account, Order, HighScore, Product
import json
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


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

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.views import APIView

# class ListUsers(APIView):
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.player_name for user in HighScore.objects.all()]
#         return Response(usernames)
from django.http import Http404

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return HighScore.objects.get(pk=pk)
        except HighScore.DoesNotExist:
            raise Http404

    def get(self, request, pk = None, format=None):
        if pk:
           data = self.get_object(pk)
           serializer = HighScoreSerializer(data)
        else: 
           data = HighScore.objects.all()
           serializer = HighScoreSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = HighScoreSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Todo in the DB
        serializer.save()

        # Return Response to User

        response = Response()

        response.data = {
            'message': 'Score Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HighScoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.generics import CreateAPIView
class CreateItem(CreateAPIView):
   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer