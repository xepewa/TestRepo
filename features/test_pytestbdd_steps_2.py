"""BDD Test too feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('bdd_test_2.feature', 'Test out more BDD functions')
def test_test_out_more_bdd_functions():
    """Test out more BDD functions."""

@given('an initial starting point')
def an_initial_starting_point():
    """an initial starting point."""
    pass


@when('something new happens')
def something_new_happens():
    """something new happens."""
    pass


@then('a result is apparently correct')
def a_result_is_apparently_correct():
    """a result is apparently correct."""
    assert True

