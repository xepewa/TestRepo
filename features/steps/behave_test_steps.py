from behave import *

@given('an initial state')
def step_impl(context):
	print("whatever")
	pass

@when('something happens')
def step_impl(context):
	assert(True != False)

@then('a result is apparent')
def step_impl(context):
	assert True
