from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import modelformset_factory,inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tablib import Dataset
from .resources import *
from .filters import *
from .models import *
from .forms import *

# Create your views here.
def Dashboard(request):
    return render(request,'System/Dashboard.html')

@login_required(login_url='System/loginpage')
def home(request):
    upld=Upload.objects.all()
    context={'upld':upld}
    
    return render(request,'System/home.html',context)

def upldatabase(request):
    if request.method=='POST':
        upload_resource=Upload2Resource()
        dataset=Dataset()
        new_upload=request.FILES['myfile']
        if not new_upload.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data=dataset.load(new_upload.read(),format='xlsx')
        for data in imported_data:
            print(data)
            value=Upload2(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6]
                )
            value.save()
        return redirect('createupload')
            
        print("hello4")
    return render(request,'System/upload.html')

def createupload(request):
    form=UploadForm()
    if request.method=='POST':
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={'form':form}
             
    return render(request,'System/createupload.html',context)

def update(request,pk):
    uplds=Upload.objects.get(id=pk)
    form=UploadForm(instance=uplds)

    if request.method=='POST':
        form=UploadForm(request.POST,request.FILES,instance=uplds)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}

    return render(request,'System/createupload.html',context)

def delete(request,pk):
    upds=Upload.objects.get(id=pk)

    if request.method=='POST':
        upds.delete()
        return redirect('home')

    context={'upds':upds}
    return render(request,'System/deleteupload.html',context) 


def download_excel_data(request):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'attachment; filename=mywebsitename.xlsx'
            return response
    else:
        raise Http404
def search(request):
    upld=Upload.objects.all()
    
    sya=upld.filter(div="SY_A").count()
    syb=upld.filter(div="SY_B").count()
    syc=upld.filter(div="SY_C").count()
    sys=sya+syb+syc

    tya=upld.filter(div="TY_A").count()
    tyb=upld.filter(div="TY_B").count()
    tyc=upld.filter(div="TY_C").count()
    tys=tya+tyb+tyc


    fya=upld.filter(div="BTech_A").count()
    fyb=upld.filter(div="BTech_A_B").count()
    fyc=upld.filter(div="BTech_A_C").count()
    myfilter=UploadFilter(request.GET,queryset=upld)
    fys=fya+fyb+fyc

    myfilter=UploadFilter(request.GET,queryset=upld)
    upld=myfilter.qs
    
    context={'myfilter':myfilter,'sya':sya,'syb':syb,'syc':syc,
    'tya':tya,'tyb':tyb,'tyc':tyc,'fya':fya,
    'fyb':fyb,'fyc':fyc,'sys':sys,'tys':tys,'fys':fys,'upld':upld}
    return render(request,'System/searchfile.html',context)

def registerpage(request):

    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account has created successfully for'+user)
            return redirect('loginpage_clerk')

    context={'form':form}       
    return render(request,'System/registerpage.html',context)   

def loginpage(request):
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                pass
                
    else:
        messages.info(request,"username or passsword is incorrect")
                

    return render(request,'System/loginpage.html')

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def facultyreg(request):
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        f_reg_form=FacultyForm(request.POST)
        if form.is_valid() and f_reg_form.is_valid():
            u=form.save()
            u.refresh_from_db()
            f_reg_form=FacultyForm(request.POST,instance=u.faculty)
            f_reg_form.full_clean()
            user=form.cleaned_data.get('user')
            messages.success(request,'Account has created successfully for'+user)
            return redirect('loginpage_faculty')
    else:
        form=CreateUserForm()
        f_reg_form=FacultyForm()
    context={'form':form,'f_reg_form':f_reg_form}       
    return render(request,'System/facultyreg.html',context) 

def floginpage(request):
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('faculty')
            else:
                pass
                
    else:
        messages.info(request,"username or passsword is incorrect")
                

    return render(request,'System/floginpage.html')

def facultyhome(request):
    fdata=faculty.objects.all()
    myfilter=FacultyFilter(request.GET,queryset=fdata)
    fdata=myfilter.qs
    context={'fdata':fdata,'myfilter':myfilter}
    return render(request,'System/faculty.html',context)

def fview(request,pk):
    fview=faculty.objects.get(id=pk)
    upld=Upload2.objects.all()
    at=attendance.objects.filter(asub=fview)
    print(at)
    fbatch=fview.batch
    print(fbatch)
    fdiv=fview.div
    print(fdiv)
    sdata=Upload2.objects.filter(sdiv=fdiv,batch=fbatch) or Upload2.objects.filter(batch=fbatch).values_list()
    re=attendance.objects.filter(asub=fview,Remark='A').values_list()
    ro=attendance.objects.filter(asub=fview,Remark='A').count()
    c=[]
    for i in range(ro):
        g=re[i][1]
        c.append((g))
    print(c)
    print(re)
    cnt=sdata.count()
    context={'fview':fview,'sdata':sdata ,'cnt':cnt,'re':re,'at':at}
    return render(request,'System/attendance.html',context)

def fupdateprofile(request,pk):
    uplds=faculty.objects.get(id=pk)
    form=FacultyForm(instance=uplds)

    if request.method=='POST':
        form=FacultyForm(request.POST,request.FILES,instance=uplds)
        if form.is_valid():
            form.save()
            return redirect('faculty')

    context={'form':form}
    return render(request,'System/facultyprofile.html',context)

 ## to select faculty members and other
 ## data in faculty's dashboard 
def facultyprofile(request):
    form=FacultyForm()

    if request.method=='POST':
        form=FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty')

    context={'form':form}
    return render(request,'System/facultyprofile.html',context)

def atten(request,pk):
    fview=faculty.objects.get(id=pk)
    upld=Upload2.objects.all()

    fbatch=fview.batch
    print(fbatch)
    fdiv=fview.div
    print(fdiv)
    sdata=Upload2.objects.filter(sdiv=fdiv) or Upload2.objects.filter(batch=fbatch)

    salldata=sdata.values_list('roll_no',flat=True)
    print(salldata)
    
    cnt=sdata.count()
    # print(cnt)
    
    # d=[]
    # for j in range(cnt):
    #     f=salldata[j][4]
    #     d.append(int(f))
    # print(d)

    # print(sdata)


    AttendanceFormSet=inlineformset_factory(faculty,attendance,fields=('asub','stud','Remark'),extra=cnt)
    formset=AttendanceFormSet(queryset=attendance.objects.none(),instance=fview)

    
    for form,i in zip(formset.forms,range(cnt)):
        form.initial['stud']=salldata[i]

    if request.method=='POST':
        formset=AttendanceFormSet(request.POST,instance=fview)
        if formset.is_valid():
            formset.save()
            return redirect('faculty')
            
    context={'fview':fview,'sdata':sdata ,'cnt':cnt,'formset':formset}
    return render(request,'System/formset.html',context)

def updateatten(request,pk):
    uat=attendance.objects.get(id=pk)
    form=AttendanceForm(instance=uat)

    if request.method=='POST':
        form=AttendanceForm(request.POST,instance=uat)
        if form.is_valid():
            form.save()
            return redirect('faculty')
    context={'form':form}
    return render(request,'System/updateatten.html',context)


def default(request,pk):
    fview=faculty.objects.get(id=pk)
    re=attendance.objects.filter(asub=fview,Remark='A').values_list()
    ro=attendance.objects.filter(asub=fview,Remark='A').count()
    c=[]
    # print(re)
    for i in range(ro):
        g=re[i][1]
        c.append((g))
    # print(c)
    
    import pandas as pd
    from collections import Counter

    count=pd.Series(c).value_counts()
    # print("element count")
    # print(count)

    a=dict(Counter(c))
    print(a)
    a=dict((k,v) for k,v in a.items() if v>=2)
    mylist=list(a.keys())
    cont=len(mylist)
    # print(cont)
    # print(mylist)
    
    # d=[]
    # for i in range(cont):
    #     pss=Upload2.objects.filter(id=mylist[i]).values_list()
    #     d.append(pss)
    # print(d)

    # print(re)
    context={'fview':fview,'a':a}
    return render(request,'System/defaulter.html',context)

def adminhome(request):
    hods=HOD.objects.all()
    context={'hods':hods}
    return render(request,'System/adminhome.html',context)

def viewadmin(request,pk):
    hd=HOD.objects.get(id=pk)
    print(hd.dpart)
    fault=defaulter.objects.filter(dpart=hd.dpart)
    print(fault.values_list())
    count=fault.count()
    context={'hd':hd,'fault':fault,'count':count}
    return render(request,'System/viewadmin.html',context)

def createadmin(request):
    form=HODForm()
    if request.method=='POST':
        form=HODForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
    
    context={'form':form}
             
    return render(request,'System/createadmin.html',context)

def updateadmin(request,pk):
    hod=HOD.objects.get(id=pk)
    form=HODForm(instance=hod)

    if request.method=='POST':
        form=HODForm(request.POST,instance=hod)
        if form.is_valid():
            form.save()
            return redirect('adminhome')

    context={'form':form}

    return render(request,'System/createadmin.html',context)

def deleteadmin(request,pk):
    hod=HOD.objects.get(id=pk)

    if request.method=='POST':
        hod.delete()
        return redirect('adminhome')

    context={'hod':hod}
    return render(request,'System/deleteadmin.html',context) 

def definput(request):
    form=DefaulterForm()

    if request.method=='POST':
        form=DefaulterForm(request.POST,extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            form.save()
            return redirect('faculty')
            
    
    context={'form':form}
             
    return render(request,'System/definput.html',context)

def adminreg(request):

    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account has created successfully for'+user)
            return redirect('adminlogin')

    context={'form':form}       
    return render(request,'System/adminregister.html',context)   

def adminlogin(request):
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('adminhome')
            else:
                pass
                
    else:
        messages.info(request,"username or passsword is incorrect")
                

    return render(request,'System/adminlogin.html')

def viewdefaulter(request,pk):
    df=defaulter.objects.get(id=pk)
    dfroll=df.defaulter_list.all()
    print(dfroll)
    context={'df':df,'dfroll':dfroll}
    return render(request,'System/viewdefault.html',context)
