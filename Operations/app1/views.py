from django.shortcuts import render

#Addition

def addition(request):


    if(request.method=="POST"):  #after form submission
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        result=int(n1)+int(n2)
        # print(result)
        context={'result':result}
        return render(request,'addition.html',context)

    if(request.method=="GET"):

        return render(request,'addition.html')


# class ClassName(View):
#     def get(self):
#          #code
#     def post(self):
#         #code
def fact(request):
    if(request.method=="POST"):
        n = int(request.POST.get('num1'))
        f=1
        for i in range(1,n+1):
            f=f*i
        context={'result':f}
        return render(request,'factorial.html',context)

    if(request.method=="GET"):
        return render(request,'factorial.html')


def bmi(request):
    if(request.method=="POST"):
        print(request.POST)
        weight=request.POST.get('w')
        height=request.POST.get('h')
        w=int(weight)
        h=int(height)/100
        bmi=w/(h**2)
        context={'result':bmi}
        return render(request,'bmi.html',context)


    return render(request,'bmi.html')