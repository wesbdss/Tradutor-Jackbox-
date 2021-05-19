import os
import json

def extrair_falas():
    # print(os.listdir('.\The Jackbox Party Pack 6\games\PushTheButton\content'))
    end = "./The Jackbox Party Pack 6/games/PushTheButton/content/"
    end2='./textos/'
    p1=  [] #pastas
    for x in os.listdir(end):
        if not x.endswith('.jet'):
            p1.append(x)

    for in p1:
        for y in os.listdir(end+x): #numeros dos foldes
            with open(end+x+'/'+y+'/data.jet','r') as f:
                data = json.load(f)
                f.close()
            with open(end2+y+'.txt','w') as f:
                for z in data['fields']:
                    try:
                        f.writelines(z['v']+'\n')
                    except Exception as ex:
                        print("Nao tem s")
                        f.writelines(z['s']+'\n')
                f.close()

def inserir_falas(qtd):
    # print(os.listdir('.\The Jackbox Party Pack 6\games\PushTheButton\content'))
    end1= './traduzidos/'
    end2 = "./The Jackbox Party Pack 6/games/PushTheButton/content/"
    qtd = 0
    p1=  [] #pastas
    for x in os.listdir(end2):
        if not x.endswith('.jet'):
            p1.append(x)

    for x in p1:
        for y in os.listdir(end2+x): #numeros dos foldes
            qtd+=change_text(num=y,origin=end2+x,tradu=end1)
    return qtd


def change_text(num='56150',origin='',tradu=''):
	
    print(">> >> Mudando o arquivo "+num)
    try:
        with open(origin+'/'+num+'/data.jet','r') as f: #pega os dados padroes
            arq = json.load(f)
            f.close()
        with open(tradu+num+'.txt','r') as f:# pega os traduzidos
            arq1 = f.readlines()
            f.close()
    except Exception:
        print(">> Erro")
        return 0

    arq1 = [x.rstrip('\n') for x in arq1] #remove \n's list compreession

    for z in arq['fields']:
        try:
            z['v'] = arq1[0]
            arq1.remove(arq1[0])
        except Exception:
            print("Não tem s")
            pass
    with open(origin+'/'+num+'/data.jet','w') as f:
        json.dump(arq,f)
        f.close()
    print(">> Sucesso")
    return 1
    

qtd = 0
qtd = inserir_falas(qtd)
print("{}/{} Traduzidos".format(qtd,len(os.listdir('./textos/'))))