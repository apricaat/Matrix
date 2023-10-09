#BDD вычитание матриц текст описание
Feature: Matrix Subtraction
  As a user of the Matrix class
  I want to be able to subtract one matrix from another
  So that I can perform linear algebra operations

  Scenario: Subtract two matrices
    Given a matrix A with dimensions 2x2 and values [1, 2; 3, 4]
    And a matrix B with dimensions 2x2 and values [5, 6; 7, 8]
    When I subtract B from A
    Then I should get a matrix C with dimensions 2x2 and values [-4, -4; -4, -4]