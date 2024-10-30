"""
URL configuration for aot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aot1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my',views.fun1),
    path('mm',views.fun2),
    path('du',views.fun3),
    path('di',views.fun4),
    path("fr",views.fun5),
    path("it",views.fun6),
    path("pt",views.task1),
    path("dt",views.fun7,name='hi'),
    path("ad",views.fun9),
    path("bkfm",views.task2a),
    path("bkdp",views.task2b),
    path("emfm",views.emp),
    path("emdp",views.emp2,name='re'),
    path("prfm",views.task3a),
    path("prdp",views.task3b,name='res'),
    path("delete_user/<int:id>",views.delete_user,name='delete'),
    path("ctfm",views.task4a),
    path("ctdp",views.task4b,name='ct'),
    path('delete_cust/<int:id>',views.delete_cust,name='delete'),
    path("blfm",views.task5a),
    path("bldp",views.task5b,name="bg"),
    path("deleteblog/<int:id>",views.delete_blog,name='delete'),
    path("updateblog/<int:id>",views.update_blog,name='update'),
    path("dpp",views.prod,name='dm'),
    path("dpf",views.prodv),
    path('t',views.employget,name='get'),
    path('epp',views.employadd),
    path('ab/<int:id>',views.delete_emp,name='dt'),
    path('bget',views.bookget,name='gt'),
    path('badd',views.bookadd),
    path('deletebook/<int:id>',views.book_del,name='delete'),
    path('updatebook/<int:id>',views.book_update,name='update'),
    path('update/<int:id>',views.update_emp,name='empup'),

    path('csget',views.courseget),
    path('stget',views.studentget,name='st'),
    path('stadd',views.studentadd),
    path("deletestudent/<int:id>",views.student_del,name='delete'),
    path('updatestudent/<int:id>',views.student_update,name='update'),
    path('courses/',views.course_list,name='course_list'),
    path('course/<int:id>/',views.course_details,name='course_details'),

    path('evget',views.eventget,name='ev'),
    path("orget",views.organizerget,name='or'),
    path("oradd",views.organizeradd),
    path("evadd",views.eventadd),
    path("deleteorganizer/<int:id>",views.organizer_del,name='delete'),
    path("deleteevent",views.event_del,name='delete'),
    path("updateorganizer/<int:id>",views.organizer_update,name='update'),
    path("updateevent/<int:id>",views.event_update,name='update'),

    path("iview",views.index_view),

    path("poget",views.post_get,name='po'),
    path("poadd",views.post_add)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,documemt_root=settings.STATIC_ROOT)