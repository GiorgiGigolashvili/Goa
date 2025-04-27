#code warsis codebs ese davwer tole adgili agar maq kompiuterze!
def sort_numbers(nums):
    if nums is None:
        return []
    return sorted(nums, key=lambda x: (x < 0, x % 2 == 0, x))
