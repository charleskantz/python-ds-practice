def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    return max(counter, key=counter.get) 
    """got return line from StackOverflow, uses get() to grab value from each key,
    then max() finds the highest and returns the key of the highest"""
