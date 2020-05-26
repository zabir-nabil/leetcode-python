'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 == 0:
            return False
        return True
        
        # slow solution
        winner = [-1]*(n+10)
        
        winner[0] = 0
        winner[1] = 1
        
        for i in range(n+4):
            if winner[i] == 0:
                winner[i+1] = 1
                winner[i+2] = 1
                winner[i+3] = 1
            elif winner[i] == 1:
                if winner[i+1] == -1:
                    winner[i+1] = 0
                if winner[i+2] == -1:
                    winner[i+2] = 0
                if winner[i+3] == -1:
                    winner[i+3] = 0      
                
        if winner[n] == 1:
            return True
        
        return False