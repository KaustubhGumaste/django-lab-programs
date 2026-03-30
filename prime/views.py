from django.shortcuts import render

def prime_form(request):
    return render(request, 'prime/prime_form.html')

def prime_result(request):
    n = int(request.GET.get('number'))

    if n < 2:
        result = f"{n} is NOT a Prime number"
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                result = f"{n} is NOT a Prime number"
                break
        else:
            result = f"{n} is a Prime number"

    return render(request, 'prime/prime_result.html', {'result': result})