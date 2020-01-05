from .models import CompanyDetail

def footer(request, *args, **kwargs):
    info = CompanyDetail.objects.last()
    context = {'info': info}
    return context