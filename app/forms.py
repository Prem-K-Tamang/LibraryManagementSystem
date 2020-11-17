from .models import Book, Faculty, Semester, Student, GatePass, Issued, Returned
from django import forms

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','author','quantity','code']
        

class FacultyModelForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name','total_student']


class SemesterModelForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['number','faculty']


class FacultyUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['total_student']


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name','address','contact_no','faculty','semester']

class StudentUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','address','contact_no']


class GatePassModelForm(forms.ModelForm):
    class Meta:
        model = GatePass
        fields = ['student','reason']


class IssuedModelForm(forms.ModelForm):
    class Meta:
        model  = Issued
        fields = ['student','book','due_date']

class ReturnedModelForm(forms.ModelForm):
    class Meta:
        model = Returned
        fields = ['issue',]