from .models import *
from django.utils import timezone
from django.conf import settings

def site_defaults(request):
    current_session = AcademicSession.objects.filter(current=True).first()
    current_term = AcademicTerm.objects.filter(current=True).first()
    setup=SchoolSetup.objects.first()
    if setup !=None:
       logo=setup.logo
    else:
        logo=settings.MEDIA_URL+'school_log/default.png'

    if current_session == None:
        current_session, created = AcademicSession.objects.get_or_create(
            name=str(timezone.now().year-1)+"/"+str(timezone.now().year), current=True)
        current_term, created = AcademicTerm.objects.get_or_create(
            name='Term I', current=True)
    vals = SiteConfig.objects.all()
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
        "school_logo":logo,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
