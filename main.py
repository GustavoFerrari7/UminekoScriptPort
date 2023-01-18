
import re
from difflib import SequenceMatcher
import time
import fileinput

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    indexnum = 0
    def testefun(aqui):
        #print(aqui)
        global indexnum
        global mudado
        if "langen" in aqui:
            best = 0
            wordbest = ""
            mudado = None
            cond = None
            mudado = aqui
            texto = re.findall("\^(.*?)\^", aqui)
            for i in range(len(texto)):
                for j in range (num_lines):
                    s = SequenceMatcher(None, texto[i].replace('\n', ''), scriptlinesEN[j].replace('\n', ''))
                    #print(texto[i] + scriptlinesEN[j] + str(s.ratio()))
                    if s.ratio() > 0.85 and s.ratio() > best:
                        best = s.ratio()
                        #print(i)
                        #print(j)
                        #print(texto[i])
                        #wordbest = texto[i]
                        #print(scriptlinesEN[j])
                        mudado = mudado.replace(texto[i], scriptlines[j].replace('\n', ''))
                        best = 0
                        cond = "aeooo"
                        print(mudado)
                #print(texto[i])
                #print(wordbest)
                #print(scriptlines[indexnum])
                indexnum = indexnum + 1
            if cond != None:
                #print(mudado)
                g.write(mudado)
                #pass
            else:
                g.write(aqui)
                #pass
        else:
            g.write(aqui)
            #pass
        #print(b)
        #teste123 = aqui.replace(texto2, scriptlines[indexnum])
        #print(teste123)



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
