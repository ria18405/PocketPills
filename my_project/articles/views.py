from django.shortcuts import render
from . import helper
from .helper import *
import mysql.connector as mc
from .forms import QueryForm, QueryForm_2input
mydb = mc.connect(host="localhost",
                          user="root",
                          passwd="xxxx", auth_plugin='mysql_native_password', database="Health")
def queries(request):

    if(request.method=='POST'):

        form=QueryForm(request.POST)

        if(form.is_valid()):
            drug=form.cleaned_data['drug']

        mycursor = mydb.cursor()

        x=usquery_2(mycursor,drug)
        return render(request, "articles/queries.html", {'form': form,'x':x})


    else:
        form =QueryForm()
        return render(request,"articles/queries.html",{'form':form})


def queries_4(request):

    if(request.method=='POST'):

        form=QueryForm(request.POST)

        if(form.is_valid()):
            drug=form.cleaned_data['drug']

        mycursor = mydb.cursor()

        x=usquery_4(mycursor,drug)
        return render(request, "articles/queries_4.html", {'form': form,'x':x})


    else:
        form =QueryForm()
        return render(request,"articles/queries_4.html",{'form':form})

def queries_5(request):

    if(request.method=='POST'):

        form=QueryForm(request.POST)

        if(form.is_valid()):
            drug=form.cleaned_data['drug']

        mycursor = mydb.cursor()

        x=usquery_5(mycursor,drug)
        return render(request, "articles/queries_5.html", {'form': form,'x':x})


    else:
        form =QueryForm()
        return render(request,"articles/queries_5.html",{'form':form})


def queries_3(request):

    if(request.method=='POST'):

        form=QueryForm_2input(request.POST)

        if(form.is_valid()):
            symp=form.cleaned_data['symptoms']
            sickness=form.cleaned_data['sickness']


        mycursor = mydb.cursor()

        x=usquery_3(mycursor,symp,sickness)
        return render(request, "articles/queries_3.html", {'form': form,'x':x})


    else:
        form =QueryForm_2input()
        return render(request,"articles/queries_3.html",{'form':form})

def queries_1(request):

    if(request.method=='POST'):


        mycursor = mydb.cursor()

        x=usquery_1(mycursor,86)
        return render(request, "articles/queries_1.html", {'x':x})


    else:
        return render(request,"articles/queries_1.html")

def queries_7(request):
    if (request.method == 'POST'):

        mycursor = mydb.cursor()
        x = usquery_7(mycursor,86)
        return render(request, "articles/queries_7.html", {'x': x})


    else:
        return render(request, "articles/queries_7.html")
