num = int(input("Ask for a number "))
i = 1

while i <= num:
  #print (i) 
  if i % 3 == 0 and i % 5 == 0:
    print ("fizzbuzz")
  elif i % 5 == 0:
    print ("buzz")
  elif i % 3 == 0:
    print ("fizz")
  else: 
    print (i)
  i += 1 

  
# user_num = int(input("Enter a number" ))

# for num in range(1, user_num):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)
    