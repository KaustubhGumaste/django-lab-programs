from django.shortcuts import render

def home(request):
    result = None

    if request.method == "POST":
        n = int(request.POST.get("num"))

        if n < 2:
            result = False
        else:
            result = all(n % i != 0 for i in range(2, int(n**0.5)+1))

    return render(request,'prime.html',{'result':result})