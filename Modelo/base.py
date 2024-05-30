from Modelo.bodega import Bodega
from Modelo.varietal import Varietal
from Modelo.tipoUva import TipoUva

tipo1 = TipoUva("t1", "Una uva tinta con cuerpo y taninos fuertes", "Cabernet Sauvignon")
tipo2 = TipoUva("t2", "Una uva blanca conocida por su frescura y acidez", "Sauvignon Blanc")
tipo3 = TipoUva("t3", "Una uva tinta famosa por sus notas frutales y especiadas", "Malbec")
tipo4 = TipoUva("t4", "Una uva blanca con notas de fruta tropical y mantequilla", "Chardonnay")
tipo5 = TipoUva("t5", "Una uva tinta con cuerpo medio y notas de cereza", "Merlot")
tipo6 = TipoUva("t6", "Una uva blanca dulce utilizada para vinos de postre", "Riesling")
tipo7 = TipoUva("t7", "Una uva tinta con aromas de frutas rojas y pimienta", "Syrah")
tipo8 = TipoUva("t8", "Una uva blanca con notas de manzana y cítricos", "Pinot Grigio")
tipo9 = TipoUva("t9", "Una uva tinta con alta acidez y taninos moderados", "Sangiovese")
tipo10 = TipoUva("t10", "Una uva blanca con aromas florales y frutales", "Gewürztraminer")


var1 = Varietal("v1", "Vino tinto de color rojo intenso con aromas a frutos rojos, especias y cuero.", "80%", tipo1)
var2 = Varietal("v2", "Vino tinto de color púrpura oscuro con aromas a grosella negra, cedro y tabaco.", "70%", tipo3)
var3 = Varietal("v3", "Vino tinto de color violeta intenso con aromas a frutos negros, pimienta negra y violetas.", "60%", tipo10)
var4 = Varietal("v4", "Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero.", "50%", tipo8)
var5 = Varietal("v5", "Vino blanco de color amarillo pajizo con aromas a manzana verde, cítricos y mantequilla.", "100%", tipo6)
var6 = Varietal("v6", "Vino blanco de color verde pálido con aromas a grosella espinosa, hierba fresca y pomelo.", "100%", tipo4)
var7 = Varietal("v7", "Vino blanco de color amarillo pajizo con aromas a heno, melocotón y cítricos.", "100%", tipo2)
var8 = Varietal("v8", "Vino blanco de color amarillo pajizo con aromas a manzana verde, lima y flores blancas.", "100%", tipo8)
var9 = Varietal("v9", "Vino tinto de color rojo claro con aromas a fresa, cereza roja y setas.", "100%", tipo7)
var10 = Varietal("v10", "Vino tinto de color rojo rubí con aromas a frambuesa, especias y cuero.", "60%", tipo4)


bod1 = Bodega(
    id="b1", 
    coordenadasUbicacion="30.679359", 
    descripcion="Bodega Argentina instalada en el Valle de Uco. Cultivan los vinos en las alturas de este valle para producir vinos con cuerpo profundo y complejo.", 
    historia="Corría el año 1861 cuando Francesc Sala Ferré se convirtió en el primer miembro de la familia Ferrer-Sala en dedicarse al negocio del vino, pero sus antepasados ya llevaban siglos elaborado vino en las fincas familiares de La Freixeneda y Can Sala, ambas en el corazón del Penedés catalán - España.", 
    nombre="Acordeon", 
    periodoActualizacion=2, 
    fechaUltimaActualizacion="10/03/2024", 
    vinos=[var1, var2, var3]
)

bod2 = Bodega(
    id="b2", 
    coordenadasUbicacion="39.9041999", 
    descripcion="Bodega instalada en Fuenmayor, en la que dos de sus pilares básicos son la unión de tradición y modernidad. Esta bodega lleva a cabo la elaboración de vinos para todo tipo de públicos, tanto para los amantes del vino clásico como para aquellos que se introducen en el mundo del vino.", 
    historia="Bodegas Altanza, está ubicada en Fuenmayor (Rioja Alta), nació en octubre de 1998 con un claro principio fundador: elaborar vinos de calidad, de un estilo más “vivaz” que el clásico Rioja de antaño, y comercializarlos a un precio justo. La arquitectura de la bodega se concibe siguiendo un equilibrio entre tradición y tecnología. La finca cuenta con una extensión de 220 Has. de viñedo y 60 de olivar.", 
    nombre="Altanza", 
    periodoActualizacion=8, 
    fechaUltimaActualizacion="5/11/2023", 
    vinos=[var4, var5, var6]
)

bod3 = Bodega(
    id="b3", 
    coordenadasUbicacion="58.478361", 
    descripcion="Bodega Baines elabora todos los productos de manera artesanal generación tras generación, cuidando cada detalle para que cada sorbo sea una experiencia única.", 
    historia="Desde Licores Baines ponemos todos los medios posibles para poder garantizar la mayor calidad en cada uno de nuestros productos en base a los valores sociales, económicos y medioambientales de la empresa.", 
    nombre="Baines", 
    periodoActualizacion=5, 
    fechaUltimaActualizacion="03/09/2023", 
    vinos=[var7]
)

bod4 = Bodega(
    id="b4", 
    coordenadasUbicacion="-7.3198199", 
    descripcion="Bodega del Grupo Peralada instalada en un edificio con mas de 300 años de historia que se encuentra rodeado de cepas perfectas para el desarrollo de los vinos de esta bodega.", 
    historia="El proyecto de Casa Gran del Siurana se inició en el año 2000 con el claro objetivo de crear unos vinos desde el mismo inicio del proceso: seleccionando las fincas con más potencial, eligiendo las plantas más adecuadas y cultivándolas con cuidado para después controlar meticulosamente el momento de la vendimia, el modo de elaboración y la crianza.", 
    nombre="Casa Gran Del Siurana", 
    periodoActualizacion=6, 
    fechaUltimaActualizacion="05/01/2024", 
    vinos=[var8, var9]
)

varietales = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]
tiposUva = [tipo1, tipo2, tipo3, tipo4, tipo5, tipo6, tipo7, tipo8, tipo9, tipo10]
bodegas = [bod1, bod2, bod3, bod4]
