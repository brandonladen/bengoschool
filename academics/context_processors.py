from .models import *
from django.utils import timezone


def site_defaults(request):
    current_session = AcademicSession.objects.filter(current=True).first()
    current_term = AcademicTerm.objects.filter(current=True).first()
    if current_session == None:
        current_session, created = AcademicSession.objects.get_or_create(
            name=str(timezone.now().year-1)+"/"+str(timezone.now().year), current=True)
        current_term, created = AcademicTerm.objects.get_or_create(
            name='Term I', current=True)
    vals = SiteConfig.objects.all()
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
