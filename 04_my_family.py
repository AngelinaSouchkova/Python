# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Vadim', 192],
    ['Sweta', 164],
    ['Sasha', 176],
    ['Angelina', 172],
]
dad_height = my_family_height[0]
mom_height = my_family_height[1]
brother_height = my_family_height[2]
my_height = my_family_height[3]
print('Рост отца - ', dad_height[1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum = dad_height[1] + mom_height[1] + brother_height[1] + my_height[1]

print(sum, 'см')