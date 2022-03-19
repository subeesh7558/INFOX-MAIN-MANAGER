from django.shortcuts import render

from base_app.models import *

# Create your views here.
def MAN_index_new(request):
   
    return render(request,'MAN_index_show.html')

def MAN_profiledash_new(request):
     Num = project.objects.count()
     project_details = project.objects.all()
    
     return render(request,'MAN_dash.html',{'project':project_details,'num':Num})

def MAN_employees_new(request):
    project_details = project.objects.all()
    departments = department.objects.all()
    return render(request,'MAN_show.html',{'project':project_details,'department':departments})

def MAN_python_new(request):
    project_details = project.objects.all()
    return render(request,'MAN_projects.html',{'project':project_details})

def MAN_projects_new(request, id):
    Num = project.objects.filter(status='accepted').filter(department=id).count()
    project_details = project.objects.all()
    departments = department.objects.get(id=id)
    id=id
    # for i in project_details:
    #     if i.progress == "in progress":  
    #         Num = Num-1
    #         break
    return render(request,'MAN_projects_show.html',{'project':project_details,'num':Num, 'department':departments,'id':id})
   


def MAN_proj_cmpltd_new(request, id):
    project_details=project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'MAN_proj_cmpltd_show.html',{'project': project_details})

# def BRadmin_proj_det(request):
#     return render(request,'BRadmin_proj_det.html')

def MAN_cmpltd_proj_det_new(request, id):
    project_details = project.objects.get(id=id)

    return render(request,'MAN_cmpltd_proj_det_show.html',{'project': project_details})

def MAN_proj_mngrs_new(request, id):
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mngrs_show.html', {'project': project_details})

def MAN_proj_mangrs1_new(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mangrs1_show.html', {'project': project_details})

def MAN_proj_mangrs2_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.all()
    return render(request,'MAN_proj_mangrs2_show.html', {'project':project_details,'project_taskassign':project_task})

def MAN_developers_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.filter(tl_id = id)
    return render(request,'MAN_developers_show.html', {'project':project_details,'project_taskassign':project_task})

def MAN_daily_report_new(request, id):
    project_task = project_taskassign.objects.get(id=id)
    tester = tester_status.objects.all()
    return render(request,'MAN_daily_report_show.html', {'project':project_task,'tester_status':tester})