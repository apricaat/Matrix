from matrix import Matrix
from behave import given, when, then
#использование behave для вычитания
@given('a matrix A with dimensions {rows:d}x{cols:d} and values {values}')
def step_impl(context, rows, cols, values):
    context.matrix_a = Matrix(rows, cols, values)

@given('a matrix B with dimensions {rows:d}x{cols:d} and values {values}')
def step_impl(context, rows, cols, values):
    context.matrix_b = Matrix(rows, cols, values)

@when('I subtract B from A')
def step_impl(context):
    context.matrix_c = context.matrix_a - context.matrix_b

@then('I should get a matrix C with dimensions {rows:d}x{cols:d} and values {values}')
def step_impl(context, rows, cols, values):
    expected_matrix = Matrix(rows, cols, values)
    assert context.matrix_c == expected_matrix