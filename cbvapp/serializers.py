from rest_framework import serializers
from cbvapp .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student # define which detabse wanto serlize
        fields=['id','name','score'] #ithis mention field only serlize