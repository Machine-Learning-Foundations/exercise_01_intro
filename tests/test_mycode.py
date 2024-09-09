"""Test the python function from src."""

import numpy as np

from fml_exercise_01_intro.my_code import Complex, my_function


def test_function() -> None:
    """See it the function really returns true."""
    assert my_function() is True


def test_complex() -> None:
    """Test if the object for a complex number instantiates."""
    complex = Complex(1.0, 2.0)
    assert np.allclose(complex.real_part, 1.0) and np.allclose(
        complex.imaginary_part, 2.0
    )


def test_add() -> None:
    """Test if adding works properly."""
    complex_1 = Complex(0.0, 1.0)
    complex_2 = Complex(1.0, 0.0)
    complex_3 = complex_1.add(complex_2)
    complex_4 = complex_3.add(complex_2)
    assert np.allclose(complex_3.real_part, 1.0) and np.allclose(
        complex_3.imaginary_part, 1.0
    )
    assert np.allclose(complex_4.real_part, 2.0) and np.allclose(
        complex_4.imaginary_part, 1.0
    )


def test_mul() -> None:
    """Test if multiplication works properly."""
    complex_1 = Complex(0.0, 1.0)
    complex_2 = Complex(1.0, 1.0)
    complex_3 = Complex(42.0, 1.0)
    result_1 = complex_1.multiply(complex_2)
    result_2 = complex_3.multiply(complex_2)
    expected_result_1 = (1.0j) * (1 + 1.0j)
    expected_result_2 = (42 + 1.0j) * (1 + 1.0j)
    assert np.allclose(result_1.real_part, expected_result_1.real) and np.allclose(
        result_1.imaginary_part, expected_result_1.imag
    )
    assert np.allclose(result_2.real_part, expected_result_2.real) and np.allclose(
        result_2.imaginary_part, expected_result_2.imag
    )
