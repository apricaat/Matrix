#BDD сложение матриц текстовое описание
Feature: Matrix addition
  In order to perform arithmetic operations on matrices
  As a user of the Matrix class
  I want to be able to add two matrices together

  Scenario: Adding two matrices of the same size
    Given I have a matrix A with the following values:
      | 1 | 2 |
      | 3 | 4 |
    And I have a matrix B with the following values:
      | 5 | 6 |
      | 7 | 8 |
    When I add A and B together
    Then the result should be a matrix with the following values:
      | 6 | 8 |
      | 10 | 12 |

  Scenario: Adding two matrices of different sizes
    Given I have a matrix A with the following values:
      | 1 | 2 |
      | 3 | 4 |
    And I have a matrix B with the following values:
      | 5 | 6 | 7 |
      | 8 | 9 | 10 |
    When I try to add A and B together
    Then an error should be raised with the message "Matrices must have the same dimensions to add them."