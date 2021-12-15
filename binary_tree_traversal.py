
input_array = [(1.0, 1, 2), (0.6, 3, 4), (0.4, 5, 6), (0.33, 0, 0), (0.27, 0, 0), (0.2, 7, 8), (0.2, 0, 0), (0.12, 0, 0), (0.08, 0, 0)]

# Реализация алгоритма обхода по дереву и составления бинарных кодов на основе
# переданного дерева.


def tree_traversal(input_array, array_binary_codes, root_nood_indxe, code='', index=0):
    if not input_array[root_nood_indxe][1] and not input_array[root_nood_indxe][2]:
        array_binary_codes[index] = code
        return index + 1

    left_root_nod_index = input_array[root_nood_indxe][1]
    right_root_nod_index = input_array[root_nood_indxe][2]

    index = tree_traversal(input_array, array_binary_codes, left_root_nod_index, code +'1', index)
    index = tree_traversal(input_array, array_binary_codes, right_root_nod_index, code +'0', index)

    return index


def binary_tree_traversal(input_array, root_nood_indxe=0):
    array_of_binary_codes = ['-1'] * (len(input_array) // 2 + 1)

    tree_traversal(input_array,array_of_binary_codes, root_nood_indxe)

    array_of_binary_codes.sort(key=lambda element: len(element))

    return array_of_binary_codes


if __name__ == '__main__':
    print(binary_tree_traversal(input_array))