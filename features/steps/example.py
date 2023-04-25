from datetime import datetime

from behave import given, when, then

from moon_locator import MoonLocator


@given('we set last moon on South to "{date}"')
def step_impl(context, date):
    last_south = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    context.moon_locator = MoonLocator()
    context.moon_locator.default_moon = last_south

@when('we ask for the next moon on South from today')
def step_impl(context):
    context.today = datetime.now()
    context.next_moon = context.moon_locator.next_moon_on_south_from_date(context.today)

@then('the next moon on South should be in the future')
def step_impl(context):
    assert context.today <= context.next_moon
