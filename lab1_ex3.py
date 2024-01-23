import lab1_ex2

l = [52633, 8137, 1024, 999]
for i in range(len(l)):
    lab1_ex2.print_factor(l[i])

# def find_factors(num):
#     factors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)
#     return factors
#
# l = [52633, 8137, 1024, 999]
#
# for num in l:
#     factors = find_factors(num)
#     print(f"The factors of {num} are: {factors}")
