
import itertools

class TwoSum:

    @staticmethod
    def find_two_sum(list_of_integers, target_value):
        """
        :param list_of_integers: A list of integers.
        :param target_value: We are looking for the indexes of two numbers that sum to this target value
        :returns: An ordered tuple of (index0, index1), indexes in the list_of_integers for numbers which sum to this target value, where index0 < index1.
        """
        for combo in itertools.combinations(enumerate(list_of_integers), 2):
            (i, m), (j, n) = combo
            if m + n == target_value:
                retval = tuple(sorted((i, j)))  # negligable effect on speed.
                return retval

if __name__ == '__main__':

    assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 13) == (0, 2)
    assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 14) is None
    assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 4) == (3, 4)
    assert TwoSum.find_two_sum([-82, 84, 85, -68, -18, -83, 2, -24, 52, 74], 86) == (1, 6)
    
