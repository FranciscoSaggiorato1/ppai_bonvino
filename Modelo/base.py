from Modelo.bodega import Bodega
from Modelo.varietal import Varietal
from Modelo.tipoUva import TipoUva
from Modelo.vino import Vino
from Modelo.maridaje import Maridaje
from Modelo.enofilo import Enofilo
from Modelo.siguiendo import Siguiendo
from Modelo.usuario import Usuario
from datetime import date

# Tipos de Uva
tipo1 = TipoUva("Una uva tinta con cuerpo y taninos fuertes", "Cabernet Sauvignon")
tipo2 = TipoUva("Una uva blanca conocida por su frescura y acidez", "Sauvignoon Blanc")
tipo3 = TipoUva("Una uva tinta famosa por sus notas frutales y especiadas", "Malbec")
tipo4 = TipoUva("Una uva blanca con notas de fruta tropical y mantequilla", "Chardonnay")
tipo5 = TipoUva("Una uva tinta con cuerpo medio y notas de cereza", "Merlot")
tipo6 = TipoUva("Una uva blanca dulce utilizada para vinos de postre", "Riesling")
tipo7 = TipoUva("Una uva tinta con aromas de frutas rojas y pimienta", "Syrah")
tipo8 = TipoUva("Una uva blanca con notas de manzana y cítricos", "Pinot Grigio")
tipo9 = TipoUva("Una uva tinta con alta acidez y taninos moderados", "Sangiovese")
tipo10 = TipoUva("Una uva blanca con aromas florales y frutales", "Gewürztraminer")

# Varietales
var1 = Varietal("Vino tinto de color rojo intenso con aromas a frutos rojos, especias y cuero.", "80%", tipo1)
var2 = Varietal("Vino tinto de color púrpura oscuro con aromas a grosella negra, cedro y tabaco.", "70%", tipo3)
var3 = Varietal("Vino tinto de color violeta intenso con aromas a frutos negros, pimienta negra y violetas.", "60%", tipo10)
var4 = Varietal("Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero.", "50%", tipo8)
var5 = Varietal("Vino blanco de color amarillo pajizo con aromas a manzana verde, cítricos y mantequilla.", "100%", tipo6)
var6 = Varietal("Vino blanco de color verde pálido con aromas a grosella espinosa, hierba fresca y pomelo.", "100%", tipo4)
var7 = Varietal("Vino blanco de color amarillo pajizo con aromas a heno, melocotón y cítricos.", "100%", tipo2)
var8 = Varietal("Vino blanco de color amarillo pajizo con aromas a manzana verde, lima y flores blancas.", "100%", tipo8)
var9 = Varietal("Vino tinto de color rojo claro con aromas a fresa, cereza roja y setas.", "100%", tipo7)
var10 = Varietal("Vino tinto de color rojo rubí con aromas a frambuesa, especias y cuero.", "60%", tipo4)
var11= Varietal("Vino tinto de color rojo rubí con aromas a cereza, vainilla y cuero.", "90%", tipo8)
var12= Varietal("Vino tinto de color púrpura oscuro con aromas a cedro, tomillo y tabaco.", "70%", tipo3)

# Maridajes
m1 = Maridaje("Vino tinto Malbec con queso Gouda añejo.", "Malbec y Gouda")
m2 = Maridaje("Vino blanco Chardonnay con salmón a la plancha.", "Chardonnay y Salmón")
m3 = Maridaje("Vino tinto Cabernet Sauvignooon con carne de cordero asada.", "Cabernet Sauvignion y Cordero")
m4 = Maridaje("Vino rosado Pinot Noir con ensalada de quinoa y verduras.", "Pinot Noir y Ensalada")
m5 = Maridaje("Vino espumoso Brut Rosé con sushi.", "Brut Rosé y Sushi")
m6 = Maridaje("Vino blanco Sauvignoun Blanc con ceviche de pescado.", "Sauvignon Blanc y Ceviche")
m7 = Maridaje("Vino tinto Tempranillo con paella de mariscos.", "Tempranillo y Paella")
m8 = Maridaje("Vino blanco Verdejo con tapas españolas.", "Verdejo y Tapas")
m9 = Maridaje("Vino tinto Syrah con quesos azules.", "Syrah y Quesos Azules")
m10 = Maridaje("Vino blanco Riesling con postres frutales.", "Riesling y Postres")

# Bodegas
bod1 = Bodega("30.679359", "Bodega Argentina instalada en el Valle de Uco. Cultivan los vinos en las alturas de este valle para producir vinos con cuerpo profundo y complejo.", "Corría el año 1861 cuando Francesc Sala Ferré se convirtió en el primer miembro de la familia Ferrer-Sala en dedicarse al negocio del vino, pero sus antepasados ya llevaban siglos elaborado vino en las fincas familiares de La Freixeneda y Can Sala, ambas en el corazón del Penedés catalán - España.", "Acordeon", 2, date(2024, 3, 10))
bod2 = Bodega("39.9041999", "Bodega instalada en Fuenmayor, en la que dos de sus pilares básicos son la unión de tradición y modernidad. Esta bodega lleva a cabo la elaboración de vinos para todo tipo de públicos, tanto para los amantes del vino clásico como para aquellos que se introducen en el mundo del vino.", "Bodegas Altanza, está ubicada en Fuenmayor (Rioja Alta), nació en octubre de 1998 con un claro principio fundador: elaborar vinos de calidad, de un estilo más “vivaz” que el clásico Rioja de antaño, y comercializarlos a un precio justo. La arquitectura de la bodega se concibe siguiendo un equilibrio entre tradición y tecnología. La finca cuenta con una extensión de 220 Has. de viñedo y 60 de olivar.", "Altanza", 8, date(2023, 11, 5))
bod3 = Bodega("58.478361", "Bodega Baines elabora todos los productos de manera artesanal generación tras generación, cuidando cada detalle para que cada sorbo sea una experiencia única.", "Desde Licores Baines ponemos todos los medios posibles para poder garantizar la mayor calidad en cada uno de nuestros productos en base a los valores sociales, económicos y medioambientales de la empresa.", "Baines", 5, date(2023, 9, 3))
bod4 = Bodega("-7.3198199", "Bodega del Grupo Peralada instalada en un edificio con mas de 300 años de historia que se encuentra rodeado de cepas perfectas para el desarrollo de los vinos de esta bodega.", "El proyecto de Casa Gran del Siurana se inició en el año 2000 con el claro objetivo de crear unos vinos desde el mismo inicio del proceso: seleccionando las fincas con más potencial, eligiendo las plantas más adecuadas y cultivándolas con cuidado para después controlar meticulosamente el momento de la vendimia, el modo de elaboración y la crianza.", "Casa Gran Del Siurana", 6, date(2024, 1, 5))
bod5 = Bodega("8.3048218", "La bodega es mundialmente admirada y reconocida por su papel pionero al haber hecho resurgir la variedad Malbec y haber descubierto terroirs de altura extrema al pie de los Andes. Entre otros numerosos premios, en 2023 fue galardonada como mejor bodega del mundo según el ranking World's Best Vineyards.", "Fundada en 1902, Bodega Catena Zapata es reconocida por su rol pionero en haber hecho resurgir la variedad Malbec y haber descubierto los terroirs de altura extrema al pie de los Andes.", "Catena Zapata", 6, date(2024, 4, 17))
bod6 = Bodega("18.32482158", "Bodega Aragonesa que elabora unos vinos de alta calidad llevando a cabo unos procesos de elaboración con el máximo cuidado del medioambiente.", "Edra Bodega y Viñedos se gesta en el año 1999 en Ayerbe, Hoya de Huesca. En este enclave del prepirineo aragonés construyen una bodega moderna y adaptada a el entorno, cubriéndola con un manto de hiedra. Hoy disponen de 30 ha de viñedo propio en las que cultivan las variedades Merlot, Cabernet Sauvignon, Syrah, Tempranillo, Garnacha y Viognier.", "Edra", 7, date(2024, 5, 22))
bod7 = Bodega("40.25826254", "Bodegas Faustino, situada en Oyón, Rioja Alavesa, goza de un prestigio internacional logrado a lo largo de más de 150 años de experiencia en la elaboración y crianza de vinos de alta gama.", "En 1861 Eleuterio Martinez Arzok se instala en Oyon y compra alli la casa palacio y los viñedos. Es el principio de todo un linaje.", "Faustino", 4, date(2024, 2, 6))
bod8 = Bodega("32.1297563", "En plena Milla de Oro de la ribera del Duero, Finca Villacreces, se esconde, desde hace siglos, en un entorno único, entre sus viñedos, el Duero y un bosque de pinos centenarios.", "La bodega y el vino toman el nombre de Don Pedro de Villacreces, fraile y teólogo franciscano, primer habitante de Finca Villacreces en el S. XIII. En el año 2003, Grupo Artevino adquiere Finca Villacreces, una finca de 110 hectáreas en plena Milla de Oro de la Ribera del Duero bañada por el río Duero, asentada sobre un monasterio del císter posterior al s. XV. Finca Villacreces posee 64 hectáreas de viñedo propio, cuya mayor parte fue plantado en los años 70, dividida en 15 fincas de las variedades Tinto Fino, Cabernet Sauvignon y Merlot.", "Finca Villacreces", 8, date(2023, 10, 12))
bod9 = Bodega("-5.1279645", "Malbec es un tinto de color rojo violáceo brillante. Sus aromas son intensos y amables, con notas que recuerdan a frutas rojas, y tonos algo florales y especiados. En boca es generoso, fluido y expresivo, con taninos incipientes. De paladar franco y paso refrescante, con buen cuerpo y carácter.", "Es una bodega familiar fundada por la familia Arizu en 1901, y ha producido desde entonces vinos de alta calidad.", "Luigi Bosca", 3, date(2024, 2, 15))
bod10 = Bodega("15.1513845", "Vinos míticos como la Manzanilla Solear o el Amontillado Príncipe forman parte ya de la vinícola de España. Además de los vinos clásicos Jerezanos, desde Manzanillas a Palos Cortados, Barbadillo también elabora vinos tranquilos, tanto blancos como tintos y más recientemente espumosos de calidad como son el Beta Sur o el limitadisimo Toto.", "La bodega Barbadillo tiene su origen en el año 1821, año en el que empezó a elaborar Manzanilla. La esencia de la bodega es una conjunción de varios factores en el entorno de Sanlúcar. Un clima cálido y soleado, el viento de poniente, la característica uva Palomino y la increíble composición del suelo que tan grácilmente influye en la particularidad de estos vinos de Jerez, la Albariza.", "Barbadillo", 3, date(2024, 4, 25))
bod11 = Bodega("42.876523", "Esta bodega situada en la región de Borgoña, Francia, es conocida por sus exclusivos vinos Pinot Noir y Chardonnay.", "Fundada en 1880 por Jules Lavatine, esta bodega ha pasado por cuatro generaciones familiares, siempre manteniendo la tradición y calidad de sus vinos.", "Château Lavatine", 5, date(2023, 5, 14))
bod12 = Bodega("36.778259", "Conocida por sus innovadores métodos de vinificación y su compromiso con la sostenibilidad, esta bodega californiana destaca en el Valle de Napa.", "Establecida en 1976 por Robert Mondavi, esta bodega ha sido pionera en la producción de vinos de calidad en California, especialmente con su Cabernet Sauvignon y Chardonnay.", "Robert Mondavi Winery", 7, date(2023, 8, 20))
bod13 = Bodega("45.803755", "Ubicada en la región de Piamonte, Italia, esta bodega es famosa por sus vinos Barolo y Barbaresco, hechos de la variedad Nebbiolo.", "Desde 1896, la familia Marchesi di Barolo ha cultivado sus viñedos en las colinas de Langhe, produciendo vinos que reflejan el terroir único de la región.", "Marchesi di Barolo", 6, date(2024, 1, 3))
bod14 = Bodega("34.925601", "Esta bodega chilena, ubicada en el Valle de Colchagua, es reconocida por sus vinos Carmenere y Cabernet Sauvignuon.", "Casa Lapostolle fue fundada en 1994 por la familia Marnier Lapostolle y desde entonces ha ganado reconocimiento internacional por su dedicación a la calidad y la innovación en viticultura.", "Casa Lapostolle", 4, date(2023, 1, 18))
bod15 = Bodega("-33.869904", "Bodega australiana que combina técnicas tradicionales con modernas para crear vinos Shiraz y Cabernet Sauvignoin de alta calidad.", "Penfolds, fundada en 1844, es una de las bodegas más antiguas y prestigiosas de Australia, famosa por su vino insignia, Penfolds Grange.", "Penfolds", 8, date(2024, 2, 12))
bod16 = Bodega("41.385064", "Situada en la región de Cataluña, esta bodega se destaca por sus Cavas y vinos tintos de alta gama.", "Codorníu, con más de 450 años de historia, es una de las bodegas más antiguas de España y un referente en la producción de vinos espumosos de calidad.", "Codorníu", 5, date(2022, 12, 27))
bod17 = Bodega("38.736946", "Bodega portuguesa ubicada en el Valle del Duero, reconocida por sus vinos de Oporto y Douro de alta calidad.", "Desde 1880, Sandeman ha sido un nombre sinónimo de excelencia en vinos de Oporto, combinando tradición con innovación para crear vinos únicos y apreciados en todo el mundo.", "Sandeman", 6, date(2024, 3, 30))
bod18 = Bodega("40.712776", "Esta bodega estadounidense, ubicada en el estado de Nueva York, es famosa por sus vinos Riesling y Cabernet Franc.", "Dr. Konstantin Frank Wine Cellars, fundada en 1962, revolucionó la viticultura en la región de Finger Lakes al introducir variedades de uva europeas que prosperan en el clima frío.", "Dr. Konstantin Frank", 4, date(2023, 2, 8))
bod19 = Bodega("-34.603684", "Bodega uruguaya conocida por su vino Tannat, con una fuerte tradición familiar y un enfoque en la calidad y la autenticidad.", "Bodega Garzón, establecida en 2014, ha sido rápidamente reconocida por sus vinos excepcionales y su enfoque en la sostenibilidad y el respeto por el medio ambiente.", "Bodega Garzón", 7, date(2024, 5, 22))
bod20 = Bodega("41.902783", "Ubicada en la región de Toscana, Italia, esta bodega produce algunos de los mejores vinos Chianti y Super Tuscans.", "Antinori, una familia con más de 600 años de historia en la vinificación, ha sido un pionero en la creación de vinos innovadores y de alta calidad en la región de Toscana.", "Antinori", 5, date(2024, 4, 17))


# Vinos
v1 = Vino(2018, date(2024, 1, 15), "Trumpeter", "https://acdn.mitiendanube.com/stores/968/403/products/art10099_trumpetermalbec_750cc1bot1-d22d7d2b0354f0e2b015589991124106-640-0.jpg", "MODIFICA", 1500, [var1, var2, var3], [m1, m2, m3], bod1)
v2 = Vino(2019, date(2024, 2, 10), "Dada", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQelj-P5HqS_pTzC8YnXnpWkmpjBhBrSnErPORRgquoP03L_IrIxzSX1-mtCRVDWn1yyTc&usqp=CAU", "Notas de cassis y pimienta negra", 2000, [var7],[m3, m6], bod1)
v3 = Vino(2020, date(2024, 3, 12), "Protos", "https://www.bodegasprotos.com/wp-content/uploads/2020/04/Protos-Gran-Reserva-GEN%C3%89RICA.jpg", "Notas de cereza y chocolate", 1800, [var8, var2],[m9, m2, m4], bod1)
v4 = Vino(2017, date(2024, 1, 20), "Wenete", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhraOeDvzt__vdJSKaeQfP4hFbr1rBuTBxj5aNmelCO9mF6HZvnweazd58ivUzaEWOFM7XX867PbfewEmtTmcDepPU_fes1Z3v8jRaawxq5a0g-59FCQTcZwn30_7RGr9MSM9XNmyXVOTZq/s1600/Portada+Como+leer+una+etiqueta+de+vino+Entre+Copas+y+Corchos+01.jpg", "Notas de frambuesa y especias", 2200, [var1, var6, var9, var10], [m1, m6], bod2)
v5 = Vino(2021, date(2024, 4, 18), "Desquiciado", "https://eltriunfodebaco.com.ar/wp-content/uploads/2021/08/etiqueta-M.-Gutelli.png", "Notas de manzana y miel", 1600,  [var5, var7],[m3, m9, m5], bod2)
v6 = Vino(2016, date(2024, 2, 25), "Cordero con piel de lobo", "https://images.vivino.com/thumbs/yFVa6xmeRRqhiBR7FjsrPw_pl_480x640.png", "Notas de mora y regaliz", 1900,  [var3, var10, var8],[m4, m7, m10], bod2)
v7 = Vino(2018, date(2024, 3, 30), "LAN D-12", "https://www.casagourmet.es/blog/wp-content/uploads/2023/01/03072017-LAN-D-12-botella-sin-anada_-1024x641.jpg", "Notas de flores blancas y cítricos", 1400,  [var2, var6],[m4, m8, m9], bod3)
v8 = Vino(2019, date(2024, 1, 10), "San Cobate", "https://www.abzimpresores.es/wp-content/uploads/2023/02/confinamiento-conceptual-98.webp", "Notas de frutos rojos y tabaco", 1700,  [var1],[m2, m5], bod4)
v9 = Vino(2020, date(2024, 2, 14), "Etymo", "https://brandemia.org/contenido/subidas/2021/12/01-etymo-etiquetavino.jpg", "Notas de frutos negros y vainilla", 1500,  [var3, var7, var8, var10],[m1, m9], bod4)
v10 = Vino(2021, date(2024, 3, 22), "Krauel", "https://almargen.com/wp-content/uploads/2021/05/detalle_blanco_Krauel.jpg", "Notas de lima y hierbas", 1600,  [var3, var5],[m4], bod5)
v11 = Vino(2015, date(2024, 5, 10), "Rutini", "https://clickandfoods.com/cdn/shop/files/AL7A6dlCTTSyYa-wR_Jxmw_pl_375x500_a0f35c07-1444-4a43-a1e4-37ddcdde9f9d.png?v=1712513920", "Notas de cafe", 2000,  [var2, var6],[m7, m10], bod5)
v12 = Vino(2021, date(2024, 6, 5), "Vega Real", "https://www.empacke.com/wp-content/uploads/2018/05/vegareal-empacke-1.jpg", "Notas de piña y caramelo", 1900,  [var3, var8],[m2, m8], bod6)
v13 = Vino(2017, date(2024, 2, 3), "Durigutti", "https://http2.mlstatic.com/D_NQ_NP_786367-MLA51681595255_092022-O.webp", "Notas de cereza", 1900,  [var3, var6],[m1, m9], bod7)
v14 = Vino(2021, date(2024, 6, 5), "Matina", "https://www.ofifacil.com/portfolio/diseno-etiquetas-aceite-vino-envases-packaging-design-wine-oil-labels/matina/diseno-etiqueta-vino-matina-wine-label-design-2.jpg", "Notas de piña", 1900,  [var7, var8],[m1, m6], bod7)
v15 = Vino(2016, date(2024, 1, 11), "Puerta Grande", "https://sacesaseleccion.com/1296-thickbox_default/vino-rosado-etiqueta-botella-3-4-l-125-vol.jpg", "Notas de Lima", 1900,  [var5, var6],[m8, m4], bod7)
v16 = Vino(2021, date(2024, 6, 5), "Sol Naciente", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6MhQZqo3-LlJc7OmTtCUhtcF-xv9xK4vfRCvpN-oUHQ&s", "Notas de piña y caramelo", 1900,  [var3, var8],[m2, m8], bod8)
v17 = Vino(2022, date(2024, 6, 20), "Brisas del Sur", "https://f.fcdn.app/imgs/c4ae25/lasacristia.com.uy/scr/22df/original/catalogo/120135412013541/450_600/brisas-blend-selection-brisas-blend-selection.jpg", "Notas de cítricos, pomelo y hierbas frescas", 1700, [var2, var5, var9],[m4], bod8)
v18 = Vino(2019, date(2024, 6, 5), "Viñedos Escondidos", "https://almadelosandes.com.ar/wp-content/uploads/2021/03/ESCONDIDO-1.jpg", "Notas de ciruela, cereza y chocolate", 2800,  [var3, var8],[m2], bod9)
v19 = Vino(2021, date(2024, 6, 10), "El Amanecer", "https://acdn.mitiendanube.com/stores/087/677/products/amanecer_andino_blend1-5680bf48e1777e172516675914347280-640-0.png", "Notas de manzana verde, pera y flores blancas", 1600,  [var1, var5, var9],[m7, m9], bod9)
v20 = Vino(2023, date(2024, 6, 20), "La Joya del Desierto", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTG3rPQ87cDFinwAQSV6DhTwULN3GNdkIwiop12VKgV-A&s", "Notas de dátiles, higos y miel", 2001,  [var1, var5, var9],[m1, m5], bod10)
v21 = Vino(2018, date(2024, 7, 1), "Aurora", "https://www.sawinery.com/wp-content/uploads/2021/04/unnamed-6.jpg", "Notas de frutas tropicales y vainilla", 1800,  [var1, var3, var7],[m2, m6], bod11)
v22 = Vino(2019, date(2024, 7, 2), "Nebula", "https://www.nakedwines.com.au/wineImages/67294.jpg", "Notas de cereza negra y especias", 2000, [var2, var5], [m3, m8], bod11)
v23 = Vino(2020, date(2024, 7, 3), "Aromas del Bosque", "https://media.istockphoto.com/vectors/red-wine-bottle-label-with-woodland-and-forest-background-vector-id934828912?k=6&m=934828912&s=612x612&w=0&h=6u-W75mZjHxMmSf8Lr6zlR1lyR2veT99I87eJiOGbGA=", "Notas de bayas silvestres y roble", 2100, [var3, var8], [m1, m7], bod12)
v24 = Vino(2017, date(2024, 7, 4), "Luminoso", "https://i.etsystatic.com/8766829/r/il/8e2bc4/1701891673/il_570xN.1701891673_3qxp.jpg", "Notas de frutas rojas y chocolate", 1900,  [var4, var9],[m4, m9], bod13)
v25 = Vino(2021, date(2024, 7, 5), "Serendipia", "https://www.cuvashop.com/2182-large_default/vino-serendipia.jpg", "Notas de durazno y almendra", 2200,  [var2, var6, var10],[m5, m10], bod13)
v26 = Vino(2016, date(2024, 7, 6), "Travesía", "https://www.creativefabrica.com/wp-content/uploads/2021/01/Wine-Bottle-Label-By-Bartemis-Studio-5.jpg", "Notas de frutos negros y cuero", 1700,  [var1, var5, var8],[m2, m8], bod13)
v27 = Vino(2018, date(2024, 7, 7), "Amanecer en la Viña", "https://m.media-amazon.com/images/I/61VtORt0c6L._AC_SY450_.jpg", "Notas de frutas blancas y almendras", 2000, [var3, var7, var9], [m3, m9], bod14)
v28 = Vino(2019, date(2024, 7, 8), "Luz de Luna", "https://img.vinepair.com/wp-content/uploads/2020/11/white-wine-label-internal.jpg", "Notas de pera y miel", 1800,  [var2, var4, var8],[m4, m10], bod15)
v29 = Vino(2020, date(2024, 7, 9), "Alborada", "https://cdn.shopify.com/s/files/1/0504/1766/6671/products/Alborada_Tardia1_500x.jpg?v=1609577670", "Notas de manzana y caramelo", 1900,  [var1, var6, var10],[m5, m6], bod15)
v30 = Vino(2021, date(2024, 7, 10), "Bruma Matinal", "https://i.pinimg.com/originals/31/9a/57/319a5733141b7fb69b6c4c00000e47b3.jpg", "Notas de melocotón y vainilla", 2100,  [var3, var5, var9],[m7, m8], bod16)
v31 = Vino(2017, date(2024, 7, 11), "Destellos de Estío", "https://cdn.shopify.com/s/files/1/0004/0219/1437/products/bodegas-alnus-ribera-del-duero-vino-tinto-crianza-2020-sel-pun-id-2878848_550x550.png?v=1617635723", "Notas de ciruela y chocolate", 2200,  [var2, var7, var8],[m9, m10], bod17)
v32 = Vino(2018, date(2024, 7, 12), "Sinfonía de Uvas", "https://static.wixstatic.com/media/5d5612_e0835b8a7e524a49bc8c55e3d24f9400~mv2.jpg/v1/fill/w_1400,h_1400,al_c,q_90/5d5612_e0835b8a7e524a49bc8c55e3d24f9400~mv2.jpg", "Notas de bayas y vainilla", 1900,  [var1, var3, var10],[m1, m2, m3], bod17)
v33 = Vino(2020, date(2024, 7, 13), "Cielo Nocturno", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2bDF4Niwb4p0aQJ8D3xTQWJf3UAK54TeHyW-dGZWP-w&s", "Notas de arándanos y especias", 2100,  [var2, var5, var7],[m2, m5, m8], bod18)
v34 = Vino(2022, date(2024, 7, 14), "Alma del Valle", "https://www.casillerodeldiablo.com/ar/wp-content/uploads/2021/04/750_Wine_Devil-Reserva_CabSauv_Agosto2019_Mesa-Trabajo-1-1-1.jpg", "Notas de frutos rojos y especias", 2500,  [var4, var8, var9],[m2, m7], bod18)
v35 = Vino(2023, date(2024, 7, 15), "Celestia", "https://www.nakedwines.com.au/wineImages/86990.jpg", "Notas de frutas tropicales y flores blancas", 2300,  [var1, var5, var6],[m3, m8], bod19)
v36 = Vino(2024, date(2024, 7, 16), "Néctar de las Hadas", "https://images-na.ssl-images-amazon.com/images/I/51GgCxQWe4L._AC_SY450_.jpg", "Notas de fresas y crema", 2700,  [var2, var7, var10],[m4, m9], bod20)
v37 = Vino(2023, date(2024, 7, 17), "Vino del Ocaso", "https://images-na.ssl-images-amazon.com/images/I/81P3bmOr9yL._AC_SL1500_.jpg", "Notas de ciruela pasa y cuero", 2600,  [var3, var6, var9],[m5, m10], bod20)
v38 = Vino(2022, date(2024, 7, 18), "Estrella del Sur", "https://www.casillerodeldiablo.com/ar/wp-content/uploads/2021/04/750_Wine_Devil-Reserva_CabSauv_Agosto2019_Mesa-Trabajo-1-1-1.jpg", "Notas de frutos rojos y especias", 2400,  [var4, var8, var9],[m2, m7], bod20)

# Usuarios
u1 = Usuario("contraseña1", "Juan", True)
u2 = Usuario("contraseña2", "María", False)
u3 = Usuario("contraseña3", "Carlos", True)
u4 = Usuario("contraseña4", "Ana", False)
u5 = Usuario("contraseña5", "Luis", True)
u6 = Usuario("contraseña6", "Elena", False)
u7 = Usuario("contraseña7", "José", True)
u8 = Usuario("contraseña8", "Laura", False)
u9 = Usuario("contraseña9", "Pablo", True)
u10 = Usuario("contraseña10", "Sofía", False)

# Siguiendos y Enófilos
e1 = Enofilo("Gómez", "https://previews.123rf.com/images/deagreez/deagreez1802/deagreez180200132/95041097-concepto-de-estilo-de-vida-individual-de-personas-retrato-de-abuelo-pensativo-seguro-de-s%C3%AD-mismo.jpg", "Juan", u1)
e3 = Enofilo("Pérez", "https://www.shutterstock.com/image-photo/portrait-cheerful-man-smiling-camera-260nw-1478224751.jpg", "Carlos", u3)
e4 = Enofilo("Rodríguez", "https://www.stelorder.com/wp-content/uploads/2021/09/portada-empresario-individual.jpg", "Andres", u4)
e2 = Enofilo("Fernández", "https://previews.123rf.com/images/ariwasabi/ariwasabi1102/ariwasabi110200029/8871278-retrato-de-hombre-joven-guapo-aislada-sobre-fondo-blanco-cauc%C3%A1sico-hombre-con-barba-sonriendo.jpg", "Marcos", u2)
e9 = Enofilo("Sánchez", "https://esemanal.mx/revista/wp-content/uploads/2019/12/Mukund-Seetharaman-300x300.jpg", "Pablo", u9)
e10 = Enofilo("Ramírez", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEVvPqzHzxD68KYcpnVygPOew7j_kKTucv6pHH9rAuSA&s", "Sofía", u10)
e5 = Enofilo("López", "https://st2.depositphotos.com/3889193/8014/i/450/depositphotos_80142372-stock-photo-confident-businessman-posing-at-desk.jpg", "Luis", u5)
e8 = Enofilo("Hernández", "https://www.hacerempresa.uy/wp-content/uploads/2023/04/Ent_Scagani_home.jpg", "Laura", u8)
e6 = Enofilo("Martínez", "https://www.shutterstock.com/image-photo/friendly-charismatic-happy-curlyhaired-freckled-260nw-1561507150.jpg", "Elena", u6)
e7 = Enofilo("García", "https://impulsapopular.com/wp-content/uploads/2020/02/4645-Lectura-recomendada-cero-a-empresario.jpg", "José", u7)


s6 = Siguiendo(date(2023, 4, 3), date(2024, 1, 10), None, bod6,e3)
s1 = Siguiendo(date(2023, 10, 4), date(2024, 3, 15), e3, None,e1)
s2 = Siguiendo(date(2022, 12, 21), date(2023, 8, 20), None, bod8,e1)
s3 = Siguiendo(date(2024, 1, 12), date(2024, 5, 31), None, bod9,e2)
s17 = Siguiendo(date(2022, 12, 27), date(2023, 6, 4), e1, None,e9)
s7 = Siguiendo(date(2022, 9, 27), date(2023, 6, 4), e3, None,e4)
s5 = Siguiendo(date(2022, 11, 8), date(2023, 7, 5), e4, None,e2)
s18 = Siguiendo(date(2023, 6, 22), date(2023, 12, 13), e2, None,e9)
s19 = Siguiendo(date(2024, 12, 1), date(2024, 9, 6), None, bod1,e9)
s20 = Siguiendo(date(2023, 3, 19), date(2024, 4, 4), e4, None,e10)
s8 = Siguiendo(date(2023, 3, 22), date(2023, 12, 13), e9, None,e5)
s9 = Siguiendo(date(2024, 2, 1), date(2024, 9, 6), e10, None,e5)
s15 = Siguiendo(date(2022, 4, 8), date(2023, 7, 5), e5, None,e8)
s16 = Siguiendo(date(2024, 8, 3), date(2024, 1, 10), None, bod2,e8)
s4 = Siguiendo(date(2023, 5, 9), date(2024, 2, 29), e8, None,e2)
s11 = Siguiendo(date(2022, 11, 4), date(2024, 3, 15), e3, None,e6)
s12 = Siguiendo(date(2022, 2, 21), date(2023, 8, 20), None, bod1,e6)
s13 = Siguiendo(date(2024, 7, 12), date(2024, 5, 31), None, bod9,e7)
s10 = Siguiendo(date(2023, 7, 19), date(2024, 4, 4), e6, None,e7)
s14 = Siguiendo(date(2023, 5, 19), date(2024, 2, 29), e7, None,e5)


# Almacenamos todos los objetos en arrays con nombre representativo
bodegas = [bod1, bod2, bod3, bod4, bod5, bod6, bod7, bod8, bod9, bod10, bod11, bod12, bod13, bod14, bod15, bod16, bod17, bod18, bod19, bod20]
enofilos = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
maridajes = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
siguiendos = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]
tiposUva = [tipo1, tipo2, tipo3, tipo4, tipo5, tipo6, tipo7, tipo8, tipo9, tipo10]
usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
varietales = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]
vinos = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38]
