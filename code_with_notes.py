import itertools
class TwoSum:

    @staticmethod
    def find_two_sum(list_of_integers, target_value):
        """
        :param list_of_integers: A list of integers.
        :param target_value: We are looking for the indexes of two numbers that sum to this target value
        :returns: An ordered tuple of (index0, index1), indexes in the list_of_integers for numbers which sum to this target value, where index0 < index1.
        """

        # # bruit force first...
        # for i, n in enumerate(list_of_integers):
        #     for j, m in enumerate(list_of_integers):
        #         if j == i:
        #             continue
        #         if m + n == target_value:
        #             return tuple(sorted((i, j)))

        # round two!
        # itertools.combinations should be fast.
        # more thining!... it should be reasonably fast to use enumerate here too...


        # time to clean up. I'll preserve this marked-up version.
        
        for combo in itertools.combinations(enumerate(list_of_integers), 2):
            (i, m), (j, n) = combo
            if m + n == target_value:
                retval = tuple(sorted((i, j)))  # negligable effect on speed.
                return retval

        # more thinking... what's wrong with this...?
        # HOLY SMOKES! I saw "recording" and didn't see the "share desktiop" button. I thought I was done!
        # as a backup. I have been recording w/ quicktime. grr!!!
        # see above. nothing much exciting has happened
        # will send the qt recording also. time to stop thrashing myself.
        # thinking... still...
        # I believe that `combinations` is the most efficient way of listing the pairs. we can't do
        # anything about the speed of `+`. I don't doubt there's a trik. thinking.
        # let's do some quick testing of performance.

        # I'm not coming up with a linear time solution. Considering "cheating" shortly...
        # assume better than O^2 means "linear". I can't imagine something in-between.
        # hm. well. let' slook around
        # yes! obvious cheating here. I _need_ the answer. I am going to have to look at the book
        # not the same problem! and we lose indexes.
        # but ideas...?

        # we could use that solution to get the numbers (linear) and find their indicies (linear)
        # requires calculating the len of the list, also linear
        # try?...
        # Returns number of pairs in arr[0..n-1] 
    # with sum equal to 'sum'
    def getPairsCount(arr, sum):

        n = len(arr)
        m = [0] * 1000

        # Store counts of all elements in map m
        for i in range(0, n):
            m[arr[i]]
            m[arr[i]] += 1

        twice_count = 0

        # Iterate through each element and increment
        # the count (Notice that every pair is 
        # counted twice)
        for i in range(0, n):

            twice_count += m[sum - arr[i]] 

            # if (arr[i], arr[i]) pair satisfies the
            # condition, then we need to ensure that
            # the count is  decreased by one such 
            # that the (arr[i], arr[i]) pair is not
            # considered
            if (sum - arr[i] == arr[i]):
                twice_count -= 1

        # return the half of twice_count
        return int(twice_count / 2)

    # hm! no, we cannot use this. we lose the value of the "first" int when calculating the sum

if __name__ == '__main__':

    # hrrm.. well, we assume only one pair?
    # I don't see it in the instructions, but I will assume that we want the *first* such pair. Return value is
    # always a two-tuple or None... no other possiblities.
    # the above is obviously slow. thinking...
    assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 13) == (0, 2)
    assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 14) is None
    assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 4) == (3, 4)
    assert TwoSum.find_two_sum([-82, 84, 85, -68, -18, -83, 2, -24, 52, 74], 86) == (1, 6)
    
