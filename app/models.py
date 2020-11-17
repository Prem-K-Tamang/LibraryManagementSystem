from django.db import models
from django.contrib.auth.models import User




class Faculty(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False, primary_key=True)
    total_student = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

class Semester(models.Model):
    number = models.IntegerField(blank=False, null=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.number)

class Book(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False)
    author = models.CharField(max_length=254, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=False)
    code = models.CharField(max_length=254, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=254, blank=False, null=False)
    address = models.CharField(max_length=254, blank=False, null=False)
    contact_no = models.CharField(max_length=20,null=False, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)



class GatePass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    reason = models.CharField(max_length=1024, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Issued(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False, null=True, blank=True)
    date_issued = models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(auto_now=False, auto_now_add=False)


    class Meta:
        ordering = ('-date_issued',)


class Returned(models.Model):
    issue = models.ForeignKey(Issued, on_delete=models.CASCADE)
    charge = models.IntegerField(default=0, null=True, blank=True)
    returned_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-returned_date',)