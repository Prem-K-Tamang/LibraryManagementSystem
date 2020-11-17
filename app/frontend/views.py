from django.shortcuts import render, redirect


def home(reqest):
    return render(reqest, 'frontend/index.html')