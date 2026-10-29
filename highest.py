marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}
highest=max(marks.values())
for name,score in marks.items():
    if score==highest:
        print(name,score)
