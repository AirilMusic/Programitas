import pyperclip
import os
import subprocess
import keyboard

c1 = ("ni", "hi", "hura", "gu", "zu", "zuek", "haiek") #eje y
c2 = ("niri", "hiri", "hari", "guri", "zuri", "zuei", "haiei") #eje x

no = ("nadin", "hadin", "dadin", "gaitezen", "zaitezen", "zaitezten", "daitezen")
ni = ("nendin", "hendin", "zedin", "gintezen", "zintezen", "zintezten", "zitezen")

nno = (("", "nakian/nakinan", "nakion", "", "nakizun", "nakizuen", "nakien"),
       ("hakidan", "", "hakion", "hakigun", "", "", "hakien"),
       ("dakidan", "dakian/dakinan", "dakion", "dakigun", "dakizun", "dakizuen", "dakien"),
       ("", "gakizkian/gakizkinan", "gakizkion", "", "gakizkizun", "gakizkizuen", "gakizkien"),
       ("zakizkidan", "", "zakizkion", "zakizkigun", "", "", "zakizkien"),
       ("zakizkidaten", "", "zakizkioten", "zakizkiguten", "", "", "zakizkieten"),
       ("dakizkidan", "dakizkian/dakizkinan", "dakizkion", "dakizkigun", "dakizkizun", "dakizkizuen", "dakizkien"))
nni = (("", "nenkian/nenkinan", "nenkion", "", "nenkizun", "nenkizuen", "nenkien"),
       ("henkidan", "", "henkion", "henkigun", "", "", "henkien"),
       ("zekidan", "zekian/zekinan", "zekion", "zekigun", "zekizun", "zekizuen", "zekien"),
       ("", "genkizkian/genkizkinan", "genkizkion", "", "genkizkizun", "genkizkizuen", "genkizkien"),
       ("zenkizkidan", "", "zenkizkion", "zenkizkigun", "", "", "zenkizkien"),
       ("zenkizkidaten", "", "zenkizkioten", "zenkizkiguten", "", "", "zenkizkieten"),
       ("zekizkidan", "zekizkian/zekizkinan", "zekizkion", "zekizkigun", "zekizkizun", "zekizkizuen", "zekizkien"))

nnko = (("", "hazadan", "dezadan", "", "zaitzadan", "zaitzatedan", "ditzadan"),
        ("nazaan/nazanan", "", "dezaan/dezanan", "gaitzaan/gaitzanan", "", "", "ditzaan/ditzanan"),
        ("nazan", "hazan", "dezan", "gaitzan", "zaitzan", "zaitzaten", "ditzan"),
        ("", "hazagun", "dezagun", "", "zaitzagun", "zaitzategun", "ditzagun"),
        ("nazazun", "", "dezazun", "gaitzazun", "", "", "ditzazun"),
        ("nazazuen", "", "dezazuen", "gaitzazuen", "", "", "ditzazuen"),
        ("nazaten", "hazaten", "dezaten", "gaitzaten", "zaitzaten", "zaitzateten", "ditzaten"))
nnki = (("", "hintzadan", "nezan", "", "zintzadan", "zintzatedan", "nintzan"),
        ("nintzaan/nintzanan", "", "hezan", "gintzaan/gintzanan", "", "", "hitzan"),
        ("nintzan", "hintzan", "zezan", "gintzan", "zintzan", "zintzaten", "zitzan"),
        ("", "hintzagun", "genezagun", "", "zintzagun", "zintzategun", "genitzan"),
        ("nintzazun", "", "zenezan", "gintzazun", "", "", "zenitzan"),
        ("nintzazuen", "", "zenezaten", "gintzazuen", "", "", "zenitzaten"),
        ("nintzaten", "hintzaten", "zenezaten", "gintzaten", "zintzaten", "zintzateten", "zitzaten"))

nnnos = (("", "diezaadan/diezanadan", "diezaiodan", "", "diezazudan", "diezazuedan", "diezaiedan"),
        ("diezadaan/diezadanan", "", "diezaioan/diezaionan", "diezaguan/diezagunan", "", "", "diezaiean/diezaienan"),
        ("diezadan", "diezaan/diezanan", "diezaion", "diezagun", "diezazun", "diezazuen", "diezaien"),
        ("", "diezaagun/diezanagun", "diezaiogun", "", "diezazugun", "diezazuegun", "diezaiegun"),
        ("diezadazun", "", "diezaiozun", "diezaguzun", "", "", "diezaiezun"),
        ("diezadazuen", "", "diezaiozuen", "diezaguzuen", "", "", "diezaiezuen"),
        ("diezadaten", "diezaaten/diezanaten", "diezaioten", "diezaguten", "diezazuten", "diezazueten", "diezaieten"))
nnnis = (("", "niezaan/niezanan", "niezaion", "", "niezazun", "niezazuen", "niezaien"),
        ("hiezadan", "", "hiezaion", "hiezagun", "", "", "hiezaien"),
        ("ziezadan", "ziezaan/ziezanan", "ziezaion", "ziezagun", "ziezazun", "ziezazuen", "ziezaien"),
        ("", "geniezaan/geniezanan", "geniezaion", "", "geniezazun", "geniezazuen", "geniezaien"),
        ("zeniezadan", "", "zeniezaion", "zeniezagun", "", "", "zeniezaien"),
        ("zeniezadaten", "", "zeniezaioten", "zeniezaguten", "", "", "zeniezaieten"),
        ("ziezadaten", "ziezaaten/ziezanaten", "ziezaioten", "ziezaguten", "ziezazuten", "ziezazueten", "ziezaieten"))

nnnop = (("", "diezazkiadan/diezazkiadanan", "diezazkiodan", "", "diezazkizudan", "diezazkizuedan", "diezazkiedan"),
        ("diezazkian/diezazkinan", "", "diezazkioan/diezazkionan", "diezaizkiguan/diezazkigunan", "", "", "diezazkiean/diezazkienan"),
        ("diezazkidan", "diezazkian/diezazkinan", "diezazkion", "diezazkigun", "diezazkizun", "diezazkizuen", "diezazkien"),
        ("", "diezazkiagun/diezazkinagun", "diezazkiogun", "", "diezazkizugun", "diezazkizuegun", "diezazkiegun"),
        ("diezazkidazun", "", "diezazkiozun", "diezazkiguzun", "", "", "diezazkiezun"),
        ("diezazkidazuen", "", "diezazkiozuen", "diezazkiguzuen", "", "", "diezazkiezuen"),
        ("diezazkidaten", "diezazkiaten/diezazkinaten", "diezazkioten", "diezazkiguten", "diezazkizuten", "diezazkizueten", "diezazkieten"))
nnnip = (("", "niezazkian/ziezanaten", "niezazkion", "", "niezazkizun", "niezazkizuen", "niezazkien"),
        ("hiezazkidan", "", "hiezazkion", "hiezazkigun", "", "", "hiezazkien"),
        ("ziezazkidan", "ziezazkian/ziezazkinan", "ziezazkion", "ziezazkigun", "ziezazkizun", "ziezazkizuen", "ziezazkien"),
        ("", "geniezazkian", "geniezazkinan", "geniezazkion", "", "geniezazkizun", "geniezazkizuen", "geniezazkien"),
        ("zeniezazkidan", "", "zeniezazkion", "zeniezazkigun", "", "", "zeniezazkien"),
        ("zeniezazkidaten", "", "zeniezazkioten", "zeniezazkiguten", "", "", "zeniezazkieten"),
        ("ziezazkidaten", "ziezazkiaten/ziezazkinaten", "ziezazkioten", "ziezazkiguten", "ziezazkizuten", "ziezazkizueten", "ziezazkieten"))

def update():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Obteniendo lista de actualizaciones...\n"
      "Leyendo lista de paquetes...\n"
      "Generando árbol de dependencias...\n"
      "Leyendo estado de paquetes...\n"
      "Calculando la actualización...\n\n"
      "Los siguientes paquetes serán actualizados:\n"
      "  foo (1.0 => 1.1)\n"
      "  bar (2.3 => 2.4)\n"
      "  baz (4.5 => 4.6)\n"
      "  qux (0.9 => 1.0)\n"
      "...\n"
      "...\n"
      "...\n\n"
      "Algo salió mal, buscando una solución, por favor no cierre esta pestaña...")

while True:
    update()
    try:
        #denbora = input("Denbora (Orainaldia/O, Iragana/I): ").lower()
        #mota = input("Mota (Nor/N, Nor Nori/NN, Nor Nork/NNK, Nor Nori Nork/NNN): ").lower()
        denbora = input().lower()
        update()
        pyperclip.copy("..")
        mota = input().lower()
        update()
        pyperclip.copy(".")
        
        if mota == "nor" or mota == "n":
            if denbora == "orainaldia" or denbora == "o":
                #pertsona = input("Pertsona: ").lower()
                pertsona = input().lower()
                if pertsona in c1:
                    print(no[c1.index(pertsona)])
                    pyperclip.copy(no[c1.index(pertsona)])
            
            elif denbora == "iragana" or denbora == "i":
                #pertsona = input("Pertsona: ").lower()
                pertsona = input().lower()
                if pertsona in c1:
                    print(ni[c1.index(pertsona)])
                    pyperclip.copy(ni[c1.index(pertsona)])
        
        elif mota == "nor nori" or mota == "nn":
            if denbora == "orainaldia" or denbora == "o":
                #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                pertsona1, pertsona2 = list((input().lower()).split())
                if pertsona1 in c1 and pertsona2 in c2:
                    print(nno[c1.index(pertsona1)][c2.index(pertsona2)])
                    pyperclip.copy(nno[c1.index(pertsona1)][c2.index(pertsona2)])
            
            elif denbora == "iragana" or denbora == "i":
                #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                pertsona1, pertsona2 = list((input().lower()).split())
                if pertsona1 in c1 and pertsona2 in c2:
                    print(nni[c1.index(pertsona1)][c2.index(pertsona2)])
                    pyperclip.copy(nni[c1.index(pertsona1)][c2.index(pertsona2)])
        
        elif mota == "nor nork" or mota == "nnk":
            if denbora == "orainaldia" or denbora == "o":
                #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                pertsona1, pertsona2 = list((input().lower()).split())
                if pertsona1 in c1 and pertsona2 in c2:
                    print(nnko[c1.index(pertsona1)][c2.index(pertsona2)])
                    pyperclip.copy(nnko[c1.index(pertsona1)][c2.index(pertsona2)])
            
            elif denbora == "iragana" or denbora == "i":
                #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                pertsona1, pertsona2 = list((input().lower()).split())
                if pertsona1 in c1 and pertsona2 in c2:
                    print(nnki[c1.index(pertsona1)][c2.index(pertsona2)])
                    pyperclip.copy(nnki[c1.index(pertsona1)][c2.index(pertsona2)])
        
        elif mota == "nor nori nork" or mota == "nnn":
            update()
            pyperclip.copy("..")
            if denbora == "orainaldia" or denbora == "o":
                #p = input("Singularra(S)/Plurala(P): ").lower()
                p = input().lower()
                update()
                pyperclip.copy(".")
                if p == "singularra" or p == "s":
                    #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                    pertsona1, pertsona2 = list((input().lower()).split())
                    if pertsona1 in c1 and pertsona2 in c2:
                        print(nnnos[c1.index(pertsona1)][c2.index(pertsona2)])
                        pyperclip.copy(nnnos[c1.index(pertsona1)][c2.index(pertsona2)])
                else:
                    #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                    pertsona1, pertsona2 = list((input().lower()).split())
                    if pertsona1 in c1 and pertsona2 in c2:
                        print(nnnop[c1.index(pertsona1)][c2.index(pertsona2)])
                        pyperclip.copy(nnnop[c1.index(pertsona1)][c2.index(pertsona2)])
                    
            elif denbora == "iragana" or denbora == "i":
                #p = input("Singularra(S)/Plurala(P): ").lower()
                p = input().lower()
                if p == "singularra" or p == "s":
                    #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                    pertsona1, pertsona2 = list((input().lower()).split())
                    if pertsona1 in c1 and pertsona2 in c2:
                        print(nnnis[c1.index(pertsona1)][c2.index(pertsona2)])
                        pyperclip.copy(nnnis[c1.index(pertsona1)][c2.index(pertsona2)])
                else:
                    #pertsona1, pertsona2 = list((input("Pertsonak: ").lower()).split())
                    pertsona1, pertsona2 = list((input().lower()).split())
                    if pertsona1 in c1 and pertsona2 in c2:
                        print(nnnip[c1.index(pertsona1)][c2.index(pertsona2)])
                        pyperclip.copy(nnnip[c1.index(pertsona1)][c2.index(pertsona2)])
        
        if pyperclip.paste() == "." or pyperclip.paste() == ".." or pyperclip.paste() == "...":
            pyperclip.copy("....")
        #t = input("[+] Press Enter to continue")
    except:
        pass
