from django.http import HttpResponse

def vc(request, sentence):
    vowels = "aeiouAEIOU"

    v = []
    c = []

    for ch in sentence:
        if ch.isalpha():
            if ch in vowels:
                v.append(ch)
            else:
                c.append(ch)

    return HttpResponse(
        f"Vowels: {len(v)} {v}<br>"
        f"Consonants: {len(c)} {c}"
    )