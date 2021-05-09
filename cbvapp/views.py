from django.shortcuts import render

# Create your views here.
from cbvapp . models import Student
from cbvapp.serializers import StudentSerializer
from rest_framework .response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins ,generics # for using generics and mixin
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination # for custome pagination for view set 


# for custimse pagination for viewset
class StudentPagnation(PageNumberPagination):
    page_size=1

#viewset ro minimize all code only for readopertaions 
class studentViewSET(viewsets.ReadOnlyModelViewSet):  # combine two classes 
    queryset=Student.objects.all()  # it tell query of data
    serializer_class=StudentSerializer # it tell whuc is serilazer class is
    #pagination_class=StudentPagnation # for custimizing pagination 
    pagination_class=LimitOffsetPagination # the global pagination will aply to it /it used for direct jump
    

"""

#viewset ro minimize all code 
class studentViewSET(viewsets.ModelViewSet):  # combine two classes 
    queryset=Student.objects.all()  # it tell query of data
    serializer_class=StudentSerializer # it tell whuc is serilazer class is
"""

"""


# generic api view


class student_list(generics.ListCreateAPIView):  # it will do get and post method by itself
    queryset=Student.objects.all()  # it tell query of data
    serializer_class=StudentSerializer # it tell whuc is serilazer class is




class Student_detail(generics.RetrieveUpdateDestroyAPIView):  # it will do put,get,desstroy method by itself
    queryset=Student.objects.all()  # it tell query of data
    serializer_class=StudentSerializer # it tell whuc is serilazer class is


"""


#mixing

"""

#useing mixing to less code
class student_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView) : #ListModelMixing is used to get list og object/post operation createMM is used

    queryset=Student.objects.all()  # it tell query of data
    serializer_class=StudentSerializer # it tell whuc is serilazer class is

    def get(self,request): # get is method from listgmodelmixing
        return self.list(request) # list is method from listmodelmixing 

    def post(self,request):  # get is method from Creategmodelmixing
        return self.create(request) # create is method from createmodelmixing 


class Student_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView) : #Rtrimm is used for single get object/ update is used for updting single object/detroy to delet opertions   
    
    queryset=Student.objects.all()  # it tell query of data
    serializer_class=StudentSerializer # it tell whuc is serilazer class is

    def get(self,request,pk):
        return self.retrieve(request,pk) # retrive  is method from retrivemodelmixing 

    def put(self,request,pk):
        return self.update(request,pk) # update  is method from Updatemodelmixing 

    def delete(self,request,pk):
        return self.destroy(request,pk)    # destroy is method from destroyemodelmixing 




"""






"""
 # non primary key request
class Student_list(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)


    def post(self,request):
        serialize=StudentSerializer(data=request.data) 
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)   
        

# primaey key request
class Student_detail(APIView):
    def get_object(self,pk):

        try:
            return Student.objects.get(pk=pk)

        except Student.DoesNotExist :   
            raise Http404

    def get(self,request,pk):
        student=self.get_object(pk)
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student=self.get_object(pk)   
        serialize=StudentSerializer(student,data=request.data) 
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)    

    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""

