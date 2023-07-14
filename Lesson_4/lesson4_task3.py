# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def make_dict(str_input:str):
    beg,end=sorted(str_input.split())
    # dict={ord(x):x for x in range(int(beg),int(end))}
    # return dict
    return {ord(str(x)):x for x in range(int(beg),int(end)+1)}

print(make_dict('7 3'))
