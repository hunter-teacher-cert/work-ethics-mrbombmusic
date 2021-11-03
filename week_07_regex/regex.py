import re


# Still having trouble getting rid of extra word when name is just prefix and last name
# Example: [('Ms', ' Hartman was)] instead of [('Ms', ' Hartman')]
# Could find no clear way to get proper noun names (First name - Last name) without also locating any set of two words that both start with capital letters
def find_names(line):
    pattern = r"(Mr|Ms|Dr|Mrs)\.( [A-Z][a-z]+ ?[A-Z]?[a-z]+)"
    result = re.findall(pattern,line)
    return result

f = open("datefile.txt")
for line in f.readlines():
    name_result = find_names(line)
    if (len(name_result)>0):
        print(name_result)
