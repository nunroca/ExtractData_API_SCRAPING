<p align="center">
<img src="https://marketbusinessnews.com/wp-content/uploads/2020/09/Web-scraping-vs-API-5983948598.jpg"   
>
</p>

​
# <h1 align="center">**EXTRACT DATA [API] [SCRAPING]**
</p>
<br><br><br>

<hr>  

## Resumen del Proyecto

Proyecto de extracción de datos, haciendo uso de herramientas de scrapping, y una Api oficial, cuya data extraída será aplicada en los nuevos objetivos una empresa de eccommerce, en la promoción de nuevo rubro de productos de refrigeracion.
<br>
<hr>  

## Transformaciones - ETL:

La primera parte, se requiere establecer una data ordenada de los clientes del ecommerce, categorizando por un rango etario de mayor venta, estableciendo las columnas.


            ["ID","Nombre_y_Apellido","Domicilio","Localidad","Provincia","X","Y"]       

Haciendo uso de dos datas:

+ Clientes.csv

+ Venta.csv

La segunda parte, se requiere trabajar con la data de los productos del eccomerce, estableciendo las columnas:

            ["ID_PRODUCTO","Concepto","Tipo","Precio"]   

haciendo uso de la data:

+ PRODUCTOS.csv



<hr>

## Extraccion de la API [WEATHER_CLIENT]:

Con la data generada en la primera parte, se realiza la consulta a la API de la página del clima, haciendo uso de los datos de latitud y longitud, para establecer la temperatura del lugar de residencia del cliente evaluado, luego se extrae y ordena de mayor a menor a los clientes con temperatura mayor a los 12Cº, estableciéndose un script que genere la data requerida.

            El script resultante : weather_client.py



<hr> 

## Extraccion por Scrapping [PRODUCT_TEST]:

Como parte de la segunda etapa, generamos los codigos de extraccion de dos paginas de eccomerce:

+ MercadoLibre

+ Tiendamia

Haciendo uso de la biblioteca beatifulsoup, se hace scrapping de las principales páginas, según los productos requeridos, estableciendo una estructura de ingreso de datos, desde la selección de la tienda, cantidad de productos a buscar, e ingreso de los nombres de los productos, seleccionado productos de refrigeración, los datos extraídos se ordenaran según la estructura de la data productos siendo ingresados en la misma, generando una nueva data de test, se establece el script de la extracción de data y generación de la nueva data. 


            El script resultante : product_test.py



<hr>

## Paginas de Extraccion :



<p><img src='img/mercado.jpg' width=65 height=30> &nbsp Mercado Libre</p>
<p><img src='img/tienda.jpg' width=65 height=30> &nbsp Tiendamia</p>
<p><img src='img/open.jpg' width=65 height=30> &nbsp OpenWeather</p>



<br>
<br>

## Herramientas :



<p><img src='img/pythonLogo.png' width=30 height=30> &nbsp Python</p>
<p><img src='img/soup.jpg' width=65 height=30> &nbsp BeautifulSoup</p>
<p><img src='img/pandasLogo.png' width=65 height=30> &nbsp Pandas</p>



<br>
<br>




**`Repositorio`**
                    https://github.com/nunroca/ExtractData_API_SCRAPING
