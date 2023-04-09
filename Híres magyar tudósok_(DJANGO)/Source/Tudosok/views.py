from django.http import HttpResponse,HttpRequest
from django.shortcuts import render,redirect
from Quiz.models import QuesModel
score = 0
correct = 0
wrong = 0
Current_DB = QuesModel.objects.all()
def index_view(request:HttpRequest) -> HttpResponse:
    '''
    View for the index (home) page

    Returns: Httpresponse object (renders the html page)
    '''
    return render(request,'index.html')


def Quiz_view(request:HttpRequest) -> HttpResponse:
    '''
    The view for the Quiz HTML webpage

    Returns: Httpresponse object (renders the html page and binds the context dictionary to it)
    '''
    if request.method == "POST":
        print(request.POST)
        questions = QuesModel.objects.all()
    
        for q in questions:
            print(request.POST.get(q.question_title))
            print(q.ans)
            if q.ans == request.POST.get(q.question_title):
                score+=1
                correct+=1
            else:
                wrong+=1
            percent = score/(len(questions)*10)/100

        context_dict =  {
                'score':score,
                'correct':correct,
                'wrong':wrong,
                'percent':percent
            }
        print(correct)
        return render(request,'result.html',context_dict)
    else:
        

        context_dict = {
        'questions':Current_DB,
        'title':Current_DB[1].question_title,
        'option1':Current_DB[1].option1,
        }
        return render(request,'quiz.html',context_dict )
    
def Neumann_view(request):
    return render(request,"Tudos/Neumann.html")

def Puskas_view(request):
    return render(request, "Tudos/Puskas.html")

def Jedlik_view(request):
    return render(request,"Tudos/Jedlik.html")
def Rubik_view(request):
    return render(request,"Tudos/Rubik.html")



    

        