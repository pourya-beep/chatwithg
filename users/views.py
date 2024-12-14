from .models import user
from .serializer import UserSerializer
from rest_framework import viewsets

#region viewsets


class UsersViewSetApiView(viewsets.ModelViewSet):
    queryset = user.objects.order_by('id').all()
    serializer_class = UserSerializer


#class InturupteduserUsersViewSetApiView(viewsets.ModelViewSet, pk):
   # queryset = u



#endregion
