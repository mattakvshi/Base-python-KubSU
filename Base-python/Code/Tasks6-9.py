
# #Laba 6 Task 8
#
# n = int(input())
# maxOfSequence = 0
#
# while n != 0:
#
#     if n > maxOfSequence:
#         maxOfSequence = n
#
#     n = int(input())
#
# print(maxOfSequence)


#Laba 7 Task 10

# someList = []
#
# for i in range(10):
#     someList.append(int(input()))
#
# print(someList)
# someList.sort()
# print("Min = " + str(someList[0]))
# someList.reverse()
# print("Max = " + str(someList[0]))


#Laba 8 Task 3

# def capitalizeAllWords(s):
#     words = s.split()
#     if len(words) == 0:
#         return ""
#     else:
#         firstWord = words[0]
#         modifiedWord = firstWord[0].upper() + firstWord[1:]
#         remainingStrind = " ".join(words[1:])
#         return modifiedWord + " " + capitalizeAllWords(remainingStrind)
#
#
# defaultString = input()
# print(capitalizeAllWords(defaultString))



#Laba 9 Task 4

n = int(input())

matrix = [[0 if i != j else 0 for j in range(n)] for i in range(n)]

for row in matrix:
    print(row)
print("\n")

for k in range(1, n):
    for i in range(n - k):
        j = i + k
        matrix[i][j] = matrix[j][i] = k


for row in matrix:
    print(row)