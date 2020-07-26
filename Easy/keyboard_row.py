from typing import List
# QUESTION URL: https://leetcode.com/problems/keyboard-row/

class Solution:
    KEYBOARD_ROW_TOP = "qwertyuiop"
    KEYBOARD_ROW_MID = "asdfghjkl"
    KEYBOARD_ROW_BOT = "zxcvbnm"
    
    def findWords(self, words: List[str]) -> List[str]:
        row_typeable = []
        for word in words:
            if word[0].lower() in self.KEYBOARD_ROW_TOP:
                row = self.KEYBOARD_ROW_TOP
            elif word[0].lower() in self.KEYBOARD_ROW_MID:
                row = self.KEYBOARD_ROW_MID
            else:
                row = self.KEYBOARD_ROW_BOT
            
            typeable = True
            
            for letter in word:
                if letter.lower() not in row:
                    typeable = False
                    break

            if typeable:
                row_typeable.append(word)
                    
        return row_typeable

if __name__ == "__main__":
    sln = Solution()
    print(sln.findWords(["Hello","Alaska","Dad","Peace"]))
