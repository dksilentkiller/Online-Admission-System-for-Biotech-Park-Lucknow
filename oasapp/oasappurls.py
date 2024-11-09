from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('org/',views.org,name='org'),
    path('login/',views.login,name='login'),
    path('whybiotech/',views.whybiotech,name='whybiotech'),
    path('location/',views.location,name='location'),
    path('certification/',views.certification,name='certification'),
    path('activity/',views.activity,name='activity'),
    path('ceo/',views.ceo,name='ceo'),
    path('mentor/',views.mentor,name='mentor'),
    path('satff/',views.staff,name='staff'),
    path('adminis/',views.adminis,name='adminis'),
    path('services/',views.services,name='services'),
    path('labs/',views.labs,name='labs'),
    path('courses/',views.courses,name='courses'),
    path('training/',views.training,name='training'),
    path('skill/',views.skill,name='skill'),
    path('contact/',views.contact,name='contact'),
    path('logcode/',views.logcode,name='logcode'),
    path('adminlayout/',views.adminlayout,name='adminlayout'),
    path('showenquiry/',views.showenq,name='showenq'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('addsession/',views.addsession,name='addsession'),
    path('viewsession/',views.viewsession,name='viewsession'),
    path('delview/<int:id>',views.delview,name='delview'),
    path('assave/',views.assave,name='assave'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('editsession/<id>',views.editsession,name='editsession'),
    path('savecourse/',views.savecourse,name='savecourse'),
    path('viewcourse/',views.viewcourse,name='viewcourse'),
    path('delcourse/<id>',views.delcourse,name='delcourse'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('savestudent/',views.savestudent,name='savestudent'),
    path('editcourse/<id>',views.editcourse,name='editcourse'),
    path('viewstudents/',views.viewstudents,name='viewstudents'),
    path('studentlayout',views.studenthome,name='studentlayout'),
    path('changepass/',views.changepass,name='changepass'),
    path('stdprofile',views.stdprofile,name='stdprofile'),
    path('upsave/',views.upsave,name='upsave'),
    path('docsave/',views.docsave,name='docsave'),
    path('docverification/',views.docverification,name='docverification'),
    path('feespayment/',views.feespayment,name='feespayment'),
    path('logout/',views.logout,name='logout'),
    path('approvelpedding/<id>',views.approvelpedding,name='approvelpedding'),
    path('adminchngpass',views.adminchngpass,name='adminchngpass'),
    path('feesave',views.feesave,name='feesave'),
    path('vfees',views.vfees,name='vfees'),
    path('admin_dash',views.admin_dash,name='admin_dash'),
    path('approvefees/<id>',views.approvelfees,name='approvelfees'),
    path('studenthome',views.studenthome,name='studenthome'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)