from pytest_bdd import scenario, given, when, then

@scenario('bdd_test.feature', 'Test out the BDD functions')
def test_publish():
	pass

@given("an initial state")
def step_impl():
	print("whatever")
	pass

@when("something happens")
def step_impl():
	assert(True != False)

@then("a result is apparent")
def step_impl():
	assert True
