from http.client import HTTPResponse
import imp
from django.shortcuts import render
from .models import profile
from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa

# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        email = request.POST.get("email","")
        school = request.POST.get("school","")
        degree = request.POST.get("degree","")
        university = request.POST.get("university","")
        skill = request.POST.get("skill","")
        about_you = request.POST.get("about_you","")
        previous_work = request.POST.get("previous_work","")

        profile_info = profile(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skill=skill,about_you=about_you,previous_work=previous_work)
        profile_info.save()
    return render(request, "accept.html")


def resume(request,pk):
    user_profile = profile.objects.get(id=pk)
    return render(request,'resume.html',{"products":user_profile})

def resume_download(request,pk):
    rdownload = profile.objects.get(id=pk)
    template_path = 'temp.html'

    context = {'products': rdownload}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'attachment;filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response