import requests
from bs4 import BeautifulSoup
import pandas as pd

def Extrac_MercadoLibre(prod):
    r=requests.get("https://listado.mercadolibre.com.ar/{}#D[A:{}]".format(prod.replace(" ","-"),prod))
    cont=r.content
    soup=BeautifulSoup(cont,"html.parser")
    div=soup.find_all("div",{"class":"andes-card"})
    array=[]
    for item in div:
        data={}
        data["ID_PRODUCTO"]=43044
        data["Concepto"]=item.find("h2",{"class":"ui-search-item__title shops__item-title"}).text
        data["Tipo"]="REFRIGERACIÓN"
        data["Precio"]=item.find("span",{"class":"price-tag-fraction"}).text
        array.append(data)
    dat=pd.DataFrame(array).head(2)
    return(dat)

def Extrac_Tiendamia(prod):
    r=requests.get("https://tiendamia.com/ar/search?amzs={}".format(prod))
    
    cont=r.content
    soup=BeautifulSoup(cont,"html.parser")
    div=soup.find_all("div",{"class":"item button-border"})
    array=[]
    for item in div:
        data={}
        data["ID_PRODUCTO"]=43044
        data["Concepto"]=item.find("div",{"class":"item-name"}).text.replace("\n","")
        data["Tipo"]="REFRIGERACIÓN"
        try:data["Precio"]=item.find("span",{"class":"currency_price"}).text.replace("AR$ ","")
        except: data["Precio"]=item.find("span",{"class":"currency_price"})
        array.append(data)      
    dat=pd.DataFrame(array).head(2)
    return(dat)

def data_extract():
    store=int(input("Store Nº1: Mercado Libre \nStore Nº2: TiendaMia \n1 or 2 option: "))
    n_product=int(input("Nº Products: "))
    tab1=pd.DataFrame(columns=["ID_PRODUCTO","Concepto","Tipo","Precio"])
    for i in range(1,n_product+1):
        text=input("Product Nº"+str(i)+": ") 
        if   (store==1):tab2=Extrac_MercadoLibre(text) 
        elif (store==2):tab2=Extrac_Tiendamia(text)
        tab1=pd.concat([tab1,tab2])   
    return (tab1)

def data_insert():
    df=pd.read_csv("./Data/PRODUCTOS.csv",encoding="ANSI",sep=";")
    df=df.rename(columns={" Precio ":"Precio"})
    lng_id=df["ID_PRODUCTO"].max()
    tab1=data_extract()
    tab1["ID_PRODUCTO"]=range(lng_id+1,len(tab1["ID_PRODUCTO"])+43044)
    df=pd.concat([df,tab1])
    df.to_csv("./Data/Client_Test",index=False)
    text=print("generated file")
    return

if __name__ == '__main__':
    data_insert()
