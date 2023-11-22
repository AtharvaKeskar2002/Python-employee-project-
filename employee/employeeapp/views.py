from django.shortcuts import render,redirect
from .models import User, employeeform , employeeevalution
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def elogin(request):
    error = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pwd']
        user = authenticate(username=email,password=password)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request,'elogin.html',locals())

def alogin(request):
    return render(request,'alogin.html')

def signin(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pwd']
        try:
            User.objects.create_user(first_name=name,username=email,password=password)
            error="no"
        except:
            error = "yes"
    return render(request,'signin.html',locals())

def employeeform1(request):
    if request.method == 'POST':
        name = request.POST['TSE_name']
        number = request.POST['case_number']
        region = request.POST['fav_language']
        c1 = employeeform.objects.create(name=name,case_number=number,region=region)
        c1.save()
        return render(request,'evalutionform.html')
    else:
        return render(request,'employeeform.html')

def evalutionform(request):
    pass

def admindashboard(request):
    form = employeeform.objects.all()
    evalution = employeeevalution.objects.all()
    # merged_table = table1.filter(name=table2.name).select_related('name')
    return render(request,'admin.html',{"employeeform":form,"employeeevalution":evalution})
# ,{'merged_table': merged_table}

def thankyou(request):
    if request.method =='POST':
        t4 = request.POST['fav_language']
        t5 = request.POST['fav_language1']
        t6 = request.POST['fav_language2']
        t7 = request.POST['fav_language3']
        t8 = request.POST['fav_language4']
        t9 = request.POST['fav_language5']
        t10 = request.POST['fav_language6']
        t11= request.POST['fav_language7']
        t12 = request.POST['fav_language8']
        t13 = request.POST['fav_language9']
        note = request.POST['whyscorelow']
        deep_drive = request.POST['yesno']
        reasondeepdrive = request.POST['reasondeepdrive']
        exemplaryperformance = request.POST['yesno1']
        reasonexemplaryperformance =request.POST['reasonexemplaryperformance']
        additionalnote = request.POST['additionalnote']
        q4 = 1 
        q5 = 1
        q6 = 0.5
        q7 = 0.5 #knowledge
        q8 = 1   #knowledge
        q9 = 1
        q10 = 0.75
        q11 = 0.75 #knowledge
        q12 = 1.75 #knowledge
        q13 = 1.75

        a4 = int(t4)
        a5 = int(t5)
        a6 = int(t6)
        a7 = int(t7)
        a8 = int(t8)
        a9 = int(t9)
        a10 = int(t10)
        a11 = int(t11)
        a12 = int(t12)
        a13 = int(t13)

        b4 = a4*q4
        b5 = a5*q5
        b6 = a6*q6
        b7 = a7*q7
        b8 = a8*q8
        b9 = a9*q9
        b10 = a10*q10
        b11 = a11*q11
        b12 = a12*q12
        b13 = a13*q13

        total = ((b4+b5+b6+b7+b8+b9+b10+b11+b12+b13)/40)*100
        coustomer_service_score = ((b4+b5+b6+b9+b10+b13)/24)*100
        knowledge_troubleshooting_score = ((b7+b8+b11+b12)/16)*100
       
        d = employeeevalution.objects.create(overall_score=total,customer_score=coustomer_service_score,knowledge_score=knowledge_troubleshooting_score,note=note,deep_flag=deep_drive,reason_deep=reasondeepdrive,exemplary_flag=exemplaryperformance,reason_exemplary=reasonexemplaryperformance,additionalnote=additionalnote)
        d.save()
        return render(request,'thankyou.html')
    else:
        return render(request,'evalutionform.html')

    