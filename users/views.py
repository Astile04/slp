from .serializers import UserSerializer,RegisterSerializer
from .models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer