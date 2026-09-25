class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        def bin_search(end, f):
            start = 0
            while start < end:
                mid = (start + end) // 2
                if f(mid):
                    start = mid+1
                else:
                    end = mid

            return end if f(end) else -1

        h=[(nums[i],i-nums[i]) for i in range(len(nums)) if nums[i]<=i]
        h.sort()
        dp={x:1 for x in h}
        for i, v in enumerate(h):
            if i==0:
                continue
            imin=bin_search(end=i-1, f=lambda x: h[x][0]!=v[0] and h[x][1]<=v[1])
            if imin>=0:
               dp[v]=max(dp[v], dp[h[imin]]+1)
        return max(dp.values()) if dp.values() else 0





sol=Solution()
nums=[1,0,1,2]
print(sol.maxFixedPoints(nums))
