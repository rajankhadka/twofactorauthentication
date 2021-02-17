from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from api.serializers import StudentSerializer
from api.models import Student

from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.


def students(request):
    if(request.method == "GET"):
        students = Student.objects.all()
        print(students)
        studentSerializer = StudentSerializer(students, many=all)
        print(studentSerializer.data)
        json_data = JSONRenderer().render(studentSerializer.data)
        print(json_data)
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(json_data)


def student(request, student_id):
    try:
        if(request.method == "GET"):
            student = Student.objects.get(id=student_id)
            studentSerializer = StudentSerializer(student)
            json_data = JSONRenderer().render(studentSerializer.data)
            return HttpResponse(json_data, content_type='application/json')
    except Student.DoesNotExist:
        msg = {'msg': 'doesnot exists'}
        json = JSONRenderer().render(msg)
        return HttpResponse(json, content_type='application/json')


@csrf_exempt
def studentCreate(request):
    if(request.method == "POST"):
        stream = io.BytesIO(request.body)
        print(stream)
        parse_data = JSONParser().parse(stream)
        print(parse_data)
        data = StudentSerializer(data=parse_data)
        print(data)
        print(data.is_valid())
        # data.save()
        if(data.is_valid()):
            data.save()
        return HttpResponse(request.body, content_type="application/json")


@csrf_exempt
def studentupdate(request):
    if(request.method == 'PATCH'):
        stream = io.BytesIO(request.body)
        parse_data = JSONParser().parse(stream)
        print(parse_data)
        update_name = parse_data.get('name')
        print(update_name)
        update_student = Student.objects.get(name=update_name)
        print(update_student)
        update = StudentSerializer(update_student, parse_data, partial=True)

        if(update.is_valid()):
            update.save()
        # print(update.data)
        return HttpResponse(request.body, content_type="application/json")


@csrf_exempt
def delete(request):
    if request.method == 'DELETE':
        stream = io.BytesIO(request.body)
        parse_data = JSONParser().parse(stream)
        print(parse_data)
        delete_data = Student.objects.get(name=parse_data.get('name'))
        delete_data.delete()
        return HttpResponse(request.body, content_type="application/json")


