import numpy as np
from collections.abc import Iterable
from numbers import Number


class Vector(object):
    def __init__(self, numbers_list):
        """

        Args:
            numbers_list (list[float]):
        """
        self.float_list = numbers_list  # type: list[float]

    # --------------------------- Class Methods -----------------------------------
    @classmethod
    def from_numpy_array(cls, numpy_array):
        """

        Args:
            numpy_array (np.ndarray):

        Returns:
            Vector:
        """
        the_list = list(numpy_array.tolist())
        new_vector = cls(the_list)

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
        return np.array(self.float_list)

    @property
    def x(self):
        """

        Returns:
            float:
        """
        return self.float_list[0]

    @x.setter
    def x(self, value):
        """

        Args:
            value (float):

        Returns:

        """

        self.float_list[0] = value

    @property
    def y(self):
        """

        Returns:
            float:
        """
        return self.numpy_array.item(1)

    @y.setter
    def y(self, value):
        """

        Args:
            value (float):

        Returns:

        """

        self.float_list[1] = value

    @property
    def z(self):
        """

        Returns:
            float:
        """
        return self.numpy_array.item(2)

    @z.setter
    def z(self, value):
        """

        Args:
            value (float):

        Returns:

        """

        self.float_list[0] = value

    # --------------------------- Methods -----------------------------------

    def normalize(self):
        """
        normalize the vector

        """
        norm = np.linalg.norm(self.numpy_array)
        if norm == 0:
            return

        new_array = self.numpy_array / norm  # type: np.ndarray
        self.float_list = list(new_array.tolist())

    def copy(self):
        """
        copy the current vector

        Returns:
            Vector:
        """
        new_list = [value for value in self.float_list]
        new_vector = Vector(new_list)
        return new_vector

    def asList(self):
        """

        Returns:
            list[float]:
        """
        return self.float_list

    # --------------------------- Overrides -----------------------------------
    def __add__(self, other):
        """

        Args:
            other (Vector):

        Returns:
            Vector:
        """
        new_list = []
        for my_value, other_value in zip(self.float_list, other.float_list):
            new_value = my_value + other_value
            new_list.append(new_value)

        new_vector = Vector(new_list)
        return new_vector

    def __iadd__(self, other):
        """

        Args:
            other (Vector):

        Returns:
            Vector:
        """
        new_list = []
        for my_value, other_value in zip(self.float_list, other.float_list):
            new_value = my_value + other_value
            new_list.append(new_value)

        self.float_list = new_list
        return self

    def __sub__(self, other):
        """

       Args:
           other (Vector):

       Returns:
           Vector:
       """
        new_list = []
        for my_value, other_value in zip(self.float_list, other.float_list):
            new_value = my_value - other_value
            new_list.append(new_value)

        new_vector = Vector(new_list)

        return new_vector

    def __isub__(self, other):
        """

        Args:
            other (Vector):

        Returns:
            Vector:
        """
        new_list = []
        for my_value, other_value in zip(self.float_list, other.float_list):
            new_value = my_value - other_value
            new_list.append(new_value)

        self.float_list = new_list
        return self

    def __mul__(self, other):
        """

        Args:
            other (Vector or Number):

        Returns:
            Vector:
        """
        if isinstance(other, Number):
            new_array = self.numpy_array * other  # type: np.ndarray

        else:
            new_array = self.numpy_array * other.numpy_array  # type: np.ndarray

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
            new_array = self.numpy_array * other  # type: np.ndarray

        else:
            new_array = self.numpy_array * other.numpy_array  # type: np.ndarray

        self.float_list = list(new_array.tolist())
        return self

    def __str__(self):
        return str(f'Vector: {self.float_list}')

    def __iter__(self):
        for i in self.float_list:
            yield i

    def __len__(self):
        return len(self.float_list)


if __name__ == '__main__':
    test_vector_1 = Vector([0, 0, 0])
    test_vector_2 = Vector([1.0, 5, 3])
    the_dist = Vector.distance(test_vector_1, test_vector_2)
    test_vector_3 = test_vector_2 * 2
    print(test_vector_1)
    print(test_vector_2)
    print(test_vector_3)
    print(the_dist)
