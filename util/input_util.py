def to_two_num(text):
    nums = [int(n) for n in text.split(",")]
    return nums[0], nums[1]
