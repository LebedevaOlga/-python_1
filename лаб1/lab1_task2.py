CONST = 1024
volume = 1.44
page = 100
str = 50
symbol = 25
weight = 4
print("Количество книг, помещающихся на дискету:", int(volume * CONST * CONST // (page * str * symbol * weight)))
