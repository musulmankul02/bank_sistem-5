from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.serializers import UserSerializer
from apps.users.models import User

class UserAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = (IsAuthenticated, )
    
    # def get_permissions(self):
    #     if self.action == 'retrive':
    #         return (IsAuthenticated(),)
    #     if self.action in ('update','partial_update', 'destroy'):
    #         return (UserPermissions(), )
    #     return (AllowAny(),)
    
    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)