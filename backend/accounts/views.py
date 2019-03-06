from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    auth = { 
        "username": request.data["username"], 
        "password": request.data["password"] 
    }

    tokens = TokenObtainPairSerializer(auth).validate(auth)

    return Response(data=tokens)
