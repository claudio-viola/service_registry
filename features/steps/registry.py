from behave import when, then
import json


@when('I add a service "{service}" with version "{version}"')
def add_service(context, service, version):
    service_to_add = {
        "service": service,
        "version": version
    }
    context.response = context.test.client.post('/services',
                                json.dumps(service_to_add),
                                content_type="application/json")

@then('I should be notified with a change "{change}"')
def i_should_be_notified(context, change):
    payload = json.loads(context.response.content)
    assert payload['status'] == 'created'


@when('I search for a service "{service}" with version "{version}"')
def search_service(context, service, version):
    service_to_search = {
        "service": service,
        "version": version
    }
    context.response = context.test.client.get('/services',service_to_search)


@then('I should find count "{count}" instances of service"')
def i_should_find(context, count):
    payload = json.loads(context.response.content)
    assert payload['count'] == count
