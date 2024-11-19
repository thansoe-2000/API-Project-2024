from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Member, Group
from .serializers import MemberSerializer, GroupSerializer
# Create your views here.



@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'list':'/Group-list/',
        'Create':'/Group-create/',
        'Detail':'/Group-detail/<str:pk>/',
        'Update':'/Group-update/<str:pk>/',
        'Detete':'/Group-delete/<str:pk>/',
        
        # members
        'Member':'/Member-list/', #member list
        'Create':'/Member-create/',
        'Detail':'/Member-detail/<str:pk>/',
        'Update':'/Member-update/<str:pk>/',
        'Delete':'/Member-delete/<str:pk>/',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def memberList(requset):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def memberCreate(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def memberDetail(request, pk):
    member = Member.objects.get(id=pk)
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def memberUpdate(request, pk):
    member = Member.objects.get(id=pk)
    serializer = MemberSerializer(instance=member, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def memberDelete(requset, pk):
    member = Member.objects.get(id=pk)
    member.delete()
    return Response('Member have benn deleted successfully!')

@api_view(['GET'])
def GroupList(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createGroup(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def detailGroup(request, pk):
    groups = Group.objects.get(id=pk)
    serializer = GroupSerializer(groups, many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
def updateGroup(request, pk):
    group = Group.objects.get(id=pk)
    serializer = GroupSerializer(instance=group,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return Response("Group successfully deleted!")
    