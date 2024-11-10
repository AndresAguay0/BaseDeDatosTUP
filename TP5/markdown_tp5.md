1. Determinación de Dependencias Funcionales  ######################################

    Basándonos en las restricciones, podemos deducir las siguientes dependencias funcionales para TORNEO:

    1) cod_torneo → nombre_torneo: Cada torneo tiene un código único (cod_torneo), pero el nombre del torneo (nombre_torneo) puede repetirse.

    2) {cod_torneo, cod_corredor} → nyap_corredor: El nombre y apellido del corredor (nyap_corredor) son únicos por corredor en cada torneo.

    3) {cod_torneo, cod_bicicleta} → marca_bicicleta: La marca de cada bicicleta depende de su código en el contexto de un torneo.

    4) {cod_torneo, cod_corredor, sponsor} → DNI_presidente_sponsor, DNI_medico: Cada sponsor tiene un único presidente y médico, y esta relación es única por corredor y torneo.


2. Claves Candidatas  ######################################

    Para identificar las claves candidatas, observamos que:

    {cod_torneo, cod_corredor, cod_bicicleta, sponsor} es una combinación que identifica de manera única a cada registro, dado que representa una bicicleta específica usada por un corredor, patrocinada por un sponsor en un torneo determinado.

    Por lo tanto, la única clave candidata es {cod_torneo, cod_corredor, cod_bicicleta, sponsor}.


3. Elección de Clave Primaria  ######################################
   
    Elegimos {cod_torneo, cod_corredor, cod_bicicleta, sponsor} como clave primaria, ya que identifica de manera única cada registro en la tabla TORNEO y permite que todas las dependencias funcionales estén correctamente localizadas.


5. Normalización hasta 3FN  ######################################
   
    1FN: La tabla TORNEO ya está en 1FN, ya que todos los atributos son atómicos.

    2FN : Para cumplir 2FN, eliminamos dependencias parciales en la clave primaria {cod_torneo, cod_corredor, cod_bicicleta, sponsor}. Esto implica crear nuevas tablas para que cada atributo dependa completamente de una clave primaria en su tabla correspondiente.

    3FN: Eliminamos dependencias transitivas para que cada atributo no clave dependa únicamente de la clave primaria.

    El nuevo esquema en 3FN queda como sigue:

    1)Tabla Torneo
         Atributos: cod_torneo, nombre_torneo
         Clave primaria: cod_torneo

    2)Tabla Corredor
          Atributos: cod_torneo, cod_corredor, nyap_corredor
         Clave primaria compuesta: (cod_torneo, cod_corredor)
          Clave foránea: cod_torneo (referencia a Torneo)

    3)Tabla Bicicleta
           Atributos: cod_torneo, cod_bicicleta, marca_bicicleta
           Clave primaria compuesta: (cod_torneo, cod_bicicleta)
           Clave foránea: cod_torneo (referencia a Torneo)

    4)Tabla Sponsor
          Atributos: sponsor, DNI_presidente_sponsor, DNI_medico
         Clave primaria: sponsor

    5)Tabla Patrocinio
          Atributos: cod_torneo, cod_corredor, cod_bicicleta, sponsor
          Clave primaria compuesta: (cod_torneo,  cod_corredor,cod_bicicleta, sponsor)
          Claves foráneas:
                     cod_torneo, cod_corredor (referencia a Corredor)
                      cod_torneo, cod_bicicleta (referencia a Bicicleta)
                     sponsor (referencia a Sponsor)
