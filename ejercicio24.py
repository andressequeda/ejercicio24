venta  =  int ( input ( "Ingrese el valor de la venta:" ))
iva  =  venta  *  0.19
descuento  =  venta  *  0.05
si  venta  > =  150000 :
    print ( "El valor de la venta mas iva y con descuento es de" , ( venta  +  iva ) -  descuento )
otra cosa :
    print ( "El valor de la venta mas iva es de" , venta  +  iva )