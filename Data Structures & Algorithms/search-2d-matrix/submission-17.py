class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        def bst(arr, t):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2
                if t == arr[m]:
                    return True
                elif t < arr[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            return False

        while l <= r:
            m = (l + r) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                return bst(matrix[m], target)
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1

        return False

        