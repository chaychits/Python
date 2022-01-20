# 1) Создать переменную типа String
a = "Hello"

# 2) Создать переменную типа Integer
b = 15

# 3) Создать переменную типа Float
c = 4.54

# 4) Создать переменную типа Bytes
d = "привет"
e = d.encode(encoding="utf-8")

# 5) Создать переменную типа List
l = ['run','jump','go']

# 6) Создать переменную типа Tuple
t = ('run','jump','go')

# 7) Создать переменную типа Set
s = set('Привет')

# 8. Создать переменную типа Frozen set
fs = frozenset('Привет')

# 9) Создать переменную типа Dict
dict_1 = {}  #создаем пустой словарь
dict_1["country"] = "Minsk"

#
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(a, type(a))
print(b,type(b))
print(c,type(c))
print(e, type(e))
print(l, type(l))
print(t, type(t))
print(s,type(s))
print(fs, type(fs))
print(dict_1['country'], type(dict_1))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
m = 'Mar'
n = 'ina'
print(m + n)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
m = 'Marina'
n = 34
print(m, n)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
m = 'Marina '
n = 34
print(m + str(n))

