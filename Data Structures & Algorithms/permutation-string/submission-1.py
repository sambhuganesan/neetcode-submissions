class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        frequency_of_s1 = [0]*26
        frequency_of_s2 = [0]*26

        for i in s1:
            frequency_of_s1[ord(i) - 97] += 1
        for i in range(len(s1)):
            frequency_of_s2[ord(s2[i]) - 97] += 1
        if frequency_of_s1 == frequency_of_s2:
            return True

        for i in range(len(s1), len(s2)):
            frequency_of_s2[ord(s2[i]) - 97] += 1
            frequency_of_s2[ord(s2[i - len(s1)]) - 97] -= 1
            if frequency_of_s1 == frequency_of_s2:
                return True
        
        return False