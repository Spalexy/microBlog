from django.shortcuts import render, render_to_response
from .forms import Add_User_Form
from general_function.general_function import Return_to_back

def main(request):
    return render_to_response("index.html")

