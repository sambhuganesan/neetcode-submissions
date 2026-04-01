class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        visited = set()
        for i in range(0, len(strs)):
            if strs[i] in visited:
                continue
            hashmap_i = {}
            for char in strs[i]:
                if char in hashmap_i:
                    hashmap_i[char] += 1
                else:
                    hashmap_i[char] = 1
            sub_array = [strs[i]]
            visited.add(strs[i])
            for j in range(i+1, len(strs)):
                if strs[i] == strs[j]:
                    sub_array.append(strs[j])
                    visited.add(strs[j])
                hashmap_j = {}
                for char in strs[j]:
                    if char in hashmap_j:
                        hashmap_j[char] += 1
                    else:
                        hashmap_j[char] = 1
                if (strs[j] not in visited) and (hashmap_i == hashmap_j):
                    sub_array.append(strs[j])
                    visited.add(strs[j])               
            output.append(sub_array)
        return output

