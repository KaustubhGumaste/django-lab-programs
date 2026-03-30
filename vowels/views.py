from django.http import HttpResponse

def vowels(request, text):
    v = "aeiouAEIOU"

    vowel_list = [c for c in text if c in v]
    consonant_list = [c for c in text if c.isalpha() and c not in v]

    return HttpResponse(
        f"Input string: {text} <br>"
        f"Vowels: {vowel_list} <br>"
        f"Consonants: {consonant_list} <br>"
        f"Number of vowels: {len(vowel_list)} <br>"
        f"Number of consonants: {len(consonant_list)}"
    )