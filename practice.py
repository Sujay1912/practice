#Q1: Print numbers from 1 to 10.
# for i in range(1,101):
#     print(i)
import time

#Q2: Print even numbers from 2 to 20.
# for i in range(2,21,2):
#     print(i)

#Q3: Print each character of a string "Python"
# for char in "Python":
#     print(char)

#Q4: Calculate the sum of elements in a list [1, 2, 3, 4, 5].
# nums=[1,2,3,4,5]
# total=0
# for num in nums:
#     total +=num
#     print(total)

#Q5: Find the product of elements in a list [2, 3, 4]
# nums=[2,3,4]
# total=1
# for num in nums:
#     total *=num
#     print(total)

#Q6: Print the squares of numbers from 1 to 5.
# for i in range(1,6):
#     total= i**2
#     print(total)

#Q7: Print the first 5 multiples of 3.
# num=3
# for i in range(1,6):
#     total=num*i
#     print(total)

#Q8: Count the number of vowels in a string "hello".
# word="Hello"
# count=0
# for char in word:
#     if char in "aeiou":
#         count +=1
#         print(count)

#Q9: Reverse a string "world".
# word="World"
# reverse_word=""
# for char in reversed(word):
#     reverse_word +=char
#     print(reverse_word)

#Q10: Print the keys of a dictionary {'a': 1, 'b': 2}.
# dict={'a': 1, 'b': 2}
# for key in dict:
#     print(key)
#-------------------------------------------------------------------------------------------------
# Q11: Print numbers from 10 down to 1.
# num=10
# while num>0:
#     print(num)
#     num -=1

# Q12: Get input until "quit" is entered.
# inp=""
# while inp !="quit":
#     inp = input("Enter a word")


# Q13: Calculate the factorial of 5.
# n=5
# fact=1
# while n>0:
#     fact *=n
#     n -=1
#     print(fact)


# Q14: Find the first power of 2 greater than 100.
# power=1
# while power <=100:
#     power *=2
#     print(power)

# Q15: Reverse a number (e.g., 123 becomes 321).
# num=123
# reverse_num=0
# while num>0:
#     reverse_num=reverse_num *10 + num %10
#     num //=10
#     print(reverse_num)


# Q16: Check if a number is a palindrome.
# num=121
# temp=num
# reverse_num=0
# while temp>0:
#     reverse_num=reverse_num *10 + temp%10
#     temp//=10
#     print(num==reverse_num)


# Q17: Simulate a simple countdown timer.
# count=5
# while count>0:
#     print(count)
#     time.sleep(1)
#     count -=1
#     print("Blastoff!")

# Q18: Keep asking for a positive number until one is entered.
# num=-1
# while num <=0:
#     num=int(input("Enter Positive number: "))

# Q19: Find the greatest common divisor (GCD) of two numbers.
# a,b=24,36
# while b:
#     a,b=b,a
#     a%b
#     print(a)

#Q20: Sum the digits of a number
# num=456
# total=0
# while num>0:
#     total +=num %10
#     num//=10
#     print(total)

#Q1: Print numbers 1 to 10, but stop at 5 using break.
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)

#Q2: Print odd numbers from 1 to 10 using continue.
# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)

#Q3: Create an empty loop using pass.
# for i in range(5):
#     pass

#Q4: Find the first even number in a list and print it.
# list=[1,3,4,5]
# for i in list:
#     if i%2==0:
#         print(i)
#         break

#Q5: Skip printing strings with length less than 3
# strings = ["a", "abc", "abcd"]
# for i in strings:
#     if len(i)<3:
#         continue
#     print(i)

#Q6: Exit a while loop when a specific condition is met.
# count=0
# while True:
#     if count==3:
#         break
#     count +=1
#     print(count)

#Q7: Skip multiples of 3 in a loop.
# for i in range(11):
#     if i%3==0:
#         continue
#     print(i)

#Q8: Use pass as a placeholder in a conditional inside a loop.
# for i in range(5):
#     if i==2:
#         pass
#     print(i)

#Q9: Stop a while loop when a user enters a specific value.
# inp=""
# while True:
#     val=input("Enter (stop to exit)")
#     if val=="stop":
#         break
#     print(val)

#Q10: Break out of nested loops when a condition is met.
# for i in range(3):
#     for j in range(3):
#         if i==1 and j==1:
#             break
#         print(i,j)

# Q1:print([i for i in range(1, 11) if i % 2 == 0])
# Q2:print([i ** 2 for i in [1, 2, 3]])
# Q3:print([s.upper() for s in ["Hello", "World"]])
# Q4:print([i for i in ["a", "abc", "abcd"] if len(i) > 3])
# Q5:print([(i, v) for i, v in enumerate([10, 20, 30])])
# Q6:print([item for sublist in [[1, 2], [3, 4]] for item in sublist])
# Q7:print({k: v for k, v in zip(["a", "b"], [1, 2])})
# Q8:print([x for x in [1, "a", 2, "b"] if isinstance(x, int)])
# Q9:print([i > 5 for i in [1, 3, 5, 6]])
# Q10:print([len(word) for word in "Hello World".split()])

#Q1: Print a 3x3 matrix of asterisks.
# for i in range(3):
#     for j in range(3):
#         print("*", end=" ")
#     print()

#Q2: Print a multiplication table (1 to 5).
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j, end="\t")
#     print()

#Q3: Find pairs of numbers in a list that sum to 10.
# nums=[1,2,3,4,5,6]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] +nums[j] ==10:
#             print(nums[i],nums[j])

# # Q4: Print a triangle pattern of numbers.
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# Q5: Check if a matrix contains a specific element.
# matrix=[[1,2,3], [4,5,6]]
# target=5
# found=False
# for row in matrix:
#     for element in row:
#         if element ==target:
#             found=True
#             break
#         if found:
#                 break
# print(found)

# Q6: Find all prime numbers up to 20.
# for num in range(2,21):
#     for i in range(2,num):
#         if num % i==0:
#             break
#         else:
#             print(num)



