"""This module ships code to implement some complex-valued math in python."""

from __future__ import annotations

from math import atan2, cos, sin, sqrt


def my_function() -> bool:
    """Return True immediately to demonstrate a working test.

    Returns:
        : Hardcoded to True.
    """
    return True


class Complex:
    """Implement a complex number class with addition and multiplication."""

    def __init__(self, realpart: float, imagpart: float):
        """Create a complex number object.

        Args:
            realpart: The real part of the number.
            imagpart: The complex part of the number.
        """
        raise NotImplementedError  # TODO implement

    def add(self, other: Complex) -> Complex:
        """Add to complex numbers.

        For two complex numbers x_1 + iy_1, x_2 + iy_2,
        compute (x_1 + iy_1) + (x_2 + iy_2) = x_1 + x_2 + i(y_1 + y_2).

        Args:
            other: The number to add to self.

        Returns:
            : A complex number object containing the sum of the two.
        """
        raise NotImplementedError  # TODO implement

    def radius(self) -> float:
        """Compute the radius of the complex number.

        According to Pythagoras, the radius is given by sqrt(x^2 + y^2)

        Returns:
            : The radius of the complex number.
        """
        raise NotImplementedError  # TODO implement

    def angle(self) -> float:
        """Compute the angle of the complex number.

        For a complex number c = x + iy,
        the angle is typically given by atan2(y, x)

        Returns:
            : The angle of self.
        """
        raise NotImplementedError  # TODO implement

    def multiply(self, other: Complex) -> Complex:
        """Multiply two complex numbers (x_1 + jy_1) * (x_2 + jy_2).

        Complex numbers are often multiplied in polar form via

            c_mul = r_1 * r_2 * e^(theta_1 + theta_2).

        In other words, the new radius is the product of the incoming radii.
        The new angle is given by the sum of the incoming angles.

        The radius and angle can be converted back to the Cartesian form via:

            x = r_mul * cos(theta_mul),
            y = r_mul * sin(theta_mul).

        Args:
            other: The number to multiply self by.

        Returns:
            : The product of self and other.
        """
        raise NotImplementedError  # TODO implement
