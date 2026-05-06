class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        arr = []
        for key, value in hashmap.items():
            arr.append([value, key])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res