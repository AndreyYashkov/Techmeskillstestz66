spisok = ["Пустой Список"]
slovar = dict()


def add_todo():
    vvodimkolzadach = int(input("""
    ______________________________________
    Сколько задач хотите добавить?
    Для возврата в главное меню введите 0
    ______________________________________

    Число: """))
    if vvodimkolzadach != int(vvodimkolzadach):
        print('Введите число:', vvodimkolzadach)

    if vvodimkolzadach == 0:
        menu()

    i = 0
    while i < vvodimkolzadach:
        b = input('Напишите задачу: ')
        spisok.append(b)
        i += 1

    #show_todos(spisok)
    menu()


def del_todo(spisok):
    dada = show_todos(spisok)
    if len(spisok) == 1:
        menu()
    else:
        deletim = int(input("""
    ____________________

    Введите номер задач на удаление:

    ____________________
    Число :"""))
        spisok.pop(deletim)
        b = input('Вернуться в меню? y/n : ')
        if b == "y":
            menu()
        else:
            del_todo()




def show_todos(spisok):
    if len(spisok) == 1:
        print("""
        __________________

          Задач пока нет

        __________________
        """)
    else:
        for num, zadacha in enumerate(spisok[1::], 1):
            #slovar[num] = zadacha
            print(f'{num}: {zadacha}, состояние выполнения: Не выполнено [В разработке]')
        #return slovar



def menu():
    i = 1
    print("""
______________________________    

    1. DOBAVIT_ZADACHU
    2. UDALIT_ZADACHU
    3. POKAZAT_VSE_ZADACHI
    4. EXIT

______________________________
    """)
    a = int(input("VVEDITE_NOMER : "))

    while a != 4:
        global spisok

        if a == 1:
            add_todo()

        if a == 2:
            del_todo(spisok)

        if a == 3:

            show_todos(spisok)
            b = input('Вернуться в меню? y/n : ')
            if b == "y":
                menu()
            else:
                print(' Всего доброго, офаем ')
                break
        break


menu()