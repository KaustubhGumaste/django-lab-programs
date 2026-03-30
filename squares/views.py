from django.http import HttpResponse

def table(request, s, n):
    result = ""
    for i in range(1, n+1):
        result += f"<p>{s} * {i} = {s*i}</p>"
    return HttpResponse(result)