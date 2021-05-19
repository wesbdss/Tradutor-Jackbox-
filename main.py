from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as time
import codecs
import os
import ast
from unidecode import unidecode

def init():
    global drive
    drive = webdriver.Firefox()
    drive.get('https://translate.google.com/#view=home&op=translate&sl=en&tl=pt')

def close():
    drive.quit()

def check_integridade():
    for x in os.listdir('./textos/'):
        try:
            with open("./textos/"+x,"r") as f:
                text = f.readlines()
        except Exception as ex:
            print("{} - Arquivo Não existe no source".format(x))
            continue
        try:
            with open("./traduzidos/"+x,"r") as f:
                text1 = f.readlines()
        except Exception as ex:
            print("{} - Arquivo Não foi traduzido".format(x))
            body()

        if len(text) != len(text1):
            print("{} - Integridade Violada".format(x))
            verifi = len(text)
            text = [u.rstrip('\n') for u in text]
            translate = []
            for y in text:
                try:
                    if y in ["true","false"]:
                        translate.append(y)
                    else:
                        type(ast.literal_eval(y))
                        translate.append(y)
                except Exception as ex:
                    # print("traduziu ",y)
                    a = traduzir(y)
                    if a == translate[-1]:
                        time.sleep(2)#tem 10 sec pra internet voltar
                        a = traduzir(y)
                    translate.append(a)

            translate = [unidecode(u)+'\n' for u in translate]
            # print(translate)
            if verifi != len(translate):
                print("Erro duplicata: source: {} traduzido: {}".format(verifi,len(translate)))
                continue
            with codecs.open("./traduzidos/"+x,"w",'utf-8') as f:
                f.writelines(translate)

    
    

    
def traduzir(text=''):
    # codigo massivo de tradução
    ## send
    element = drive.find_element_by_id('source')
    element.clear()
    element.send_keys(text)
    time.sleep(2)

    ## get
    span = WebDriverWait(drive, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.tlid-translation.translation")))
    # element.clear()
    return span.text

def body():
    for x in os.listdir('./textos/'):
        with open("./textos/"+x,"r") as f:
            text = f.readlines()
        verifi = len(text)
        if x not in os.listdir('./traduzidos'):
            text = [u.rstrip('\n') for u in text]
            translate = []
            for y in text:
                try:
                    if y in ["true","false"]:
                        translate.append(y)
                    else:
                        type(ast.literal_eval(y))
                        translate.append(y)
                except Exception as ex:
                    # print("traduziu ",y)
                    a = traduzir(y)
                    if a == translate[-1]:
                        time.sleep(2)#tem 10 sec pra internet voltar
                        a = traduzir(y)
                    translate.append(a)

            translate = [unidecode(u)+'\n' for u in translate]
            # print(translate)
            if verifi != len(translate):
                print("Erro duplicata: source: {} traduzido: {}".format(verifi,len(translate)))
                continue
            with codecs.open("./traduzidos/"+x,"w",'utf-8') as f:
                f.writelines(translate)
        print("{}/{} traduzidos".format(len(os.listdir('./traduzidos')),len(os.listdir('./textos'))))

while len(os.listdir('./traduzidos')) <= len(os.listdir('./textos')):
    try:
        init()

        body()
            
        close()

        check_integridade()

        break
    except Exception as ex:
        continue




