from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')      

def result(request):
    number_list = []

    for i in range(1,7):
        num = request.GET['number%d' % i]
        number_list.append(num)


    random_list = []
    arr = [i for i in range(1, 46)]
    random.shuffle(arr)
    random_list = arr[:6]
    random_list.sort()

    count = 0

    for i in range(6):
           
        for j in range(6):
            if number_list[i] == random_list[j]:

                count +=1

    return render(request, 'result.html',{'number_list':number_list,'random_list':random_list, 'count':count})