class set_solution:
    def subsets(self, nums):
        new_set = [[]]

        for num in nums:

            new_set += [(i + [num]) for i in new_set]
        return new_set
