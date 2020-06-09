m = "masa madre"
h = "harina"
s = "sal"
a = "agua"
av = "agua para viga"
ac = "aceite"
le = "levadura en polvo"
pi = "pizza"
pa = "pan"
fo = "focaccia"
vi = "viga"

def Calcmm():
    maspi1 = int(input("Ingrese la cantidad de mass madre que vas a utilizar para hacer esta pizza:"))
    harpi1 = ((100 * maspi1) / masam)
    salpi1 = ((2.5 * harpi1) / 100)
    agupi1 = ((agua * harpi1) / 100)
    acepi1 = ((2.5 * harpi1) / 100)
    print("vas a necesitar: \n",
          maspi1, "gr de masa madre\n",
          harpi1, "gr de Harina\n",
          salpi1, "gr de Sal\n",
          agupi1, "gr de Agua\n",
          acepi1, "gr de Aceite"
          )

def Calcha():
    harpi2 = int(input("Ingrese la cantidad de harina que vas a utilizar para hacer esta pizza: "))
    salpi2 = ((2.5 * harpi2) / 100)
    maspi2 = ((masam * harpi2) / 100)
    agupi2 = ((agua * harpi2) / 100)
    acepi2 = ((2.5 * harpi2) / 100)
    print("vas a necesitar: \n",
          maspi2, "gr de masa madre\n",
          harpi2, "gr de Harina\n",
          salpi2, "gr de Sal\n",
          agupi2, "gr de Agua\n",
          acepi2, "gr de Aceite"
          )

def Calcsa():
    salpi3 = int(input("Ingrese la cantidad de sal que vas a utilizar para hacer esta pizza: "))
    harpi3 = ((100 * salpi3) / 2.5)
    maspi3 = ((masam * harpi3) / 100)
    agupi3 = ((agua * harpi3) / 100)
    acepi3 = ((2.5 * harpi3) / 100)
    print("vas a necesitar: \n",
          maspi3, "gr de masa madre\n",
          harpi3, "gr de Harina\n",
          salpi3, "gr de Sal\n",
          agupi3, "gr de Agua\n",
          acepi3, "gr de Aceite"
          )

def Calcag():
    agupi4 = int(input("Ingrese la cantidad de agua que vas a utilizar para hacer esta pizza: "))
    harpi4 = ((100 * agupi4) / agua)
    maspi4 = ((masam * harpi4) / 100)
    salpi4 = ((2.5 * harpi4) / 100)
    acepi4 = ((2.5 * harpi4) / 100)
    print("vas a necesitar: \n",
          maspi4, "gr de masa madre\n",
          harpi4, "gr de Harina\n",
          salpi4, "gr de Sal\n",
          agupi4, "gr de Agua\n",
          acepi4, "gr de Aceite"
          )

def Calcac():
    acepi5 = int(input("Ingrese la cantidad de aceite que vas a utilizar para hacer esta pizza: "))
    harpi5 = ((100 * acepi5) / 2.5)
    maspi5 = ((masam * harpi5) / 100)
    salpi5 = ((2.5 * harpi5) / 100)
    agupi5 = ((agua * harpi5) / 100)
    print("vas a necesitar: \n",
          maspi5, "gr de masa madre\n",
          harpi5, "gr de Harina\n",
          salpi5, "gr de Sal\n",
          agupi5, "gr de Agua\n",
          acepi5, "gr de Aceite"
          )
    




print("vamos a hacer una masa de pan, pizza o focaccia con masa madre.")
print("Que masa queres hacer hoy?: \n1.",pi,"\n2.",pa,"\n3.",fo,"\n4.",vi)
masa = int(input("Que masa queres hacer hoy?(pon el numero de masa):"))

#agua = int(input("Con que porcentaje de hidratacion queres hacer la masa?: "))
if masa == 1:
    agua = int(input("Con que porcentaje de hidratacion queres hacer la masa?: "))
    masam= int(input("con que porcentaje de masa madre queres hacer la masa: "))
    print("Genial, vamos a hacer una pizza! con ",agua,"% de hidratacion y con un ",masam, "% de masa madre).")
    print("vamos a necesitar los siguientes ingredientes:"
          "\nHarina"
          "\nAgua"
          "\nAceite"
          "\nSal"
          "\nMasa madre")
    print("Quieres calcular los ingredientes en base a: \n1.", m, "\n2.", h, "\n3.", s, "\n4.", a, "\n5.", ac)
    i = input("Ingresa el numero del ingrediente: ")
    i = int(i)
    # ----------- calculo de pizza con la masa madre --------------------------
    if i == 1:
        print("Has seleccionado hacer el calculo con la: ", m)
        Calcmm()
    # ----------- calculo de pizza con la harina --------------------------
    elif i == 2:
        print("Has seleccionado hacer el calculo con la: ", h)
        Calcha()

    # ----------- calculo de pizza con la sal --------------------------

    elif i == 3:
        print("Has seleccionado hacer el calculo con la: ", s)
        Calcsa()

    # ----------- calculo de pizza con el agua --------------------------

    elif i == 4:
        print("Has seleccionado hacer el calculo con el: ", a)
        Calcag()

    # ----------- calculo de pizza con el aceite --------------------------

    elif i == 5:
        print("Has seleccionado hacer el calculo con el: ", ac)
        Calcac()

# -------------- calculo de pan -----------------------------------------
elif masa == 2:
    agua = int(input("Con que porcentaje de hidratacion queres hacer la masa?: "))
    print("Genial, vamos a hacer una pan! con ", agua, "% de hidratacion (20% de masa madre).")
    print("Vamos a necesitar los siguientes ingredientes:"
          "\nHarina"
          "\nAgua"
          "\nMasa madre"
          "\nSal")
    print("Quieres calcular los ingredientes en base a: \n1.", m, "\n2.", h, "\n3.", s, "\n4.", a)
    i = input("Ingresa el numero del ingrediente: ")
    i = int(i)

    # -------------- calculo de pan con la masa madre ---------------------

    if i == 1:
        print("Has seleccionado hacer el calculo con la: ", m)
        maspa1 = int(input("Ingrese la cantidad de masa madre: "))
        harpa1 = ((100 * maspa1) / 20)
        salpa1 = ((2 * harpa1) / 100)
        agupa1 = ((agua * harpa1) / 100)
        print("vas a necesitar: \n",
              maspa1, "gr de masa madre\n",
              harpa1, "gr de Harina\n",
              salpa1, "gr de sal\n",
              agupa1, "gr de Agua\n"
              )

    # -------------- calculo de pan con la harina ---------------------

    elif i == 2:
        print("Has seleccionado hacer el calculo con la: ", h)
        harpa2 = int(input("Ingrese la cantidad de harina: "))
        maspa2 = ((20 * harpa2) / 100)
        salpa2 = ((2 * harpa2) / 100)
        agupa2 = ((agua * harpa2) / 100)
        print("vas a necesitar: \n",
              maspa2, "gr de masa madre\n",
              harpa2, "gr de Harina\n",
              salpa2, "gr de sal\n",
              agupa2, "gr de Agua\n"
              )

    # -------------- calculo de pan con la sal ---------------------

    elif i == 3:
        print("Has seleccionado hacer el calculo con la: ", s)
        salpa3 = int(input("Ingrese la cantidad de sal: "))
        harpa3 = ((100 * salpa3) / 2)
        maspa3 = ((20 * harpa3) / 100)
        agupa3 = ((agua * harpa3) / 100)
        print("vas a necesitar: \n",
              maspa3, "gr de masa madre\n",
              harpa3, "gr de Harina\n",
              salpa3, "gr de sal\n",
              agupa3, "gr de Agua\n"
              )

    # -------------- calculo de pan con el agua ---------------------

    elif i == 4:
        print("Has seleccionado hacer el calculo con el: ", a)
        agupa4 = int(input("Ingrese la cantidad de agua: "))
        harpa4 = ((100 * agupa4) / agua)
        maspa4 = ((20 * harpa4) / 100)
        salpa4 = ((2 * harpa4) / 100)
        print("vas a necesitar: \n",
              maspa4, "gr de masa madre\n",
              harpa4, "gr de Harina\n",
              salpa4, "gr de sal\n",
              agupa4, "gr de Agua\n"
              )

#----------------- calculo de la focaccia ---------------------------
if masa == 3:
    agua = int(input("Con que porcentaje de hidratacion queres hacer la masa?: "))
    print("Genial!, vamos a hacer una focaccia! con ",agua,"% de hidratacion.")
    print("vamos a necesitar los siguientes ingredientes:"
          "\nHarina"
          "\nAgua"
          "\nAceite"
          "\nSal"
          "\nMasa madre")
    print("Quieres calcular los ingredientes en base a: \n1.", m, "\n2.", h, "\n3.", s, "\n4.", a, "\n5.", ac)
    i = input("Ingresa el numero del ingrediente: ")
    i = int(i)
    # ----------- calculo de focaccia con la masa madre --------------------------
    if i == 1:
        print("Has seleccionado hacer el calculo con la: ", m)
        masfo1 = int(input("Ingrese la cantidad de masa madre que vas a utilizar para hacer esta pizza:"))
        harfo1 = ((100 * masfo1) / 25)
        salfo1 = ((2.5 * harfo1) / 100)
        agufo1 = ((agua * harfo1) / 100)
        acefo1 = ((2.5 * harfo1) / 100)
        print("vas a necesitar: \n",
              masfo1, "gr de masa madre\n",
              harfo1, "gr de Harina\n",
              salfo1, "gr de Sal\n",
              agufo1, "gr de Agua\n",
              acefo1, "gr de Aceite"
              )
    # ----------- calculo de focaccia con la harina --------------------------
    elif i == 2:
        print("Has seleccionado hacer el calculo con la: ", h)
        harfo2 = int(input("Ingrese la cantidad de harina que vas a utilizar para hacer esta pizza: "))
        salfo2 = ((2.5*harfo2)/100)
        masfo2 = ((25 * harfo2) / 100)
        agufo2 = ((agua * harfo2) / 100)
        acefo2 = ((2.5 * harfo2) / 100)
        print("vas a necesitar: \n",
              masfo2, "gr de masa madre\n",
              harfo2, "gr de Harina\n",
              salfo2, "gr de Sal\n",
              agufo2, "gr de Agua\n",
              acefo2, "gr de Aceite"
              )

    # ----------- calculo de focaccia con la sal --------------------------

    elif i == 3:
        print("Has seleccionado hacer el calculo con la: ", s)
        salfo3 = int(input("Ingrese la cantidad de sal que vas a utilizar para hacer esta pizza: "))
        harfo3 = ((100 * salfo3) / 2.5)
        masfo3 = ((25 * harfo3) / 100)
        agufo3 = ((agua * harfo3) / 100)
        acefo3 = ((2.5 * harfo3) / 100)
        print("vas a necesitar: \n",
              masfo3, "gr de masa madre\n",
              harfo3, "gr de Harina\n",
              salfo3, "gr de Sal\n",
              agufo3, "gr de Agua\n",
              acefo3, "gr de Aceite"
              )

    # ----------- calculo de focaccia con el agua --------------------------

    elif i == 4:
        print("Has seleccionado hacer el calculo con el: ", a)
        agufo4 = int(input("Ingrese la cantidad de agua que vas a utilizar para hacer esta pizza: "))
        harfo4 = ((100 * agufo4) / agua)
        masfo4 = ((25 * harfo4) / 100)
        salfo4 = ((2.5 * harfo4) / 100)
        acefo4 = ((2.5 * harfo4) / 100)
        print("vas a necesitar: \n",
              masfo4, "gr de masa madre\n",
              harfo4, "gr de Harina\n",
              salfo4, "gr de Sal\n",
              agufo4, "gr de Agua\n",
              acefo4, "gr de Aceite"
              )

    # ----------- calculo de pizza con el aceite --------------------------

    elif i == 5:
        print("Has seleccionado hacer el calculo con el: ", ac)
        acefo5 = int(input("Ingrese la cantidad de aceite que vas a utilizar para hacer esta pizza: "))
        harfo5 = ((100 * acefo5) / 2.5)
        masfo5 = ((25 * harfo5) / 100)
        salfo5 = ((2.5 * harfo5) / 100)
        agufo5 = ((2.5 * harfo5) / 100)
        print("vas a necesitar: \n",
              masfo5, "gr de masa madre\n",
              harfo5, "gr de Harina\n",
              salfo5, "gr de Sal\n",
              agufo5, "gr de Agua\n",
              acefo5, "gr de Aceite"
              )

# ---------------calculo para la viga -------------------------------------
elif masa == 4:
    print("Genial, vamos a hacer una viga! con. La viga la preparamos con un 50% de hidratacion y un 2% de 0,5% de levadura. ")
    print("Vamos a necesitar los siguientes ingredientes:"
          "\nHarina"
          "\nAgua"
          "\nLevadura en polvo"
          )
    print("Quieres calcular los ingredientes en base a: \n1.", h, "\n2.", av, "\n3.", le)
    i = input("Ingresa el numero del ingrediente: ")
    i = int(i)

    #-------------------- calculo de viga con harina -------------------------

    if i == 1:
        print("Has seleccionado hacer el calculo con el: ", h)
        harvi1 = int(input("Ingrese la cantidad de harina que vas a utilizar: "))
        aguvi1 = ((50 * harvi1) / 100)
        levvi1 = ((0.4 * harvi1) / 100)
        print("vas a necesitar: \n",
              harvi1, "gr de Harina\n",
              aguvi1, "gr de Agua\n",
              levvi1, "gr de Levadura\n"
              )

    # -------------------- calculo de viga con agua -------------------------

    if i == 2:
        print("Has seleccionado hacer el calculo con el: ", av)
        aguvi2 = int(input("Ingrese la cantidad de agua que vas a utilizar: "))
        harvi2 = ((100 * aguvi2) / 50)
        levvi1 = ((0.4 * harvi2) / 100)
        print("vas a necesitar: \n",
              harvi2, "gr de Harina\n",
              aguvi2, "gr de Agua\n",
              levvi2, "gr de Levadura\n"
              )

    # -------------------- calculo de viga con agua -------------------------

    if i == 3:
        print("Has seleccionado hacer el calculo con la: ", le)
        levvi3 = int(input("Ingrese la cantidad de levadura que vas a utilizar: "))
        harvi3 = ((100 * levvi3) / 0.4)
        aguvi3 = ((50 * harvi3) / 100)
        print("vas a necesitar: \n",
              harvi3, "gr de Harina\n",
              aguvi3, "gr de Agua\n",
              levvi3, "gr de Levadura\n"
              )
