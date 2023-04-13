
from django.http import JsonResponse


def rev_str(request):
    st=request.GET.get('stri','hello')
    st=st[::-1]
    return JsonResponse({'original string':request.GET.get('stri','hello'),'reverse string':str(st)})
