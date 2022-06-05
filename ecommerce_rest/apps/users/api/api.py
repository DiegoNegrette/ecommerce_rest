from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.views import APIView


# class UserAPIView(APIView):

#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return Response(users_serializer.data, status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def user_api_view(request):

    # list
    if request.method == 'GET':
        users = User.objects.all().values(
            'id', 'username', 'email', 'password', 'name'
        )
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(
                users_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            users_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):

    # queryset
    user = User.objects.filter(id=pk).first()

    # validation
    if not user:
        return Response({
            'message': f'User with id {pk} not found'
        }, status=status.HTTP_400_BAD_REQUEST)

    # retrieve
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    # update
    elif request.method == 'PUT':
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status.HTTP_200_OK)
        return Response(
            user_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    # delete
    elif request.method == 'DELETE':
        user.delete()
        return Response({
            'message': 'User has been deleted correctly!'
        }, status=status.HTTP_200_OK)
