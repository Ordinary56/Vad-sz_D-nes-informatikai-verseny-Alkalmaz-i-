from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from Quiz.models import QuesModel
Current_DB = None
correct = 0
wrong = 0
def index_view(request: HttpRequest) -> HttpResponse:
    '''
    View for the index (home) page

    Returns: Httpresponse object (renders the html page)
    '''
    return render(request, 'index.html')


def Question1_view(request: HttpRequest) -> HttpResponse:
    global Current_DB
    global correct
    global wrong
    correct = 0
    wrong = 0
    if request.method == "POST":
        if Current_DB[0].ans == request.POST.get(Current_DB[0].question_title):
            correct += 1
        else:
            wrong += 1
        return redirect("/Question2")
    else:
        value = request.GET.get('value')
        Current_DB = QuesModel.objects.filter(scientist=value)

        context_dict = {
            'Title': Current_DB[0].question_title,
            'option1': Current_DB[0].option1,
            'option2':Current_DB[0].option2,
            'option3':Current_DB[0].option3,
            'option4':Current_DB[0].option4,
            'option5':Current_DB[0].option5,
        }
        return render(request, 'Question1.html', context_dict)

def Question2_view(request: HttpRequest) -> HttpResponse:
    global Current_DB
    global correct
    global wrong
    if request.method == "POST":
        if Current_DB[1].ans == request.POST.get(Current_DB[1].question_title):
            correct += 1
        else:
            wrong += 1
        return redirect("/Question3")
    else:

        context_dict = {
            'Title': Current_DB[1].question_title,
            'option1': Current_DB[1].option1,
            'option2':Current_DB[1].option2,
            'option3':Current_DB[1].option3,
            'option4':Current_DB[1].option4,
            'option5':Current_DB[1].option5,
        }
        return render(request, 'Question2.html', context_dict)
    
def Question3_view(request: HttpRequest) -> HttpResponse:
    global Current_DB
    global correct
    global wrong
    if request.method == "POST":
        if Current_DB[2].ans == request.POST.get(Current_DB[2].question_title):
            correct += 1
        else:
            wrong += 1
        return redirect("/Question4")
    else:

        context_dict = {
            'Title': Current_DB[2].question_title,
            'option1': Current_DB[2].option1,
            'option2':Current_DB[2].option2,
            'option3':Current_DB[2].option3,
            'option4':Current_DB[2].option4,
            'option5':Current_DB[2].option5,
        }
        return render(request, 'Question3.html', context_dict)
    
def Question4_view(request: HttpRequest) -> HttpResponse:
    global Current_DB
    global correct
    global wrong
    if request.method == "POST":
        if Current_DB[3].ans == request.POST.get(Current_DB[3].question_title):
            correct += 1
        else:
            wrong += 1
        return redirect("/Question5")
    else:
       
        context_dict = {
            'Title': Current_DB[3].question_title,
            'option1': Current_DB[3].option1,
            'option2':Current_DB[3].option2,
            'option3':Current_DB[3].option3,
            'option4':Current_DB[3].option4,
            'option5':Current_DB[3].option5,
        }
        return render(request, 'Question4.html', context_dict)

def Question5_view(request: HttpRequest) -> HttpResponse:
    global Current_DB
    global correct
    global wrong
    if request.method == "POST":
        if Current_DB[4].ans == request.POST.get(Current_DB[4].question_title):
            correct += 1
        else:
            wrong += 1
        return redirect("/Result")
    else:
     
        context_dict = {
            'Title': Current_DB[4].question_title,
            'option1': Current_DB[4].option1,
            'option2':Current_DB[4].option2,
            'option3':Current_DB[4].option3,
            'option4':Current_DB[4].option4,
            'option5':Current_DB[4].option5,
        }
        return render(request, 'Question5.html', context_dict)


def Result_view(request:HttpRequest) -> HttpResponse:
    global correct
    global wrong
    percent = (correct/5)*100
    context_dict= {
        'correct':correct,
        'wrong': wrong,
        'percent': percent
    }
    return render(request,"result.html",context_dict)



def Neumann_view(request: HttpRequest) -> HttpResponse:
    return render(request, "Tudos/Neumann.html")


def Puskas_view(request: HttpRequest) -> HttpResponse:
    return render(request, "Tudos/Puskas.html")


def Jedlik_view(request: HttpRequest) -> HttpResponse:
    return render(request, "Tudos/Jedlik.html")


def Rubik_view(request: HttpRequest) -> HttpResponse:
    return render(request, "Tudos/Rubik.html")
