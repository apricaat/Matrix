from behave import given, when, then
from matrix import Matrix

#использование behave для сложения
@given("I have a matrix A with the following values:")
def step_impl(context):
    rows = len(context.table)
    cols = len(context.table[0])
    context.matrix_a = Matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            context.matrix_a[(i, j)] = int(context.table[i][j])

@given("I have a matrix B with the following values:")
def step_impl(context):
    rows = len(context.table)
    cols = len(context.table[0])
    context.matrix_b = Matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            context.matrix_b[(i, j)] = int(context.table[i][j])

@when("I add A and B together")
def step_impl(context):
    context.result = context.matrix_a + context.matrix_b

@then("the result should be a matrix with the following values:")
def step_impl(context):
    rows = len(context.table)
    cols = len(context.table[0])
    expected_result = Matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            expected_result[(i, j)] = int(context.table[i][j])
    assert context.result == expected_result

@then('an error should be raised with the message "{message}"')
def step_impl(context, message):
    try:
        context.matrix_a + context.matrix_b
    except ValueError as e:
        assert str(e) == message
    else:
        assert False, "Expected an error to be raised"