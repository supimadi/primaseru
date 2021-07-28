import requests
from django.http import JsonResponse


def fetch_school_list(request, school = 'smp', limit = 10):
    # Fetch data from URL and return the school list
    URL = 'https://referensi.data.kemdikbud.go.id/carisatpen.php'
    r = requests.get(f'{URL}?q={school}&limit={limit}')
    r = r.text

    # Removing garbage from the data
    data = r.splitlines()
    data = [x for x in data if x]
    data = [i.strip(' - ') for i in data]

    school = []
    for i in data:
        school.append(i.split("<br>")[1].lstrip(" "))

    return JsonResponse({'school': school})
