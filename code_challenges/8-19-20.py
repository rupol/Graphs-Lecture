"""
Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
For example, given the following object/dictionary as input:
{
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
Your algorithm should return 41, the sum of the values 23 and 18.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""
# input dict
# key: string/integer
# value: string/integer
# output: sum of all integers (dict values)


def sum_of_nums(dict):
    nums = []
    # loop through the dict values
    for item in dict.values():
        # find only the integers
        if type(item) == int:
            # save nums in a list
            nums.append(item)
    # sum all nums
    return sum(nums)


dict_a = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}

print(sum_of_nums(dict_a))
