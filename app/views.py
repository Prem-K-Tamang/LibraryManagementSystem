from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import Book, Faculty, Semester, Student, GatePass, Issued, Returned
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {
    }
    context['books'] = Book.objects.all()
    context['students'] = Student.objects.all()
    context['faculties'] = Faculty.objects.all()
    context['semesters'] = Faculty.objects.all()
    context['issues'] = Issued.objects.all()
    context['returns'] = Returned.objects.all()

    return render(request, 'dashboard/dashboard.html', context)

@login_required
def list_book(request):
    if request.method == 'GET':
        books = Book.objects.all()
        context = {
            'books' : books
        }
        return render(request, 'book/list.html', context)

    else:
        messages.error(request, 'Error occured during fetching books!')
        return redirect('list_book')

@login_required
def create_book(request):
    if request.method == 'POST':
        form = forms.BookModelForm(request.POST or None)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'New book added!')
                return redirect('list_book')
            else:
                messages.error(request, 'Invalid book details entered!')
                return redirect('create_book')
        except:
            messages.success(request, 'Unknown error occured while adding new book!')
            return redirect(create_book)
        
    else:
        return render(request, 'book/create.html')

@login_required
def view_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book' : book
    }

    return render(request, 'book/detail.html', context)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.BookModelForm(request.POST or None, instance=book)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Book detail updated!')
                return redirect('list_book')
            else:
                messages.error(request, 'Invalid book details supplied!')
                return redirect('list_book')
        except:
            messages.error(request, 'An error occured while updating book detail!')
            return redirect('list_book')

    else:
        context = {
            'book':book
        }

        return render(request, 'book/update.html', context)

@login_required
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, 'Book deleted!')
    return redirect('list_book')

@login_required
def list_faculty(request):
    faculties = Faculty.objects.all()
    context = {
        'faculties':faculties
    }
    return render(request, 'faculty/list.html', context)

@login_required
def create_faculty(request):
    if request.method == 'POST':
        form = forms.FacultyModelForm(request.POST or None)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'New faculty added!')
                return redirect('list_faculty')
            else:
                messages.error(request, 'Invalid faculty details entered!')
                return redirect('create_faculty')
        except:
            messages.success(request, 'Unknown error occured while adding new faculty!')
            return redirect(create_faculty)
        
    else:
        return render(request, 'faculty/create.html')

@login_required
def view_faculty(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    context = {
        'faculty':faculty
    }
    return render(request, 'faculty/detail.html', context)

@login_required
def update_faculty(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.FacultyUpdateModelForm(request.POST or None, instance=faculty)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Faculty detail updated!')
                return redirect('list_faculty')
            else:
                messages.error(request, 'Invalid faculty details supplied!')
                return redirect('list_faculty')
        except:
            messages.error(request, 'An error occured while updating faculty details!')
            return redirect('list_faculty')

    else:
        form = forms.FacultyModelForm()
        context = {
            'form':form,
            'faculty':faculty
        }

        return render(request, 'faculty/update.html', context)

@login_required
def delete_faculty(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    faculty.delete()
    messages.success(request, 'Faculty deleted!')
    return redirect('list_faculty')

@login_required
def list_semester(request):
    semesters = Semester.objects.all()
    context = {
        'semesters': semesters
    }
    return render(request, 'semester/list.html', context)

@login_required
def create_semester(request):
    if request.method == 'POST':
        form = forms.SemesterModelForm(request.POST or None)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'New semester added!')
                return redirect('list_semester')
            else:
                messages.error(request,'Invalid semester details supplied!')
                return redirect('list_semester')

        except:
            messages.error(request, 'An error occured while adding semester!')
            return redirect('list_semester')
    else:
        form = forms.SemesterModelForm()
        faculties = Faculty.objects.all()
        context = {
            'form':form,
            'faculties':faculties
        }
        return render(request, 'semester/create.html', context)

@login_required
def view_semester(request, pk):
    semester = Semester.objects.get(pk=pk)
    context = {
        'semester':semester
    }
    return render(request, 'semester/detail.html', context)


@login_required
def delete_semester(request, pk):
    semester = Semester.objects.get(pk=pk)
    semester.delete()
    messages.success(request, 'Semester deleted!')
    return redirect('list_semester')


@login_required
def list_student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student/list.html', context)

@login_required
def create_student(request):
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'New student added!')
            return redirect('list_student')
        else:
            messages.error(request,'Invalid student details supplied!')
            return redirect('list_student')
    else:
        form = forms.StudentModelForm()
        students = Student.objects.all()
        context = {
            'form':form,
            'students':students
        }
        return render(request, 'student/create.html', context)

@login_required
def view_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    context = {
        'student':student
    }
    return render(request, 'student/detail.html', context)

@login_required
def update_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    if request.method == 'POST':
        form = forms.StudentUpdateModelForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated!')
            return redirect('list_student')
        else:
            messages.error(request, 'Invalid student details supplied!')
            return redirect('list_student')
        
    else:
        form = forms.StudentUpdateModelForm()
        context = {
            'form':form,
            'student':student
        }

        return render(request, 'student/update.html', context)

@login_required
def delete_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    student.delete()
    messages.success(request, 'student info deleted!')
    return redirect('list_student')


@login_required
def cards(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'resources/card/card.html', context)


@login_required
def gate_pass(request):
    gatepasses = GatePass.objects.all()
    context = {
        'passes':gatepasses
    }

    return render(request, 'resources/gate-pass/list.html', context)


@login_required
def create_gate_pass(request):
    if request.method == 'POST':
        form = forms.GatePassModelForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New gate pass created!')
            return redirect('gate_pass')
        else:
            messages.error(request, 'Invalid gate pass details!')
            return redirect('create_gate_pass')
    else:
        form = forms.GatePassModelForm()
        students = Student.objects.all()
        context = {
            'form':form,
            'students':students
        }

        return render(request, 'resources/gate-pass/create.html', context)


@login_required
def delete_gate_pass(request, pk):
    gatepass = GatePass.objects.get(pk=pk)
    gatepass.delete()
    messages.success(request, 'Gate Pass deleted')
    return redirect('gate_pass')


@login_required
def list_issued(request):
    issues = Issued.objects.all()

    context =  {
        'issues': issues
    }

    return render(request, 'issued/list.html', context)


@login_required
def due_about_to_expire(request):
    issues = Issued.objects.all()
    two_issues = []
    for issue in issues:
        day = abs((issue.due_date-issue.date_issued).days)
        if day <=2:
            two_issues.append(issue)
    
    context = {
        'issues':two_issues
    }
    return render(request, 'issued/fewer-days.html', context)

    context =  {
        'issues': issues
    }

    return render(request, 'issued/list.html', context)


@login_required
def create_issue(request):
    if request.method == 'POST':
        form = forms.IssuedModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            book = Book.objects.get(pk=request.POST.get('book'))
            book.quantity = (book.quantity - 1)
            book.save()
            messages.success(request, 'New book issued!')
            return redirect('list_issued')
        else:
            messages.error(request, 'Unable to issue!')
            return redirect('create_issued')
    else:
        form = forms.IssuedModelForm()
        students = Student.objects.all()
        books = Book.objects.all()
        context = {
            'form':form,
            'students':students,
            'books':books
        }
        return render(request, 'issued/create.html', context)


@login_required
def delete_issue(request, pk):
    issue = Issued.objects.get(pk=pk)
    issue.delete()
    messages.success(request, 'Issue record deleted!')
    return redirect('list_issued')


@login_required
def list_returned(request):
    returns = Returned.objects.all()
    rtns = []
    for rtn in returns:
        day = (abs((rtn.issue.due_date-rtn.returned_date).days)) 
        if day > 0:
            rtn.charge = day * 10
            rtn.save()
            rtns.append(rtn)
        else:
            rtn.charge = 0
            rtn.save()
            rtns.append(rtn)

    context =  {
        'returns': rtns
    }

    return render(request, 'returned/list.html', context)


@login_required
def create_return(request):
    if request.method == 'POST':
        form = forms.ReturnedModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            issue = Issued.objects.get(pk=request.POST.get('issue'))
            issue.is_returned = True
            issue.save()

            book = Book.objects.get(pk=(issue.book.id))
            book.quantity = (book.quantity + 1)
            book.save()
            messages.success(request, 'Book returned!')
            return redirect('list_returned')
        else:
            messages.error(request, 'Unable to make issue!')
            return redirect('create_return')
    else:
        form = forms.ReturnedModelForm()
        issues = Issued.objects.filter(is_returned=False)
        context = {
            'form':form,
            'issues':issues
        }
        return render(request, 'returned/create.html', context)

@login_required
def delete_return(request, pk):
    issue = Returned.objects.get(pk=pk)
    issue.delete()
    messages.success(request, 'Return record deleted!')
    return redirect('list_returned')


    