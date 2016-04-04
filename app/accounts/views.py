from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from .models import UserExtension
from serializers import UserExtSerializer
from permissiions import UserAccessPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserExtension.objects.all()
    serializer_class = UserExtSerializer
    permission_classes = [
        UserAccessPermission
    ]


class Userslist(generics.ListCreateAPIView):
    model = UserExtension
    serializer_class = UserExtSerializer
    permission_classes = [
        UserAccessPermission
    ]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users.html'

    def get(self, request, *args, **kwargs):
        queryset = UserExtension.objects.all()
        return Response({'users': queryset})


class UserDetail(APIView):
    model = UserExtension
    serializer_class = UserExtSerializer
    permission_classes = [
        UserAccessPermission
    ]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        user = get_object_or_404(UserExtension, pk=pk)
        serializer = UserExtSerializer(user)
        return Response({'serializer': serializer, 'user': user})

    def post(self, request, pk):
        user = get_object_or_404(UserExtension, pk=pk)
        serializer = UserExtSerializer(user, data=request.data)
        if serializer.is_valid():
            if 'post' in request.POST:
                serializer.save()

                return redirect('/users/')
            if 'delete'in request.POST:
                User.objects.get(pk=pk).delete()
                self.delete(request, pk)
                return redirect('/users/')

    def delete(self, request, pk, format=None):
        user = get_object_or_404(UserExtension, pk=pk)
        user.delete()
        return redirect('/users/')