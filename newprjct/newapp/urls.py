from django.contrib import admin
from django.urls import path,include
from newapp import views

urlpatterns = [
    path('',views.index,name="index"),

    path('adminhome',views.adminhome,name="adminhome"),
    path('teacherhome',views.teacherhome,name="teacherhome"),
    path('studenthome',views.studenthome,name="studenthome"),
    path('logins',views.logins,name="logins"),
    path('lgout',views.lgout,name="lgout"),

    


    path('dep_add',views.dep_add,name='dep_add'),
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path('updates',views.updates,name='updates'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('deletestud/<int:uid>',views.deletestud,name='deletestud'),
    path('updates1',views.updates1,name='updates1'),
    path('updateteacher/<int:uid>',views.updateteacher,name='updateteacher'),
    path('adtchrview',views.adtchrview,name="adtchrview"),
    path('dlttchr/<int:uid>',views.dlttchr,name='dlttchr'),
    path('depbystudent',views.depbystudent,name="depbystudent"),
    path('depbyteacher',views.depbyteacher,name="depbyteacher"),



    


    
]