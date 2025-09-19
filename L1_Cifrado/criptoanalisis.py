import string

letras = ["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]
texto = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXVITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."

def calcular_frecuencia(texto):
    freq = {}
    for letra in string.ascii_uppercase:
        freq[letra] = texto.count(letra)
    return freq

def sustitucionAutomatica(freq, letras):
    freq_copy = freq.copy()
    clave = {}
    for letra in string.ascii_uppercase:
        letra_mas_frecuente = max(freq_copy, key=freq_copy.get)
        if freq_copy[letra_mas_frecuente] <= 0:
            break
        clave[letra_mas_frecuente] = letra
        freq_copy[letra_mas_frecuente] = -1
    return clave

def sustituir(texto: str, clave):
    nuevo_texto = ""
    for char in texto:
        if char in clave:
            nuevo_texto += clave.get(char, char)
        else:
            nuevo_texto += char
    return nuevo_texto

def sustitucionManual(texto, clave):
    while True:
        letra = input("\n¿Qué letra quieres cambiar del texto? (Pon STOP para dejar de cambiar) ").upper()
        if letra == "STOP":
            break
        if letra not in string.ascii_uppercase:
            print("Por favor, ingresa una letra válida.")
            continue
        letraNew = input("\n¿Por qué letra la quieres cambiar? ").lower()
        clave[letra] = letraNew
        texto = sustituir(texto, clave)

        print("\nTexto actualizado:")
        print(texto)
        print("\nLa clave es:")
        print(clave)
    return texto, clave

def printClave(clave):
    res = ""
    for letra in string.ascii_uppercase:
        res = res + letra + ": " + str(clave.get(letra)) + "; "
    return res

# Ejecución
freq = calcular_frecuencia(texto)
clave = sustitucionAutomatica(freq, letras)
texto_sustituido = sustituir(texto, clave)

print("\nTexto sustituido automáticamente:")
print(texto_sustituido)
print("\nClave inicial:")
print(printClave(clave))