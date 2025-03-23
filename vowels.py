s=str(input())
vowels=['a','e','i','o','u']
count=0
for i in s:
  if i in vowels:
    count=count+1
    print(i)
  else:
    continue
print(count)  