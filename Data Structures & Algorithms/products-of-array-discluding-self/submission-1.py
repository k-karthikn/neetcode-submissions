class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [nums[0]]
        suf = [nums[-1]]

        for i in range(1, len(nums)):
            pref.append(pref[-1] * nums[i])
            suf.append(suf[-1] * nums[len(nums) - i - 1])

        suf.reverse()

        result = []

        for i in range(len(nums)):
            left = pref[i - 1] if i > 0 else 1
            right = suf[i + 1] if i < len(nums) - 1 else 1

            result.append(left * right)

        return result