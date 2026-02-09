#phython recursion
def countdown(n):        #di panggil diri sendiri 
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)        # ini juga manggil diri

countdown(5)          

#Base Case and Recursive Case
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1       #
  # Recursive case
  else:
    return n * factorial(n - 1)    #factorial manggil diri sendiri

print(factorial(5))