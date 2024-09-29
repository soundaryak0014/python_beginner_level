# SUM OF NATURAL NUMBERS IN RECURSION:

def sum_of_numbers(n):
  if n==0:
      return 0
  elif n==1:
      return 1
  else:
      return n + sum_of_numbers(n-1)

num=int(input("Enter the number:"))
print(sum_of_numbers(num))