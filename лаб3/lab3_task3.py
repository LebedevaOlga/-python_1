# TODO  Напишите функцию count_letters
def count_letters(text):
    low_text = text.lower()
    dict_ = {}
    for each_letter in low_text:
        if each_letter.isalpha():
            if each_letter not in dict_:
                letter_counter = low_text.count(each_letter)
                dict_[each_letter] = letter_counter
    return dict_


# TODO Напишите функцию calculate_frequency
def calculate_frequency(any_dict):
    sum_letters = sum(any_dict.values())
    for i, letter_frequency in enumerate(any_dict):
        dict_frequency = any_dict[letter_frequency] / sum_letters
        any_dict[letter_frequency] = dict_frequency
    return any_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result_dict = count_letters(main_str)
result_dict_frequency = calculate_frequency(result_dict)
for i, each_frequency in enumerate(result_dict_frequency):
    print(f"{each_frequency}:{result_dict_frequency[each_frequency]: .2f}")
