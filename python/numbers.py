print('Привет, GIT!')
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
for i in range(10):
    print(i)

with open('names.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    print(contents)