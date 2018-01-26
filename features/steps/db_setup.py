from behave import when, then

from service.models import ServiceModel

@given('There is an empty ServiceRegistry')
def step_there_is_an_empty_service_registry(context):
  assert 0 == ServiceModel.objects.count()
