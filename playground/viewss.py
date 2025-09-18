from rest_framework.response import Response
from rest_framework.decorators import api_view
from .model import Student
from .serializer import StudentSerializer 

@api_view()
def datas(request):
    students = Student.objects.all()          
    student = StudentSerializer(students,many=True)
    return Response(student.data)                   

@api_view(['GET','PUT'])
def data(req,id):
    student = Student.objects.get(pk=id)
    if req.method == "GET":
        stud = StudentSerializer(student)
        return Response(stud.data)
    if req.method == "PUT":
        students = StudentSerializer(instance=student,data=req.data)
        if students.is_valid():
            students.save()
        else:
            return Response(students.errors)
        return Response(students.data)        