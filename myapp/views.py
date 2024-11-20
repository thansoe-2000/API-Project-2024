from django.shortcuts import render
from .models import Member, Group

# for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def index(request):
    groups = Group.objects.all()
    members = Member.objects.all()
    context = {
        'members':members,
        'groups':groups,
    }
    return render(request, 'pages/index.html', context)

def group(request):
    groups = Group.objects.all()
    context = {
        'groups':groups
    }
    return render(request, 'pages/group.html', context)

def download_group(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    groups = Group.objects.all()
    lines = []

    for group in groups:
        lines.append(group.name)
        lines.append(group.leader)
        lines.append(" ")
       
    
    for line in lines:
        textob.textLine(line)
        
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='group.pdf')

def download_member(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    members = Member.objects.all()
    lines = []

    for member in members:
        # lines.append(member.id)
        lines.append(member.name)
        # lines.append(member.languages)
        # lines.append(member.groups)
        # lines.append(member.birth_date)
        lines.append(member.bio)
        lines.append(" ")
       
    
    for line in lines:
        textob.textLine(line)
        
        
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='member.pdf')