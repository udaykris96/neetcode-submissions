class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = 0
        n = len(arr)

        for i in range(n):
            if i  == n-1:
                arr[i] = -1
            else:
                for j in range(i+1, n):
                    greatest = max(greatest, arr[j])
                arr[i] = greatest
                greatest = 0
        
        return arr 
        
        