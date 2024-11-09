from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.cache import cache_control
from .models import AdminLogin,Enquiry,tblSession,tbl_course,Student
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.mail import send_mail
from . import smssender
import datetime
from django.utils import timezone

# Create your views here.
def index(req):
    return render(req,"index.html")
def org(req):
    return render(req,"org.html")
def whybiotech(req):
    return render(req,"whybiotech.html")
def location(req):
    return render(req,"location.html")
def certification(req):
    return render(req,"certification.html")
def activity(req):
    return render(req,"activity.html")
def ceo(req):
    return render(req,"ceo.html")
def mentor(req):
    return render(req,"mentor.html")
def staff(req):
    return render(req,"staff.html")
def adminis(req):
    return render(req,"adminis.html")
def services(req):
    return render(req,"services.html")
def labs(req):
    return render(req,"labs.html")
def courses(req):
    return render(req,"courses.html")
def training(req):
    return render(req,"training.html")
def skill(req):
    return render(req,"skill.html")

def admin_dash(req):
    return render(req,"admin_dash.html")


def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        gender=req.POST['gender']
        contactno=req.POST['contactno']
        emailaddress=req.POST['emailaddress']
        address=req.POST['address']
        enquirytext=req.POST['enquirytext']
        enquirydate=datetime.date.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        smssender.sendsms(contactno)
        msg="Your enquiry is submitted sucessfully" 
        return render(req,"contact.html",{'msg':msg})
    return render(req,"contact.html")
    
def login(req):
    return render(req,"login.html")
def logcode(req):
    if req.method=="POST":
        usertype=req.POST['usertype']      
        if usertype=="admin":
            userid=req.POST['userid']
            password=req.POST['password']
            try:
                user=AdminLogin.objects.get(userid=userid,password=password)
                if user is not None:
                    req.session['adminid']=userid
                    return redirect('adminlayout')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
        elif usertype=="student":
            emailaddress=req.POST['userid']
            password=req.POST['password']
            try:
                user=Student.objects.get(emailaddress=emailaddress,password=password)
                if user is not None:
                    req.session['studentid']=emailaddress
                    return redirect('studentlayout')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
            
@cache_control(no_cache=True,must_revalidate=True,no_store=True)       
def adminlayout(req):
    try:
        if req.session['adminid']!=None:
         return render(req,"adminlayout.html")
    except KeyError:
        return redirect('login')
   
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studentlayout(req):
    try:
        if req.session['studentid']!=None:
          useremail=req.session.get('studentid')
          user=Student.objects.filter(emailaddress=useremail).first()
          
          
          return render(req,'studentlayout.html')
         
        
        
    except KeyError:
        return redirect('login')

def studenthome(req):
        useremail=req.session.get('studentid')
        user=Student.objects.filter(emailaddress=useremail).first() 
        if user.fees_status=="D":
         if user: 
            ab={'sh':user}  
            return render(req,'studenthome.html',ab)
        return render(req,'studenthome.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def showenq(req):
    sh=Enquiry.objects.all()
    return render(req,"showenquiry.html",{'show':sh})
def delenq(req,id):
    en=Enquiry.objects.get(id=id)
    en.delete()
    return redirect('showenq')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addsession(req):
    return render(req,"addsession.html")
def  assave(req):
    ses=req.POST['ses']
    created_date=timezone.now()
    ads=tblSession(ses=ses,created_date=created_date)
    ads.save()
    return redirect('viewsession')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewsession(req):
    sh=tblSession.objects.all()
    return render(req,"viewsession.html",{'show':sh})
def editsession(req,id):
    edt=tblSession.objects.get(pk=id)
    if req.method=="POST":
       ses=req.POST['ses']
       created_date=timezone.now()
       tblSession.objects.filter(id=id).update(ses=ses,created_date=created_date)
       return redirect('viewsession')
    return render(req,"editsession.html",{'edt':edt})

def delview(req,id):
    vw=tblSession.objects.get(pk=id)
    vw.delete()
    return redirect('viewsession')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addcourse(req):
    ad=tblSession.objects.all()
    return render(req,"addcourse.html",{'ad':ad})
def savecourse(req):
    course_session=req.POST['course_session']
    course_name=req.POST['course_name']
    course_fees=req.POST['course_fees']
    course_duration=req.POST['course_duration']
    created_date=timezone.now()
    crs=tbl_course(course_session=course_session,course_name=course_name,course_fees=course_fees,created_date=created_date,course_duration=course_duration)
    crs.save()
    return redirect('viewcourse')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcourse(req):
    sh=tbl_course.objects.all()
    return render(req,"viewcourse.html",{'show':sh})
def editcourse(req,id):
    edt=tbl_course.objects.get(id=id)
    if req.method=="POST":
        course_session=req.POST['course_session']
        course_name=req.POST['course_name']
        course_fees=req.POST['course_fees']
        created_date=timezone.now()
        tbl_course.objects.filter(id=id).update(course_session=course_session,course_name=course_name,course_fees=course_fees,created_date=created_date)
        return redirect('viewcourse')
    return render(req,"editcourse.html",{'edt':edt})
def delcourse(req,id):
    d=tbl_course.objects.get(id=id)
    d.delete()
    return redirect('viewcourse')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addstudent(req):
    return render(req,"addstudent.html")
def savestudent(req):
    name=req.POST['name']
    emailaddress=req.POST['emailaddress']
    contactno=req.POST['contactno']
    gender=req.POST['gender']
    password="123"
    std=Student(name=name,emailaddress=emailaddress,contactno=contactno,gender=gender,password=password)
    std.save()
    subject = 'Welcome to Biotech Park Lucknow – Your Online Admission Details'
    message = f'''
     Dear {name},
     Welcome to Biotech Park Lucknow!
     We are thrilled to have you join our community. Below are your login details to access the Nou Egyan portal for your online admission process:
     Portal Link: biotechpark.org.in
     Username: {emailaddress}
     Password:{password}

     Important Instructions:

     1.Log In: Use the provided credentials to log into Biotech park.
     2.Complete Admission Form: Fill out the online admission form with accurate details.
     3.Submit Required Documents: Upload all necessary documents as specified on the portal.
     4.Check Status: Regularly check your portal for updates on your admission status.
     5.Should you encounter any issues or have any questions, please do not hesitate to reach out to our support team at [Insert Contact Information].

     We look forward to your successful admission and to welcoming you to Biotech Park Lucknow!

     Best regards,

     [Rohit Kumar]
     [CTO Softpro India]
     Biotech Park Lucknow
     [7080102008]
     [softproindia.in]


        

     Please keep this information secure and do not share it with anyone.
        '''
    from_email = 'gupta1001ayushi@gmail.com'
    recipient_list = [emailaddress]

        # Send email
    send_mail(subject, message, from_email, recipient_list)

        # Add success message and redirect
    messages.success(req, 'Registration successful! Please check your email for confirmation.')
    return redirect('addstudent')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudents(req):
    sh=Student.objects.all()
    return render(req,"viewstudents.html",{'show':sh})
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def stdprofile(req):
    # if req.session['studentid']!=None:
    #       useremail=req.session.get('studentid')
    #       user=Student.objects.filter(emailaddress=useremail).first()
    #       if user.fees_status=="P":
    #           return HttpResponse("Your fees approval is pending!")
    #       elif user.fees_status=="D":
    #           return render(req,'studentlayout.html')
    if 'studentid' in req.session:
        useremail=req.session.get('studentid')
        user=Student.objects.filter(emailaddress=useremail).first()    
        show={'sh':user}  
    return render(req,"stdprofile.html",show)
def upsave(req):
    if req.method=="POST":
        name=req.POST['name']
        contactno=req.POST['contactno']
        dob=req.POST['dob']
        fname=req.POST['fname']
        mname=req.POST['mname']
        address=req.POST['address']
        useremail=req.session.get('studentid')
        
        user=Student.objects.filter(emailaddress=useremail).update(name=name,contactno=contactno,dob=dob,fname=fname,mname=mname,address=address)
        

        # if user:
        #     user.name=req.POST['name']
        #     user.fname=req.POST['fname']
        #     user.save()
        return redirect('docverification')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def docverification(req):
    msg="Your basic informations are successfully submitted ! Now verify all documents."  
    sc=tblSession.objects.all()
    cr=tbl_course.objects.all()
    
    con={'sc':sc,'cr':cr,'msg':msg}   
    return render(req,"docverification.html",con)
def docsave(req):
    if req.method == "POST":
        course = req.POST['course']
        c = tbl_course.objects.get(course_name=course)
        coursefees = c.course_fees
        courseduraction=c.course_duration
        session = req.POST['session']
        aadharno = req.POST['aadharno']
        aadharpic = req.FILES['aadharpic']
        hs_percent = req.POST['hs_percent']
        hs_marksheet = req.FILES['hs_marksheet']
        inter_percent = req.POST['inter_percent']
        inter_marksheet = req.FILES['inter_marksheet']
        pic = req.FILES['pic']
        sign = req.FILES['sign']
        application_status = "N"
        useremail = req.session.get('studentid')

        try:
            user = Student.objects.get(emailaddress=useremail)
            user.aadharno = aadharno
            user.aadharpic = aadharpic
            user.hs_percent = hs_percent
            user.hs_marksheet = hs_marksheet
            user.inter_percent = inter_percent
            user.inter_marksheet = inter_marksheet
            user.pic = pic
            user.sign = sign
            user.application_status = application_status
            user.course = course
            user.session = session
            user.coursefees = coursefees
            user.courseduraction=courseduraction
            user.save()
        except Student.DoesNotExist:
            # Handle the case where the student does not exist
            pass

        return redirect('feespayment')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)   
def feespayment(req):
    useremail=req.session.get('studentid')
    user=Student.objects.filter(emailaddress=useremail).first()
    if user.application_status=="" and user.fees_status=="":
        return HttpResponse("Please fill the application form before paying fees")
    elif user.application_status=="N" or user.fees_status=="P":
        return HttpResponse("Your approval is  pending Please Wait for Admin verification!")
    elif user.application_status=="U" or user.fees_status=="D":
       msg="Your Registration is successfully Completed ! Now, Please pay your fees by scanning above QR code."
       return render(req,"feespayment.html",{'msg':msg,'hi':user})
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changepass(req):
    useremail=req.session.get('studentid')
    user=Student.objects.filter(emailaddress=useremail).first()
    if req.method=="POST":
        newpass=req.POST['newpass']
        confpass=req.POST['confpass']
        if user:
         if newpass==confpass:
            user.password=newpass
            user.save()
            msg="password change successfully"
            return redirect('login')
    return render(req,"changepass.html")
def approvelpedding(req,id):
   Student.objects.filter(sid=id).update(application_status="U")
   return HttpResponse("student is verified")
    
def logout(req):
    req.session.flush()
    return redirect('login')

def adminchngpass(req): 
    userid=req.session.get('adminid')
    user=AdminLogin.objects.filter(userid=userid).first()
    if req.method=="POST":
        newpass=req.POST['newpass']
        confpass=req.POST['confpass']
        if user:
         if newpass==confpass:
            user.password=newpass
            user.save()
            return redirect('login')
    return render(req,"adminchngpass.html")
def feesave(req):
    if req.method == "POST":
        fees = req.POST.get('fees')
        fees_sc = req.FILES.get('fees_sc')
        fees_status = "P"
        useremail = req.session.get('studentid')

        try:
            user = Student.objects.get(emailaddress=useremail)
            user.fees = fees
            user.fees_sc = fees_sc
            user.fees_status = fees_status
            user.save()
        except Student.DoesNotExist:
            # Handle the case where the student does not exist
            pass

        return redirect('studentlayout')
def vfees(req):
    hr=Student.objects.all()
    return render(req,'vfees.html',{'hr':hr})

def approvelfees(req,id):
    useremail = req.session.get('studentid')
    user = Student.objects.filter(emailaddress=useremail).first()
    if user:
     subject = '📢📢 Congratulations! Your Admission is Confirmed 📢📢'
     message = f'''
     Dear [{user.name}],
     *Here are the details of your admission*
      Name: [{user.name}]
      Course Enrolled: [{user.course}]
      Session: [{user.session}]
      Duration:[{user.courseduraction}]
      We look forward to welcoming you to our campus and are excited to have you join our academic community. Please make sure to keep an eye on your email for any further instructions and important updates regarding the start of your course and orientation activities.

     If you have any questions or need further assistance, feel free to contact our support team at [Support Email] or [Support Phone Number].

     Once again, congratulations and best wishes for your upcoming academic journey!

     Warm regards,

     [Rohit Kumar]
     [CTO Softro india]
     [Softpro India Computer Technology Lucknow]
     [7080102008]
     
        '''
     from_email = 'gupta1001ayushi@gmail.com'
     recipient_list = [user.emailaddress]
   
        # Send email
     send_mail(subject, message, from_email, recipient_list)

        # Add success message and redirect
    messages.success(req, 'Registration successful! Please check your email for confirmation.')
    Student.objects.filter(sid=id).update(fees_status="D")
    return HttpResponse("student is verified")

