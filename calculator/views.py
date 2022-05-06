from django.http import JsonResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import numbers
# Create your views here.


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
@csrf_exempt
def calculate(request):
    data = json.loads(request.body)
    str_data = data['data']
    str_data = str_data.replace(',', ' ')
    dataset = str_data.split()
    list = []
    for i in range(len(dataset)):
        if isfloat(dataset[i]):
            t = float(dataset[i])
            list.append(t)
    percentile = float(data['percentile'])
    step_value = bool(data['checked'])
    if(len(list) < 2):
        return JsonResponse({'ans': "More than 2 elements required!"})
    arr = np.array(list)
    ans = np.percentile(arr, percentile)
    sorted(list)
    step__percentile = []
    if(step_value):
        for i in range(0, 101, 5):
            step__percentile.append(round(np.percentile(arr, i), 2))
    return JsonResponse({'ans': round(ans, 2), 'input': list, 'step_value': step__percentile})
