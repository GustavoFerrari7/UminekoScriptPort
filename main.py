
import re
from difflib import SequenceMatcher
import time
import fileinput

if __name__ == '__main__':
    indexnum = 0
    def testefun(aqui):
        #print(aqui)
        global indexnum
        global mudado
        if "langen" in aqui:
            best = 0
            maybe = 0
            maybebest = ""
            maybetranslation = ""
            wordbest = ""
            mudado = None
            cond = None
            mudado = aqui
            texto = re.findall("\^(.*?)\^", aqui)
            for i in range(len(texto)):
                best = 0
                passed = None
                for j in range (num_lines):
                    s = SequenceMatcher(None, texto[i].replace('\n', ''), scriptlinesEN[j].replace('\n', ''))
                    #print(texto[i] + scriptlinesEN[j] + str(s.ratio()))
                    if s.ratio() > maybe:
                        maybe = s.ratio()
                        maybebest = scriptlinesEN[j]
                        maybetranslation = scriptlines[j]
                    if s.ratio() > 0.85 and s.ratio() > best:
                        best = s.ratio()
                        mudado = mudado.replace(texto[i], scriptlines[j].replace('\n', ''))
                        cond = "aeooo"
                        passed = "yes"
                        print(mudado)
                if passed == None:
                    print("Original: " + texto[i])
                    print("Script EN: " + maybebest)
                    print("Script PT: " + maybetranslation)
                    manual = input("Frase: ")
                    if manual == "y":
                        mudado = mudado.replace(texto[i], maybetranslation.replace('\n', ''))
                    else:
                        mudado = mudado.replace(texto[i], manual.replace('\n', ''))
                    cond = "aeooo"
            if cond != None:
                g.write(mudado)
            else:
                g.write(aqui)
        else:
            g.write(aqui)



    f = open(r"C:\Users\gusta\Desktop\teste.u", "r", encoding="utf-8")
    lines = f.readlines()
    g = open("myfile.u", "w", encoding="utf-8")
    script = open("script.txt", "r", encoding="utf-8")
    scriptlines = script.readlines()
    scriptEN = open("scripten.txt", "r", encoding="utf-8")
    scriptlinesEN = scriptEN.readlines()
    num_lines = sum(1 for line in scriptlinesEN)

    for line in lines:
        testefun(line)
