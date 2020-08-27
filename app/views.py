from django.shortcuts import render
from django.http import JsonResponse
from .system_info import SystemInfo

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def system_info(request):
    system_info = SystemInfo()
    system_data = {
        'cpu': {
            'percent': system_info.get_cpu_percent(),
        },
        'ram': system_info.get_ram_stats()._asdict(),
        'disk': system_info.get_disk_stats()._asdict(),
    }
    return JsonResponse(system_data)
