import requests
import pandas as pd
import time

def DAT_VENT():    
    vent_list=pd.read_csv("./Data/Venta.csv",sep=",")
    vent_list=vent_list[["IdCliente","Precio","Cantidad"]]
    vent_list["venta"]=vent_list["Precio"]*vent_list["Cantidad"]
    vent_list=vent_list[["IdCliente","venta"]]
    vent_list=vent_list.groupby("IdCliente")["venta"].sum().reset_index()
    
    q1=vent_list["venta"].quantile(0.25)
    q2=vent_list["venta"].quantile(0.50)
    q3=vent_list["venta"].quantile(0.75)
    rang1=(vent_list["venta"].min(),q1)
    rang2=(q1,q2)
    rang3=(q2,q3)
    rang4=(q3,vent_list["venta"].max())
    
    def asignar(venta):
        if venta >= rang1[0] and venta < rang1[1]:return "Rango 1"
        elif venta >= rang2[0] and venta < rang2[1]:return "Rango 2"
        elif venta >= rang3[0] and venta < rang3[1]:return "Rango 3"
        elif venta >= rang4[0] and venta <= rang4[1]:return "Rango 4"
        else:return "Desconocido"
    vent_list["rang_vent"]=vent_list["venta"].apply(asignar)
    vent_list=vent_list.rename(columns={"IdCliente":"ID"})
    return(vent_list)

def DAT_CLIENT():
    client_list1=pd.read_csv("./Data/Clientes.csv",sep=";")
    client_list1=client_list1[["ID","Nombre_y_Apellido","Domicilio","Localidad","Provincia","X","Y"]]
    client_list1.dropna(inplace=True)
    vent_list=DAT_VENT()
    client_list2=pd.merge(client_list1,vent_list,on="ID")
    client_list2["Provincia"]=client_list2["Provincia"].replace("Ciudad de Buenos Aires","Buenos Aires")
    client_list2["X"]=client_list2["X"].str.replace(",",".")
    client_list2["Y"]=client_list2["Y"].str.replace(",",".")
    client_list2=client_list2[client_list2["rang_vent"]=="Rango 4"]
    client_list2=client_list2.sample(n=10,random_state=25)
    client_list2.reset_index(drop=True, inplace=True)
    client_list2["Temperatura"]=0
    return(client_list2)

def temp_weather(x,y):   
    clave_api ='483b23465b00c657ff8f5e197c0be5e9'
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={y}&lon={x}&appid={clave_api}&units=metric"
    respuesta = requests.get(url)
    datos_clima = respuesta.json()
    temp = datos_clima['main']['temp']
    return temp   

def temp_client():
    client_list2=DAT_CLIENT()
    for i in range(0,len(client_list2)):
        x=client_list2.loc[i,"X"]
        y=client_list2.loc[i,"Y"]
        client_list2.loc[i,"Temperatura"]=temp_weather(x,y)
        time.sleep(1)
    client_list2=client_list2[["ID","Nombre_y_Apellido","Domicilio","Localidad","Provincia","Temperatura"]]
    client_list2=client_list2[client_list2["Temperatura"]>=12]
    client_list2=client_list2.sort_values(by="Temperatura",ascending=False)
    return(client_list2)

def write():
    client_list2=temp_client()
    client_list2.to_csv("./Data/Client_weather",index=False)
    text=print("generated file")
    return

if __name__ == '__main__':
    write()