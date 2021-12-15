

# Реализация алгоритма кодирования информации по Хаффману.

input_array = [0.33, 0.27, 0.20, 0.12, 0.08]
# input_array = [11, 9, 1]


def create_tree_knot(input_array):
    """ Определяем массив кортежей, где каждый кортеж является листом дерева.
    Каждый такой лист имеет такую структуру -- (S, L, R), где 
    
    S --... 
    L --...
    R --..."""

    # Если листьев в дереве N, то узлов в этом же едереве всегда N-1!
    array_of_knot = [(sum(input_array), 0, 0)] * (len(input_array) * 2 - 1)

    for index in range(len(input_array)):
        array_of_knot[len(input_array) + index - 1] = (input_array[index], 0, 0)
    
    return array_of_knot


def alter_tree_knot(array, index_knot_tree, sum_probabilities, left_child_index, right_child_index):
    array[index_knot_tree] = (sum_probabilities, left_child_index, right_child_index)
    return None


def idk(array, index, index_knot):
    while index > -1:
        # Создаём новый узел-родитель
        sum_probabilities = array[index_knot][0] + array[index_knot - 1][0]
        sum_probabilities = round(sum_probabilities, 3)
        alter_tree_knot(array, index, sum_probabilities, index_knot - 1, index_knot)

        # Переопределяем левый узел-потомок
        alter_tree_knot(array, index_knot - 1, array[index_knot - 1][0], array[index_knot - 1][1], array[index_knot - 1][2])

        # Переопределяем правый узел-потомок
        alter_tree_knot(array, index_knot, array[index_knot][0], array[index_knot][1], array[index_knot][2])

        # Сортируем массив в обратном порядке. Ключ сортировки -- четвёртый элемент кортежа,
        # то есть сортируем по убыванию вероятности!
        array = sorted(array, key=lambda element: element[0], reverse=True)

        index -= 1
        index_knot -= 2
    return array


def haffman_algorithm(input_array):
    index_knot = (len(input_array) * 2 - 1) - 1
    index = (len(input_array) - 1) - 1


    array_of_knot = create_tree_knot(input_array)

    array_of_knot = idk(array_of_knot, index, index_knot)

    return array_of_knot
    


if __name__ == '__main__':
    # assert sum(input_array) == 1, 'Сумма элементов массива input_array != 1'

    print(haffman_algorithm(input_array))