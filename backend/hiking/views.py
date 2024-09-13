# Django - render import:
from django.shortcuts import render
from wanderswiss.base.constants.language import LanguageChoices
from hiking.models.route_model import RouteModel
import uuid

#Test page:
def test(request):
    data = {
        'page_title': 'Hello test page',
        'output': 'Hello RKKR!'
    }
    task_id = str(uuid.uuid4())
    data['output'] = LanguageChoices.tuple_from_first_values()
    all_router = RouteModel.objects.all()
    data['output'] = all_router
    return render(request, 'hiking/test.html', data)
