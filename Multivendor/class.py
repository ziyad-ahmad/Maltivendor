# for i in range(1,13,1):
#     for j in range(1,13,1):
#         print(str(i) + ' * ' + str(j) + ' = ' + str(i*j),  end = " \t ")
#     print("\n")

# print("    ", end="")
# for j in range(1, 13):
#     print(f"{j:4}", end="")
# print("\n" + "-" * 53)

# Display the multiplication table
for i in range(1, 13):
    # Display the header for each row
    print(f"{i:2} | ", end=" ")
    for j in range(1, 13):
        print(f"{i * j: 4}", end=" ")
    print()
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()