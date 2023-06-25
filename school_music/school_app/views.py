from django.shortcuts import render
from school_app.models import Student


def admin_page(request):
    context = {'students': Student.objects.all()}

    return render(request, 'adminPage.html', context=context)


def student_data(request):
    context = {'students': Student.objects.all()}

    return render(request, 'studentData.html', context=context)


def adding_students(request):
    if request.method == "POST":
        student_name = request.POST.get('name')
        student_surname = request.POST.get('surname')
        student_age = request.POST.get('age')
        student_directions = request.POST.get('directions')
        student_class_number = request.POST.get('class_number')
        student_tool = request.POST.get('tool')

        Student.objects.create(surname=student_surname,
                               name=student_name,
                               age=student_age,
                               directions=student_directions,
                               class_number=student_class_number,
                               tool=student_tool)

    return render(request, 'addingStudents.html')


def student_editing(request, student):
    student = Student.objects.get(id=student)

    if request.method == "POST":
        if request.POST.get('name'):
            student.surname = request.POST.get('surname')
            student.name = request.POST.get('name')
            student.age = request.POST.get('age')
            student.directions = request.POST.get('directions')
            student.class_number = request.POST.get('class_number')
            student.tool = request.POST.get('tool')
            student.save()

    return render(request, 'studentEditing.html', context={'student': student})
