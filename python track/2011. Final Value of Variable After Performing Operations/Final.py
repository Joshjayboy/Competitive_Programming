class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
         # Initialize the variable X
        X = 0
        
        # Iterate through the operations
        for op in operations:
            if "++" in op:
                X += 1
            elif "--" in op:
                X -= 1
        
        return X