"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left and right product lists
        left_product = nums.copy()
        for i in range(1, len(left_product)):
            left_product[i]*=left_product[i-1]
        right_product = nums.copy()
        for i in range(len(right_product)-2, -1, -1):
            right_product[i]*=right_product[i+1]
        left_product=[1]+left_product[:-1]
        right_product=right_product[1:]+[1]
        res = []
        for i in range(len(nums)):
            res.append(left_product[i]*right_product[i])
        return res


# 20220221
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur_prod = 1
        ans = []
        product_forward = []
        for i in nums:
            cur_prod *= i
            product_forward.append(cur_prod)
        product_backward = []
        cur_prod = 1
        for i in range(len(nums)-1, -1, -1):
            cur_prod *= nums[i]
            product_backward.append(cur_prod)
        product_backward = product_backward[::-1]
        ans.append(product_backward[1])
        for i in range(1, len(nums)-1):
            ans.append(product_forward[i-1]*product_backward[i+1])
        ans.append(product_forward[-2])
        return ans


# space O(1) solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p = 1
        for i in nums:
            ans.append(p)
            p *= i
        p = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        return ans


# 20230410
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_product, right_product = [nums[0]]*l, [nums[-1]]*l
        for i in range(1,l):
            left_product[i] = nums[i] * left_product[i-1]
        for i in range(l-2, -1, -1):
            right_product[i] = nums[i] * right_product[i+1]
        res = []
        left_product = [1] + left_product
        right_product = right_product + [1]
        for i in range(1,l+1):
            res.append(left_product[i-1]*right_product[i])
        return res