from django.utils.deprecation import MiddlewareMixin
from .models import Services, Departments, Special
from specialist.models import Specialist




class GetServices(MiddlewareMixin):
    def process_request(self, request):

        services_list= Services.objects.all()
       
        request.services_list = services_list
        
        print(request.services_list)
        return None


class GetDepartments(MiddlewareMixin):
    def process_request(self, request):

        departments_list= Departments.objects.all()
       
        request.departments_list = departments_list
        
        print(request.departments_list)
        return None

class GetSpecial(MiddlewareMixin):
    def process_request(self, request):

        special_list= Special.objects.all()
       
        request.special_list = special_list
        
        print(request.special_list)
        return None

class GetSpecialist(MiddlewareMixin):
    def process_request(self, request):

        specialist_list= Specialist.objects.all()
       
        request.specialist_list = specialist_list
        
        print(request.specialist_list)
        return None