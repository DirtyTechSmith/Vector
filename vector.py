import numpy as np
from collections.abc import Iterable


class Vector(object):
    def __init__(self, numbers_list=None):
        """

        Args:
            numbers_list (Iterable[Number]):
        """
        self._numpy_array = None
        if numbers_list is not None:
            self._numpy_array = np.asarray(numbers_list)

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

        Args:
            vector_1 (Vector):
            vector_2 (Vector:

        Returns:
            float:
        """
        dist = np.linalg.norm(vector_1.numpy_array - vector_2.numpy_array)
        return dist

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
        return self._numpy_array[0]

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
        return self._numpy_array[1]

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
        return self._numpy_array[2]

    @z.setter
    def z(self, value):
        """

        Args:
            value (Number):

        Returns:

        """
        self._numpy_array[2] = value

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

    def __str__(self):
        return str(self._numpy_array)


if __name__ == '__main__':
    test_vector_1 = Vector([0, 0, 0])
    test_vector_2 = Vector([1.0, 5, 3])
    dist = Vector.distance(test_vector_1, test_vector_2)
    print(test_vector_1)
    print(test_vector_2)
    print(dist)
