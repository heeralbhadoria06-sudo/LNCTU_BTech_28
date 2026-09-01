class Solution:
    def maximumSum(self, arr):
        no_delete = arr[0]
        one_delete = float('-inf')
        answer = arr[0]

        for i in range(1, len(arr)):
            # Delete current element
            one_delete = max(
                no_delete,              
                one_delete + arr[i]    
            )
            no_delete = max(
                arr[i],
                no_delete + arr[i]
            )
            answer = max(answer, no_delete, one_delete)
        return answer
