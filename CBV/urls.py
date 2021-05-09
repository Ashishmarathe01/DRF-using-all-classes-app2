
from django.contrib import admin
from django.urls import path,include
from cbvapp import views
from rest_framework.routers import DefaultRouter # to used vieset


router=DefaultRouter() # made instance of function

router.register('students',views.studentViewSET) # register function take two parameter 1 is url name and secound is class name

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]



"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.student_list.as_view()), 
    path('student/<int:pk>',views.Student_detail.as_view()), # as_views is used becuse we are using calsss
]
"""