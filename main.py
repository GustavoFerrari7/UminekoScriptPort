
import re
from difflib import SequenceMatcher

class bcolors:
    OKBLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

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
                global indexnum
                maybe = 0
                passed = None
                maybebest = ""
                maybetranslation = ""
                wordbest = ""
                iterations = 0
                for j in range (indexnum-50, num_lines):
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
                    if iterations > 100:
                        break
                    iterations +=1
                if passed == None:
                    print(bcolors.RED + "Original: " + texto[i] + "                index: " + str(indexnum+1) + bcolors.ENDC)
                    print(bcolors.YELLOW + "Script EN: " + maybebest)
                    print("Script PT: " + maybetranslation + bcolors.ENDC)
                    print(bcolors.OKBLUE + "Script EN 2: " + scriptlinesEN[indexnum])
                    print("Script PT 2: " + scriptlines[indexnum] + bcolors.ENDC)

                    manual = input("Frase: ")
                    if manual == "y":
                        mudado = mudado.replace(texto[i], maybetranslation.replace('\n', ''))
                    elif manual == "y2":
                        mudado = mudado.replace(texto[i], scriptlines[indexnum].replace('\n', ''))
                    elif manual == "n":
                        pass
                    elif manual == "n2":
                        indexnum -= 1
                    else:
                        mudado = mudado.replace(texto[i], manual.replace('\n', ''))
                    cond = "aeooo"
                indexnum+=1
            if cond != None:
                g.write(mudado)
            else:
                g.write(aqui)
        else:
            g.write(aqui)



    f = open("original.u", "r", encoding="utf-8")
    lines = f.readlines()
    savedfile = None

    nf = input("Create a new file?  y = yes")
    if nf == "y":
        g = open("myfile.u", "w", encoding="utf-8")
    else:
        g = open("myfile.u", "r+", encoding="utf-8")
        savedfile = g.readlines()

    script = open("script.txt", "r", encoding="utf-8")
    scriptlines = script.readlines()
    scriptEN = open("scripten.txt", "r", encoding="utf-8")
    scriptlinesEN = scriptEN.readlines()


    num_lines = sum(1 for line in scriptlinesEN)
    savestateline = sum(1 for line in savedfile)
    print(savestateline)
    savestateindex = 319
    indexnum = savestateindex
    countline = 0
    for line in lines:
        if countline == savestateline:
            testefun(line)
        else:
            countline += 1
