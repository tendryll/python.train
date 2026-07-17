# ask why print indention results different results
# number = 5
# while number > 0:
#     print("Countdown:", number)
#     number -= 1
#
#     print("Blast off!")

# print("range(5, 0, -1) – countdown:")
# for number in range(5, 0, -1):
#     print("Countdown:", number)
# print("Blast off! 🚀")


# even_nums_from_zero_to_ten = list(range(0, 10, 2))
# print(even_nums_from_zero_to_ten)

# cat_attributes = {"name": "Zia", "age": 1, "color": "grey", "food": "tuna"}
#
# print("Keys only:")
# for key in cat_attributes:
#     print("-", key)

# print("Multiplication table (1-3):")
# for i in range(1, 4):          # outer loop: i = 1, 2, 3
#     for j in range(1, 4):      # inner loop: j = 1, 2, 3 (for every i)
#         print(f"  {i} x {j} = {i * j}")
#     print("  ---")


# for number in range(1, 10):
#     if number == 5:
#         print("Number 5 found! Exiting loop.")
#         break
#     print("Current number:", number)
# print("The loop has ended.")
#
# num_is_five = False
#
# number = 0
# while num_is_five == False and number < 10:
#     if number == 5:
#         print("Number 5 found! Exiting loop.")
#         num_is_five = True
#
#     print("Current number:", number)
#     number += 1
# print("The loop has ended.")

# continue skips the rest of THIS iteration and moves to the next
# for number in range(1, 6):
#     if number == 3:
#         print("Skipping number 3...")
#         continue              # jumps back to the top of the loop
#     print("Current number:", number)

# Print only even numbers using continue
# print("Even numbers 1–10:")
# for n in range(1, 11):
#     if n % 2 != 0:
#         continue
#     print(n, end=" ")
# print()
#
# print("Even numbers 1–10:")
# for n in range(2, 11, 2):
#     print(n, end=" ")
# print()


numbers = [1, 2, 2, 3, 4, 4, 5]
for idx, num in enumerate(numbers):
    if num == 2:
        numbers[idx] = 22

print(numbers)

# numbers = [1, 2, 2, 3, 4, 4, 5]
# new_list = []
#
# for num in numbers:
#     if num != 2:
#         new_list.append(num)
#
# print(new_list)