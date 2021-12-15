

# Реализуем подсчёт количества каждого символов в некотором текстовом докуметне.

def create_input_array(directory_txt_file):
    chars = ' ' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    chars += chars.upper()

    input_dict = {key : 0 for key in chars}

    with open(directory_txt_file, 'r', encoding='utf-8') as file:
        while file.read(1):
            char = file.read(1)

            if char in input_dict.keys():
                input_dict[char] = input_dict[char] + 1

    return input_dict


if __name__ == '__main__':
    directory = 'D:/ГУАП_предметы/Информатика/lab_7/text_file.txt'

    input_dict = create_input_array(directory)

    print(input_dict)