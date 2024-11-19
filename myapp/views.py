from django.shortcuts import render
from .models import Member, Group
# Create your views here.

def index(request):
    groups = Group.objects.all()
    members = Member.objects.all()
    context = {
        'members':members,
        'groups':groups,
    }
    return render(request, 'pages/index.html', context)
