marks = {
    "Anir": 100,
    "shubham":56,
    "rohan":34
}

print(marks.items())
print(marks.keys())
print(marks.values())

#update method
marks.update({"Anir":99, "mohan":88})
print(marks)

#get method
print(marks.get("Anir"))