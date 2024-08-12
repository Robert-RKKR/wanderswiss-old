# Django - render import:
from django.shortcuts import render
from wanderswiss.base.constants.language import LanguageChoices
import uuid

#Test page:
def test(request):
    data = {
        'page_title': 'Hello test page',
        'output': 'Hello RKKR!'
    }
    task_id = str(uuid.uuid4())
    data['output'] = LanguageChoices.standard_value()
    return render(request, 'hiking/test.html', data)
