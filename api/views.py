from warnings import catch_warnings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import User
from .models import Task
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer,GetSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def testapi(request):
    return Response("Its Working Good", status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getNotes(request):
    userLoggedIn = request.user
    print(userLoggedIn.id)
    try:
        print("Got there")
        #resultantRecords = Task.objects.all()
        resultantRecords = Task.objects.filter(user=request.user)
        #resultantRecords = Task.objects.all.order_by('id')
        serializer = GetSerializer(resultantRecords, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Something Went Wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createNote(request):
    dataFromReq = request.data
    #dataFromReq['user'] = str(dataFromReq)
    try:
        #request.data["user"] = request.user
        userLoggedIn = request.user
        #current_user.id
        dataFromReq['user'] = userLoggedIn.id
        print("dataFromReq 002 ", dataFromReq)
        serializer = TaskSerializer(data=dataFromReq)
        print("dataFromReq 003 ", dataFromReq)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Created Successfully",safe=False,status=status.HTTP_201_CREATED )
        return Response("Error Occured")
    except:
        return Response({"message": "Something Went Wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def editNote(request,noteId):
    getRecord = Task.objects.get(id=noteId)
    dataFromReq = request.data
    try:
        serializer = TaskSerializer(instance=getRecord, data=dataFromReq)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Edited Successfully",safe=False,status=status.HTTP_201_CREATED )
            ##return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Something Went Wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteNote(request,noteId):
    getRecord = Task.objects.get(id=noteId)
    
    try:
        getRecord.delete()
        return Response("Record Deleted", status=status.HTTP_200_OK)
    except:
        return Response({"message": "Something Went Wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)