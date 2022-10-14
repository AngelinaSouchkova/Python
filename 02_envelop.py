
# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
# paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
paper_x, paper_y = 6, 8


envelop_sqare = envelop_x * envelop_y
paper_sqare = paper_x * paper_y

if envelop_sqare > paper_sqare :
    print("Yes")
else: print("No")
