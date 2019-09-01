import numpy as np
from collections.abc import Iterable
from numbers import Number


class Vector(object):
    def __init__(self, numbers_list=None):
        """

        Args:
            numbers_list (Iterable[Number]):
        """
        self._numpy_array = None
        if numbers_list is not None:
            self._numpy_array = np.asarray(numbers_list)

    # --------------------------- Class Methods -----------------------------------
    @classmethod
    def from_numpy_array(cls, numpy_array):
        """

        Args:
            numpy_array (np.ndarray):

        Returns:
            Vector:
        """
        new_vector = cls()
        new_vector.numpy_array = numpy_array

        return new_vector

    @classmethod
    def distance(cls, vector_1, vector_2):
        """
        get the euclidean distance between two vectors

        Args:
            vector_1 (Vector):
            vector_2 (Vector:

        Returns:
            float:
        """
        dist = np.linalg.norm(vector_1.numpy_array - vector_2.numpy_array)
        return dist

    # --------------------------- Properties -----------------------------------
    @property
    def numpy_array(self):
        """

        Returns:
            np.ndarray:
        """
        return self._numpy_array

    @numpy_array.setter
    def numpy_array(self, array_in):
        """

        Args:
            array_in (np.ndarray):

        """
        self._numpy_array = array_in

    @property
    def x(self):
        """

        Returns:
            Number:
        """

        return tuple(self._numpy_array)[0]

    @x.setter
    def x(self, value):
        """

        Args:
            value (Number):

        Returns:

        """
        self._numpy_array[0] = value

    @property
    def y(self):
        """

        Returns:
            Number:
        """
        return tuple(self._numpy_array)[1]

    @y.setter
    def y(self, value):
        """

        Args:
            value (Number):

        Returns:

        """
        self._numpy_array[1] = value

    @property
    def z(self):
        """

        Returns:
            Number:
        """
        return tuple(self._numpy_array)[2]

    @z.setter
    def z(self, value):
        """

        Args:
            value (Number):

        Returns:

        """
        self._numpy_array[2] = value

    # --------------------------- Methods -----------------------------------
    def copy(self):
        """
        copy the current vector

        Returns:
            Vector:
        """
        the_copy = np.copy(self.numpy_array)
        new_vector = Vector.from_numpy_array(the_copy)
        return new_vector

    def asList(self):
        """

        Returns:
            list(Number):
        """
        return list(self.numpy_array)

    # --------------------------- Overrides -----------------------------------
    def __add__(self, other):
        """

        Args:
            other (Vector):

        Returns:
            Vector:
        """
        new_array = self.numpy_array + other.numpy_array
        new_vector = Vector.from_numpy_array(new_array)
        return new_vector

    def __iadd__(self, other):
        """

        Args:
            other (Vector):

        Returns:
            Vector:
        """
        new_array = self.numpy_array + other.numpy_array
        self.numpy_array = new_array
        return self

    def __sub__(self, other):
        """

       Args:
           other (Vector):

       Returns:
           Vector:
       """
        new_array = self.numpy_array - other.numpy_array
        new_vector = Vector.from_numpy_array(new_array)
        return new_vector

    def __isub__(self, other):
        """

        Args:
            other (Vector):

        Returns:
            Vector:
        """
        new_array = self.numpy_array - other.numpy_array
        self.numpy_array = new_array
        return self

    def __mul__(self, other):
        """

        Args:
            other (Vector or Number):

        Returns:
            Vector:
        """
        if isinstance(other, Number):
            new_array = self.numpy_array * other

        else:
            new_array = self.numpy_array * other.numpy_array

        new_vector = Vector.from_numpy_array(new_array)
        return new_vector

    def __imul__(self, other):
        """

        Args:
            other (Vector or Number):

        Returns:
            Vector:
        """
        if isinstance(other, Number):
            new_array = self.numpy_array * other

        else:
            new_array = self.numpy_array * other.numpy_array

        self.numpy_array = new_array
        return self

    def __str__(self):
        return str(self._numpy_array)

    def __iter__(self):
        for i in self.numpy_array:
            yield i


if __name__ == '__main__':
    test_vector_1 = Vector([0, 0, 0])
    test_vector_2 = Vector([1.0, 5, 3])
    the_dist = Vector.distance(test_vector_1, test_vector_2)
    test_vector_3 = test_vector_2 * 2
    print(test_vector_1)
    print(test_vector_2)
    print(test_vector_3)
    print(the_dist)
