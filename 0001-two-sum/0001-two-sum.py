class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_aux = {}

        for i, key_i in enumerate(nums):
            dict_aux[target - key_i] = i

        for j, key_j in enumerate(nums):
            if key_j in dict_aux.keys() and j != dict_aux[key_j]:
                return [j, dict_aux[key_j]]