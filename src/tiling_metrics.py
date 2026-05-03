def lane_density(nums, mod=30):
    lanes = {}
    for n in nums:
        r = n % mod
        lanes[r] = lanes.get(r, 0) + 1
    total = len(nums)
    return {k: v/total for k, v in lanes.items()}
