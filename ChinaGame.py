gamer1 = input("Игрок А введите имя: ")
gamer2 = input("Игрок Б введите имя: ")
listOfGamers = [gamer1, gamer2]
stiks = 10

def choiseGamer(numb):
    while(numb > 0):
        for i in listOfGamers:
            if numb > 0:
                print(f'Осталось {numb} палочек')
                answerGamer = int(input(f'{i} выбери от 1 до 3 палочек: '))
                if answerGamer < 1 or answerGamer > 3:
                    print(f'Вы ввели {answerGamer}, а надо от 1 до 3. Пропускаете ход')
                    continue
                else:
                    numb = numb-answerGamer
            else:
                return i

        if numb <= 0:
            results(i)

def results(person):
    print(f'{person} ты победил!')
 
choiseGamer(stiks)