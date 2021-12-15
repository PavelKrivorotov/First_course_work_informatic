# 
# 
# Внимание! Программа не была протестирована на случаях когда текстовый файл пустой ИЛИ
# когда в тексте содержится всего один сивмвол ИЛИ когда текст состоит только из одного
# символа, повторяющегося n-раз. Хотя я предполагаю, что будет выбита ошибка Error... .
# 
# В остальных случаях программа должна работать корректно.
# 
# Программа расчитана на текст, состоящий из символов национального алфавита (яз. Русский).
# 
# 


import numpy as np


from create_input_array import create_input_array

from haffman_algorithm import haffman_algorithm
from fano_algorithm import fano_algorithm

from binary_tree_traversal import binary_tree_traversal


def create_table(chars, input_array, list_codes_fano, list_codes_haffman):
    max_length = 17

    max_length_fano = len(max(list_codes_fano, key=lambda length:len(length)))
    max_length_haffman = len(max(list_codes_haffman, key=lambda length:len(length)))

    if max_length_fano > max_length_haffman and max_length_fano > max_length:
        max_length = max_length_fano + 2
    elif max_length_haffman > max_length_haffman and max_length_haffman > max_length:
        max_length = max_length_haffman + 2


    print(f'+{"-"*16}+{"-"*21}+{"-"*max_length}+{"-"*max_length}+')
    print(f'|{"Буква алфавита":^16s}|{"Количество в тексте":^21s}|{"Код по Фано":^{max_length}s}|{"Код по Хаффману":^{max_length}s}|')

    print(f'+{"-"*16}+{"-"*21}+{"-"*max_length}+{"-"*max_length}+')


    for index in range(len(chars)):
        print(f'|{chars[index]:^16s}|{input_array[index]:^21d}|{list_codes_fano[index]:^{max_length}s}|{list_codes_haffman[index]:^{max_length}s}|')

        print(f'+{"-"*16}+{"-"*21}+{"-"*max_length}+{"-"*max_length}+')
    
    return None


def create_table_2(input_array, list_codes_fano, list_codes_haffman):
    sum_bits_fano, sum_bits_haffman = 0, 0
    entropy = 0
    sum_words = sum(input_array)

    for index in range(len(input_array)):
        sum_bits_fano += input_array[index] * len(list_codes_fano[index])
        sum_bits_haffman += input_array[index] * len(list_codes_haffman[index])

        p_i = input_array[index] / sum_words
        entropy += (-1) * p_i * (np.log2(p_i))
    
    entropy = round(entropy, 3)

    print('\n')
    print(f'+{"-"*7}+{"-"*10}+{"-"*20}+{"-"*25}+{"-"*15}+')
    print(f'|{" ":^7s}|{"Символов":^10s}|{"Бит для код.По Фано":^20s}|{"Бит для код.По Хаффману":^25s}|{"Энтропия":^15s}|')

    print(f'+{"-"*7}+{"-"*10}+{"-"*20}+{"-"*25}+{"-"*15}+')
    print(f'|{"Всего":^7s}|{sum_words:^10d}|{sum_bits_fano:^20d}|{sum_bits_haffman:^25d}|{entropy:^15.3f}|')

    print(f'+{"-"*7}+{"-"*10}+{"-"*20}+{"-"*25}+{"-"*15}+')

    return None


def main():
    # Адрес директории расположения файла
    directory = 'D:/.../text_file.txt'

    # Создаём массив входных данных
    input_dict = create_input_array(directory)

    input_array = sorted(filter(lambda val: val != 0, input_dict.values()), reverse=True)

    # chars = sorted(input_dict, key=lambda val: input_dict[val] != 0, reverse=True)
    not_zero_chars = filter(lambda val: input_dict[val] != 0, input_dict)
    chars = {key : input_dict[key] for key in not_zero_chars}
    chars = sorted(chars, key=lambda val:chars[val], reverse=True)

    # print(input_dict)
    # print(list(not_zero_chars))
    # print(chars)
    # print(input_list)

    # Создаем дерево по Фано
    fano_tree = fano_algorithm(input_array)
    # print(fano_tree)

    # Создаем дерево по Хаффману
    haffman_tree = haffman_algorithm(input_array)
    # print(haffman_tree)

    # Обходим деерво Фано
    list_codes_fano = binary_tree_traversal(fano_tree)
    # print(list_codes_fano)

    # Обходим дерево Хаффмана
    list_codes_haffman = binary_tree_traversal(haffman_tree)
    # print(list_codes_haffman)

    # Печатаем выкладку по работе программы
    create_table(chars, input_array, list_codes_fano, list_codes_haffman)

    # Печатаем итог
    create_table_2(input_array, list_codes_fano, list_codes_haffman)

    return None


if __name__ == '__main__':
    # directory = 'D:/ГУАП_предметы/Информатика/lab_7/text_file.txt'

    main()