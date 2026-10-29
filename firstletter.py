words = ['apple', 'ant', 'banana', 'ball', 'cat']
empty={
}
for word in words:
    first_letter=word[0]
    if first_letter in empty:
       empty[first_letter].append(word)

    else:
       empty[first_letter]=[word]

print(empty)