"""
Purpose: Regular Expressions
    Using re.match
        - It helps to identify patterns at the starting of string
        - By default, it is case-sensitive
"""

import re

# print(dir(re))

target_string = "Python Programming is good for health"
search_string = "python"

print(f"{target_string.find(search_string) =}")
print(f"{search_string in target_string    =}")
print()

reg_obj = re.compile(search_string)
print(reg_obj, type(reg_obj))

result = reg_obj.match(target_string)
print(f"{result =}")

if result:
    print(f"result.group():{result.group()}")
    print(f"result.span() :{result.span()}")
    print(f"result.start():{result.start()}")
    print(f"result.end()  :{result.end()}")
else:
    print("NO match found")
