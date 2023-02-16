from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

    # custom user model is here: following 2 models

class Upload(models.Model):

    Batch=models.CharField(max_length=9,null=True)    
    divs=(
         ('SY_A','SY_A'),
         ('SY_B','SY_B'),
         ('SY_C','SY_C'),
         ('TY_A','TY_A'),
         ('TY_B','TY_B'),
         ('TY_C','TY_C'),
         ('BTECH_A','BTECH_A'),
         ('BTECH_B','BTECH_B'),
         ('BTECH_C','BTECH_C'),
        )
    div=models.CharField(max_length=7,null=True,choices=divs,default='SY_A')
    sheet=models.FileField(null=True,upload_to='media')

    def __str__(self):
        return str(self.div)
    
    ## for database use we have used 2nd excel sheet
    ## upload form
class Upload2(models.Model):
    batch=models.CharField(max_length=10,null=True)
    sdiv=models.CharField(max_length=10,null=True)
    cnum=models.CharField(max_length=200,null=True)
    roll_no=models.CharField(max_length=200,null=True)
    Sname=models.CharField(max_length=200,null=True)
    Ph_no=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.roll_no)

class faculty(models.Model):
    fname=models.CharField(max_length=300,null=True)
    sub=(
        ('DBMS','DBMS'),
        ('CN','CN'),
        ('SDA','SDA'),
        ('DMDW','DMDW'),
        ('DSA','DSA'),
        )
    fsub=models.CharField(max_length=200,null=True,choices=sub)
    subjtype=(
         ('theory','theory'),
         ('lab','lab'),
         ('tutorial','tutorial')
        )
    subtype=models.CharField(max_length=20,null=True,choices=subjtype,default='theory')
    batch=models.CharField(max_length=200,null=True,)
    divs=(
         ('SY_A','SY_A'),
         ('SY_B','SY_B'),
         ('SY_C','SY_C'),
         ('TY_A','TY_A'),
         ('TY_B','TY_B'),
         ('TY_C','TY_C'),
         ('BTECH_A','BTECH_A'),
         ('BTECH_B','BTECH_B'),
         ('BTECH_C','BTECH_C'),
        )
    div=models.CharField(max_length=7,null=True,choices=divs)
    dep=(
           ('Computer','Computer'),
           ('ENTC','ENTC'),
           ('INSTRU','INSTRU'),
           ('MECH','MECH'),
        )
    dpart=models.CharField(max_length=20,null=True,choices=dep,default='Computer')
    total=models.IntegerField(null=True,editable=True)
     
    def __str__(self):
        return str(self.fname)+" "+str(self.fsub)

class attendance(models.Model):
    stud=models.ForeignKey(Upload2,null=True,on_delete=models.CASCADE)
    asub=models.ForeignKey(faculty,null=True,on_delete=models.CASCADE)
    date=models.DateField(null=True,auto_now_add=True)
    remark=(
        ('P','P'),
        ('A','A')
        )
    Remark=models.CharField(max_length=1,null=True,choices=remark,default='P')

    def __str__(self):
        return str(self.stud )+ " "+str(self.asub)+" "+str(self.date)

class HOD(models.Model):
    name=models.CharField(max_length=200,null=True)
    dep=(
           ('Computer','Computer'),
           ('ENTC','ENTC'),
           ('INSTRU','INSTRU'),
           ('MECH','MECH'),
        )
    dpart=models.CharField(max_length=20,null=True,choices=dep)

    def __str__(self):
        return str(self.name)+" "+str(self.dpart)

class defaulter(models.Model):
    fname=models.ForeignKey(faculty,null=True,on_delete=models.CASCADE)
    sub=(
        ('DBMS','DBMS'),
        ('CN','CN'),
        ('SDA','SDA'),
        ('DMDW','DMDW'),
        ('DSA','DSA'),
        )
    fsub=models.CharField(max_length=200,null=True,choices=sub)
    divs=(
         ('SY_A','SY_A'),
         ('SY_B','SY_B'),
         ('SY_C','SY_C'),
         ('TY_A','TY_A'),
         ('TY_B','TY_B'),
         ('TY_C','TY_C'),
         ('BTECH_A','BTECH_A'),
         ('BTECH_B','BTECH_B'),
         ('BTECH_C','BTECH_C'),
        )
    div=models.CharField(max_length=7,null=True,choices=divs)
    dep=(
           ('Computer','Computer'),
           ('ENTC','ENTC'),
           ('INSTRU','INSTRU'),
           ('MECH','MECH'),
        )
    dpart=models.CharField(max_length=20,null=True,choices=dep,default='Computer')
    month=models.DateField(null=True)
    defaulter_list=models.ManyToManyField(Upload2)

    def __str__(self):
        return str(self.fname)+" "+str(self.div)+" "+str(self.month)