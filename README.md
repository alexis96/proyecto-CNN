## Object Detection api

Para este proyecto estamos usando una api basada en tensorflow para la deteccion de objetos en [object-detection-api](https://github.com/tensorflow/models/tree/master/research/object_detection) el cual viene acompañado de unos tutoriales
de instalacion y uso.

### Tutorial

siguiendo los pasos de instalación con una variación al instalarlo en windows podemos llegar a obtener los siguientes
resultados: 

![objects](https://2.bp.blogspot.com/-MO3T6Hybpkg/WUG-QjHrHbI/AAAAAAAAB2M/tQKa2ljTkRwYgtok3o_3Y6F5KCbC7a-qQCLcBGAs/s1600/image1.jpg "ejemplo")

Aqui vamos a incluir los pasos que yo hice para instalarlo en windows.......(Proximamente)

### Detalles de la red a usar

Proximamente.....

### Generando Imagenes

Dado el poco conociemiento para generar imagenes con calidad, lo que hice a continuacion fue descargar unas imagenes ".png" de mis
objetos a reconocer y unos paisajes ".jpg" en donde pondremos nuestros objetos.

Estas son una de las imagenes descargadas.

Objeto:

![vibora](images/vib5.png)

Entorno:

![entorno](images/h2.jpg)

```xml
-<annotation>

<folder>fotos redes</folder>

<filename>viboras_2_5_3.jpg</filename>

<path>C:\Users\alexi\Downloads\fotos redes\viboras_2_5_3.jpg</path>


-<source>

<database>Viboras</database>

</source>


-<size>

<width>660</width>

<height>440</height>

<depth>3</depth>

</size>

<segmented>0</segmented>


-<object>

<name>vib5</name>

<pose>Unspecified</pose>

<truncated>0</truncated>

<difficult>0</difficult>


-<bndbox>

<xmin>57</xmin>

<ymin>225</ymin>

<xmax>137</xmax>

<ymax>282</ymax>

</bndbox>

</object>

</annotation>

            
```

Y estos son algunos de los resultados obtenidos al correr el codigo...no muy buenos pero creo que pueden funcionar:


![result](images/viboras_2_5_3.jpg)

![result](images/viboras_4_3_4.jpg)

 

### Pasos para hacer el entrenamiento


