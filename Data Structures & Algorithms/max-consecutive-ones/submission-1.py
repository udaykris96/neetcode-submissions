class Solution:
        def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            output = 0
            count = 0
            for i in range(0, len(nums)):
                if nums[i] == 1:
                    count = count + 1
                else:
                    if count > output:
                        output = count
                    count = 0
                                                                                                                                    
            if count > output:
                output = count
                                                                                                                                                                    
            return output
