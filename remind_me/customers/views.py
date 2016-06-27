from django.contrib.auth.models import User

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from generic.utils import get_data_from_request
from customers.serializers import SignupSerializer, LoginSerializer


@api_view(['POST'])
@authentication_classes(())
@permission_classes((AllowAny,))
def signup(request):
    if request.method == "POST":
        data = get_data_from_request(request)
        serializer = SignupSerializer(data=data)
        if serializer.is_valid():
            data = serializer.data
            print(data)
            user = User.objects.create_user(username=data["email"],
                                            email=data["email"],
                                            password=data["password"])
            user.is_active = True
            user.save()
            return Response(data={"token": user.auth_token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)