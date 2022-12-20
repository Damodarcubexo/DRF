from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Account, Product, Order, Detail, HighScore
from django.db import transaction


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('id','account_number',
                  'account_type', 'open_date', 'balance', 'user')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'address', 'dob', 'mobile')

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'sku')

class DetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True,many=False)
    
    class Meta:
        model = Detail
        fields = ('id', 'product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    # here we use reverse relationship to extract the detail fields.
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Product.objects.all())
    class Meta:
        model = Order
        fields = ('id', 'order_date', 'status', 'products')
    # add transaction.atomic so that if error happened, it will rollback
    # @transaction.atomic
    # def create(self, validated_data):
    #     order = Order.objects.create(**validated_data)
    #     if "products" in self.initial_data:
    #         products = self.initial_data.get("products")
    #         for product in products:
    #             quantity = product.get("quantity")
    #             product = Product.objects.get(pk=id)
    #             Detail(order=order, product=product, quantity=quantity).save()
    #     # import pdb; pdb.set_trace()
    #     order.save()
        
    #     return order


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length = 200)
    created = serializers.DateTimeField()


class HighScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighScore
        fields = ('score', 'player_name')