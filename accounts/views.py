from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from accounts.models import User
from accounts.models import StudentProfile
from accounts.models import TrainerProfile
from accounts.serializers import UserSerializer

from accounts.serializers import StudentProfileSerializer
from accounts.serializers import TrainerProfileSerializer

from accounts.permissions import IsStudentUser,IsTrainerUser


class AdminCreateView(APIView):

    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            instance = User.objects.create_superuser(role="admin",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data = serializer_instance.data)
        else:
            return Response(data = serializer_instance.errors)


# Student create view -------------------------------------------------------

class StudentCreateView(APIView):

    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            instance = User.objects.create_user(role="student",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data = serializer_instance.data)
        else:
            return Response(data = serializer_instance.errors)






class StudentProfileGetView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        instance = request.user.student
        serializer_instance = StudentProfileSerializer(instance)
        return Response(data=serializer_instance.data)


class StudentProfileUpdateView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def put(self,request):
        form_data = request.data
        student_profile_object = StudentProfile.objects.get(student = request.user)

        serializer_instance = StudentProfileSerializer(data=form_data,instance=student_profile_object)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data= serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)



# Trainer create view -------------------------------------------------------

class TrainerCreateView(APIView):

    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            instance = User.objects.create_user(role="trainer",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data = serializer_instance.data)
        else:
            return Response(data = serializer_instance.errors)


class TrainerProfileGetView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        instance = request.user.trainer
        serializer_instance = TrainerProfileSerializer(instance)
        return Response(data=serializer_instance.data)


class TrainerProfileUpdateView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def put(self,request):
        form_data = request.data

        trainer_profile_object = TrainerProfile.objects.get(trainer=request.user)

        serializer_instance = TrainerProfileSerializer(data=form_data,instance=trainer_profile_object)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data = serializer_instance.data)

        else:
            return Response(data=serializer_instance.data)

        