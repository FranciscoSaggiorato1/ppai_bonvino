from bodega import cargarData
bodegas=cargarData('./Modelo/data/bodega.csv')
for bodega in bodegas:
    print(bodega)