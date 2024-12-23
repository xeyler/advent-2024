dependencies = {}

def add_rule(line):
    dependency, dependent = map(int, line.split("|"))
    if dependent not in dependencies:
        dependencies[dependent] = set()
    dependencies[dependent].add(dependency)

def check_ordering(ordered_pages):
    pages_in_list = set(ordered_pages)
    encountered_pages = set()
    for page in ordered_pages:
        if page in dependencies and not dependencies[page].intersection(pages_in_list).issubset(encountered_pages):
            return False
        encountered_pages.add(page)
    return True

total = 0

with open('input') as input:
    encountered_newline = False
    for line in input:
        if not encountered_newline:
            if line == "\n":
                encountered_newline = True
            else:
                add_rule(line)
        else:
            ordered_pages = list(map(int, line.split(",")))
            if check_ordering(ordered_pages):
                total += ordered_pages[int(len(ordered_pages)/2)]

print(total)
