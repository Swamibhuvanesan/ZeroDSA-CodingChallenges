def max_product_subarray(nums):
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for num in nums[1:]:
        temp_max = max(num, num * max_product, num * min_product)
        min_product = min(num, num * max_product, num * min_product)
        max_product = temp_max
        
        result = max(result, max_product)
    
    return result

# Test with the provided examples
print(max_product_subarray([1, 2, 3, 4, 5, 0]))  # Output: 120
print(max_product_subarray([1, 2, -3, 0, -4, -5]))  # Output: 20
