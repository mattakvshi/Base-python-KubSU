def create_matrix(n, m):
    matrix = [[0] * m for _ in range(n)] #Создаём матрицу NxM и заполняем нулями
    counter = 1 #Счётчик итераций или значение вставляемое в ячеёку

    # if (n == m):
    for diag in range(n + m - 1): #Перебераем диагоналди от 0 до n + m - 1
        start_i = max(0, diag - m + 1) #Верхняя ячейка диагонали
        end_i = min(diag, n - 1)  #Нижняя ячейка диагонали

        for i in range(start_i, end_i + 1): #Идём от верхней до нижней ячейки диагонали
            matrix[i][diag - i] = counter #Записываем соответствующее значение
            counter += 1
    # else:
    #     for diag in range((n + m - 1)//2):
    #         start_i = max(0, diag - m + 1)
    #         end_i = min(diag, n - 1)
    #
    #         for i in range(start_i, end_i + 1):
    #             matrix[i][diag - i] = counter
    #             counter += 1
    #
    #     for diag in range(((n + m - 1)//2), n + m - 1):
    #         start_i = max(0, diag - m + 1)
    #         end_i = min(diag, n - 1)
    #
    #         for i in range( start_i,end_i + 1):
    #             matrix[i][diag - i] = counter
    #             counter += 1



    return matrix


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = create_matrix(n, m)

for i in matrix:
    print(i)