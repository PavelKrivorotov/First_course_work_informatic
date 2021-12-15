

# Реализация алгоритма кодирования информации по Шенону-Фано.

input_array = [0.33, 0.27, 0.20, 0.12, 0.08]


def create_tree_knot(input_array):
    """Создаем структуру данных --> дерево. Представляена эта структура как список кортежей, где
    каждый кортеж является узлом дерева.
    
    Первый элемент каждого кортежа-узла --> частота появления или сумма частот
    Второй элемент --> Сылка на левого потомка (Индекс левого потомка-узла в массиве array_of_knot)
    Третий элемент --> Сылка на левого потомка (Индекс левого потомка-узла в массиве array_of_knot)"""

    array_of_knot = [(0, 0, 0)] * (len(input_array) *2 - 1)
    return array_of_knot


def alter_tree_knot(array, index_knot_tree, sum_probabilities, left_child_index, right_child_index):
    """Перезаписываем элемент -- узел в заданном массиве.

    На вход подаётся:
    array --> Массив в котором предстоит заменить узел-элемент.
    index_knot_tree --> Индекс узла, который предстоит заменить.
    sum_probabilities --> Вероятность появления символа для Листа и сумма вероятносятей для узла-родителя
    left_child_indxe --> Индекс левого узла-потомка
    right_child_index --> Индекс правого узла-потомка"""

    array[index_knot_tree] = (sum_probabilities, left_child_index, right_child_index)
    return None


def search_same_amounts(array):
    """Осуществляет поиск индекса по которому следует разбить массив на два подммассива так,
    чтобы сумма первого и второго подмассивов была примерно одинакова.
    
    Реализация тут самая наипростейшая."""

    index, temp_sum = 0, 0
    
    while temp_sum < sum(array) - temp_sum:
        temp_sum += array[index]

        index += 1
    return index


def idk(input_array, array_of_knot, index_of_knot):
    """Долго думал как назвать функцию... в общем так и не придумал видимо.
    
    На вход подаётся:
    input_array --> Наш первоначальный массив вероятностей...
    array_of_knot --> Пустая структура дерева, готовая для перестроения...
    index_of_knot --> Индекс в массиве array_of_knot. Создан для последовательной записи новых узлов в массив
    
    Что делет функция? --> Рекурсивно разбивает входной массив input_array на два подмассива, а потом каждый
    из этих подмассивов также на два подмассива и так далее, пока разбиение не приведёт к массиву с одним значением
    (длина такого массива будет равна 1 (единице))
    
    А дальше снизу вверх, ну то есть рекурсивно начинает собираться к первоначальному состоянию, попутно создавая
    новые узлы и тем самым выстраивая дерево."""

    # Если длина массива input_array, поданного на в ход вдруг оказалась равна 1 (короче в массиве остался один элемент),
    # то будем действовать по данным инструкциям, описанным ниже в 3 строчки. после чего функция вернёт index_of_knot + 1
    # и дальнейшие инструкции выполняться в ЭТОМ вызове функции idk(...) не будут.
    if len(input_array) == 1:
        alter_tree_knot(array_of_knot, index_of_knot ,input_array[0], 0, 0)
        return index_of_knot - 1

    # Определяем индекс разбиения массива так что бы sum(input_array[a1, a2, ...]) sum(input_array[..., a(n-1), a(n)]).
    index_same_amount = search_same_amounts(input_array)

    # Создаем два среза массива input_array. В left_array все элементы в промежутке [0, index_same_amount),
    # В right_array [index_same_amount, n].
    left_array = input_array[ :index_same_amount]
    right_array = input_array[index_same_amount: ]

    # Рекурсивно вызываем функцию idk(...) =, попутно уменьшая количество элементов в массиве input_array, а также
    # увеличиваем index_of_knot для того чтобы запись новых узлов в массив array_of_knot проходила успешно.
    left_index_knot = idk(left_array, array_of_knot, index_of_knot)
    right_index_knot = idk(right_array, array_of_knot, left_index_knot)

    # Создаем новый узел-родитель (мнимый). sum_probabilities -- сумма вероятностей левого и правого дочерних узлов.
    sum_probabilities = sum(input_array)
    sum_probabilities = round(sum_probabilities, 3)
    alter_tree_knot(array_of_knot, right_index_knot, sum_probabilities, left_index_knot + 1, right_index_knot + 1)

    return right_index_knot - 1


def fano_algorithm(input_array):
    array_of_knot = create_tree_knot(input_array)

    index_of_knot = len(array_of_knot) - 1
    idk(input_array, array_of_knot, index_of_knot)

    return array_of_knot


if __name__ == '__main__':
    print(fano_algorithm(input_array))