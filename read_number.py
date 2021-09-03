# >>>Victor Andres Barilin<<<

from function import *

def read_number(number):
    number = clear_number(number)

    number_reverse = number[::-1]
    grup = grouper(3, number_reverse)
    text = []
    laps = 0
    mil = False

    for x in range(len(grup)):

        if  len(grup)-1 == x:
            resto = None
        else:
            resto = grup[x + 1]

        try:
            resto_mil = grup[x + 2]
        except:
            resto_mil = None


        c = 1
        double= False
        for i in range(len(grup[x])):
            if  len(grup[x])-1 == i:
                forthcoming = None
            else:
                forthcoming = grup[x][i + 1]

            if c == 1:
                if  forthcoming == '1':
                    text.append(names['doble-10'][int(grup[x][i])])
                    double= True

                elif grup[x][i] == '0':
                    if  forthcoming == None:
                        text.append(names['simples'][int(grup[x][i])])

                else:
                    if grup[x][i] != '1':
                        text.append(names['simples'][int(grup[x][i])])

                    elif grup[x][i] == '1' and len(text) == 0:
                        text.append(names['simples'][int(grup[x][i])]) 

            if c == 2 and double== False:
                if  grup[x][i] != '0':
                    if grup[x][i] == '2': 
                        if grup[x][i-1] == '0':
                            text.append('veinte ')
                        else:
                            text.append(names['doble'][int(grup[x][i])-2])

                    else:
                        if grup[x][i-1] == '0':
                            text.append(names['doble'][int(grup[x][i])-2])

                        else:
                            text.append(names['doble'][int(grup[x][i])-2] + ' y ')

            if c == 3 :
                if  grup[x][i] != '0':
                    if grup[x][i-1] == '0' and grup[x][i-2] == '0':
                        text.append((names['triple'][int(grup[x][i])-1]))

                    elif grup[x][i] == '1':
                        text.append(names['triple'][int(grup[x][i])-1] + 'to ')

                    else:
                        text.append(names['triple'][int(grup[x][i])-1])

                double= False

            c += 1

        if  resto and mil == False:
            if resto != '000':
                text.append('mil ')
                mil = True  
            else:
                mil = True          
        elif resto and mil == True :
            if resto != '000' or (resto =='000' and resto_mil != '000'):
                if resto == '1':
                    text.append(('un' + names['quintuples'][laps][:-3] + ' '))
                    laps += 1
                    mil = False
                    
                else:
                    text.append(names['quintuples'][laps])
                    laps += 1
                    mil = False
            else:
                mil = False
                laps += 1

    answer = formulate(text)
    return answer
