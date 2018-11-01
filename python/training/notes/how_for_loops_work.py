'''

C:
---

for (i=0 ; i<10 ; i++) {
    printf("%d\n", i);
    i = 5;
}
printf("%d\n", i);


'''

for i in range(10):
    print(i)
    i = 5
print(i)


''' What Python does:

data (iterable) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                           iterator ----------^
  i = 0
  print(i)
  i = 5
  i = 1
  print(i)
  i = 9
  print(i)
  i = 5
print(i)
'''
