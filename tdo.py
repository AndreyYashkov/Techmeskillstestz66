spisok = ["Пустой Список"]
slovar = dict()
slovar2 = dict()

def dekor(funk):
    def wraper(*args, **kwargs):
        print('test')
        funk(*args, **kwargs)
        menu()

    return wraper
@dekor
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
        pass
        #menu()

    i = 0
    while i < vvodimkolzadach:
        b = input('Напишите задачу: ')
        #spisok.append(b)
        slovar2[b] = 'не выполнена'
        i += 1
        
    print(slovar2)
    #show_todos(spisok)
    #menu()


def del_todo(slovar2):
    show_todos(slovar2)

    if len(slovar2) == 0:
        menu()
    else:
        deletim = int(input("""
    ____________________

    Введите номер задач на удаление:

    ____________________
    Число :"""))
        chitaem = 1
        for z in slovar2.keys():
            if chitaem == deletim:
                slovar2.pop(z)
                break
            chitaem+=1

        b = input('Вернуться в меню? y/n : ')
        if b == "y":
            menu()
        else:
            del_todo()




def show_todos(slovar2): #был spisok
    if len(slovar2) == 0:
        print("""
        __________________

          Задач пока нет

        __________________
        """)

    else:
        count = 1
        for i in slovar2.keys():

            #str(i)
            aa = slovar2[i]

            print(f'{count} {i}  состояние: {aa}')
            count+=1
#       for num, zadacha in enumerate(spisok[1::], 1):
#           slovar[num] = zadacha
#           print(f'{num}: {zadacha}, состояние выполнения: Не выполнено [В разработке]')
#       #return slovar
@dekor
def ready_todos(slovar2):
    show_todos(slovar2)
    if len(slovar2) == 0:
       menu()
    else:
       nmr = (input("""
       _________________________________
       Введите номер выполненной задачи,
       либо ввеите all для выполнения всех
       ___________________________________
       """))
       if nmr == 'all':
           for i in slovar2.keys():
               slovar2[i] = "ВЫПОЛНЕНО"
           menu()
       else:
            nmr=int(nmr)
            schet = 1
            for c in slovar2.keys():
                 if nmr == schet:
                    slovar2[c] = "ВЫПОЛНЕНО"
                 schet +=1
       show_todos(slovar2)




@dekor
def sorted_todos(slovar2):
    d = dict(sorted(slovar2.items(), key=lambda x: x[1]))
    for i in slovar2.items():
        if i[1] == 'ВЫПОЛНЕНО':
            print(i)





def prodolzaem():
     b = input('Вернуться в меню? y/n : ')
     if b == "y":
         menu()
     else:
         print(' Всего доброго, офаем ')







def menu():
    i = 1
    print("""
______________________________    

    1. DOBAVIT_ZADACHU
    2. UDALIT_ZADACHU
    3. POKAZAT_VSE_ZADACHI
    4. VIPOLNUT_ZADACHU
    5. POKAZAT_VIPOLNENNIE
    0. EXIT

______________________________
    """)
    a = int(input("VVEDITE_NOMER : "))

    while a != 0:
        global spisok

        if a == 1:
            add_todo()

        if a == 2:
            del_todo(slovar2)

        if a == 3:
            show_todos(slovar2)
            prodolzaem()

        if a == 4:
            ready_todos(slovar2)

        if a == 5:
            sorted_todos(slovar2)


        break


menu()