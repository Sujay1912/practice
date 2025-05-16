# Q1.Write a Python program that calculates the sum of all even numbers in a given list.
# numbers=[1,2,3,4,5,6]
# sum_even=0
# for num in numbers:
#     if num%2==0:
#         sum_even +=num
#         print("Sum of even numbers: ",sum_even)


# Q2.Write a Python program that counts how many numbers in a list are greater than a given threshold.
# numbers=[50,75,90,60,30]
# threshold=int(input("Enter the threshold value: "))
# count=0
# for num in numbers:
#     if num> threshold:
#         count +=1
#     print("number greater than threshold: ",count)


# Q3.Write a Python program that reverses a given list without using the built-in reverse() method.
# numbers=[1,2,3,4,5]
# reversed_list=[]
# for i in range(len(numbers)-1,-1,-1):
#     reversed_list.append(numbers[i])
#     print("reversed_list: ",reversed_list)


# Q4.Write a Python program to find and print the largest number in a given list without using the max() function.
# numbers=[45,78,90,66,89]
# max_num=numbers[0]
# for num in numbers:
#     if num> max_num:
#         max_num=num
#     print("Largest number:",max_num)


# Q.5.Write a Python program to remove all duplicate elements from a given list and print the unique values.
numbers=[10,20,20,30,40,40,10,50]
unique_list=[]
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
        print("List after removing duplicates:",unique_list)
