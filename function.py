# >>>Victor Andres Barilin<<<

def grouper(n, iterable):
    grouped_list = []
    i = 0

    while i <= len(iterable):
        grouped_list.append(iterable[i:i+3])
        i += 3
        
    return grouped_list

def clear_number(number):
    number = number.strip()
    posi = 1

    if len(number) > 1:
        while posi != -1:
            posi = number.find('0')
            if posi == 0:
                number = number[posi+1:]
            else:
                posi = -1

    number = number.strip()

    try:
        int(number)
        return number

    except:
        return 'El valor ingresado no es un entero.'

def formulate(text):
    text = text[::-1]
    answer = ''

    for i in text:
        answer = answer + i

    answer = answer.strip()
    return answer
    
names = {
        'simples': ['cero', 'uno ','dos ','tres ','cuatro ','cinco ','seis ','siete ','ocho ','nueve '],

        'doble-10': ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve'],

        'doble': ['veinti', 'treinta', 'cuarenta', 'cincuenta', 'secenta', 'setenta', 'ochenta', 'noventa'],

        'triple': ['cien', 'doscientos ', 'trescientos ', 'cuatrocientos ', 'quinientos ', 'seiscientos ', 'setecientos ', 'ochocientos ', 'novecientos '],

        'quintuples':['millones ', 'billones ', 'trillones ', 'cuatrillones ', 'quintillones ', 'sextillones ']
    }