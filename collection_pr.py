from collections import Counter,defaultdict
from itertools import count

# numbers = [1,2,2,3,3,3]
# count = Counter(numbers)
# print(count)
#
# def count_words(text: str ,n :int) -> Counter:
#     words = text.lower().split()
#     counts= Counter(words)
#     return counts.most_common(n)
# text = input (str("enter your text: "))
# result = count_words(text,2)
# print(result)

students = [
    ("Vivek", "A"),
    ("Anu", "B"),
    ("Rahul", "A")
]

grouped = defaultdict(list)

for name, grade in students:
    grouped[grade].append(name)

print(dict(grouped))

def job_department(job_dept):
    grouped = defaultdict(list)
    for name, department in job_dept:
        grouped[department].append(name)
    return dict(grouped)
employees = [
    ("Vivek", "IT"),
    ("Anu", "HR"),
    ("Rahul", "IT"),
    ("Sneha", "Finance")
]
print(job_department(employees))

students = [
    ("Vivek", "A"),
    ("Anu", "B"),
    ("Rahul", "A")
]
grouped = defaultdict(lambda :{"count" : 0 , "students" :[]})
for name, grade in students:
    grouped[grade]["count"] += 1
    grouped[grade]["students"].append(name)
print(dict(grouped))



