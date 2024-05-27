
class Solution:
    def my_sqrt(self, x: int) -> int:
        # Initialize the left and right boundaries for binary search
        L, R = 1, x

        # Perform binary search
        while (L <= R):
            # Calculate the midpoint
            M = (L+R)//2
            # Calculate the square of the midpoint
            m_squared = M*M

            # If the square of the midpoint is equal to x, return the midpoint
            if m_squared == x:
                return M
            # If the square of the midpoint is greater than x, update the right boundary
            elif m_squared > x:
                R = M-1
            # If the square of the midpoint is less than x, update the left boundary
            else:
                L = M+1


sl= Solution()
print(sl.my_sqrt(64))