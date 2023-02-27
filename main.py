
import re
from difflib import SequenceMatcher
from functools import reduce
import openai
openai.api_key = ""

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

class bcolors:
    OKBLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'

if __name__ == '__main__':
    indexnum = 0
    repls = ('\n', ''), ('`', ''), ('{n}', '')
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
                        mudado = mudado.replace(texto[i], reduce(lambda a, kv: a.replace(*kv), repls, scriptlines[j]) )
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
                    opresponse = generate_text("traduza a seguinte frase para portugues:" + texto[i])
                    print(bcolors.GREEN + "Script OpenAI:" + opresponse + bcolors.ENDC)

                    manual = input("Frase: ")
                    if manual == "y":
                        mudado = mudado.replace(texto[i],  reduce(lambda a, kv: a.replace(*kv), repls,maybetranslation))
                    elif manual == "y2":
                        mudado = mudado.replace(texto[i],  reduce(lambda a, kv: a.replace(*kv), repls, scriptlines[indexnum]))
                    elif manual == "op":
                        mudado = mudado.replace(texto[i],  reduce(lambda a, kv: a.replace(*kv), repls, opresponse))
                    elif manual == "n":
                        pass
                    elif manual == "n2":
                        indexnum -= 1
                    else:
                            mudado = mudado.replace(texto[i], reduce(lambda a, kv: a.replace(*kv), repls, manual))
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
    savestateline = 0
    nf = input("Create a new file?  y = yes")
    if nf == "y":
        g = open("myfile.u", "w", encoding="utf-8")
    else:
        g = open("myfile.u", "r+", encoding="utf-8")
        savedfile = g.readlines()
        savestateline = sum(1 for line in savedfile)

    script = open("script.txt", "r", encoding="utf-8")
    scriptlines = script.readlines()
    scriptEN = open("scripten.txt", "r", encoding="utf-8")
    scriptlinesEN = scriptEN.readlines()


    num_lines = sum(1 for line in scriptlinesEN)
    print(savestateline)
    savestateindex = 3916
    indexnum = savestateindex
    countline = 0
    for line in lines:
        if countline == savestateline:
            testefun(line)
        else:
            countline += 1


 # 67
