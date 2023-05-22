from .models import *
from authman.models import *
from django.utils import timezone


class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_session = AcademicSession.objects.get(current=True)
        current_term = AcademicTerm.objects.get(current=True)
        default_course,created=Course.objects.get_or_create(name='All')
        configdict={"school_name":"Bengo School ERP","school_slogan":"Create . Innovate . Excel","school_addres":"Excel Building, Kisumu, 1235 St.","grading_criteria":"points"}

        if current_session == None:
            current_session, created = AcademicSession.objects.get_or_create(
                name=str(timezone.now().year-1)+"/"+str(timezone.now().year), current=True)
            current_term, created = AcademicTerm.objects.get_or_create(
                name='Term I', current=True)
        configs=SiteConfig.objects.count()
        if configs ==0:
            for k,v in configdict.items():
              sc,created=SiteConfig.objects.get_or_create(key=k,value=v)
        request.current_session = current_session
        request.current_term = current_term

        response = self.get_response(request)

        return response
