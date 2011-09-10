# -*- coding: utf-8 -*-
#  base de datos
db = DAL('sqlite://producto.db');
db.define_table('producto',Field('idproducto','integer'),
						Field('nombre'),
						Field('categoria'),
						Field('stock','integer'))

db.producto.idproducto.requires = IS_NOT_EMPTY()
db.producto.idproducto.requires = IS_INT_IN_RANGE(0,10)
db.producto.nombre.requires = IS_LENGTH(100)
db.producto.nombre.requires = IS_NOT_EMPTY()
db.producto.stock.requires = IS_INT_IN_RANGE(0,100)




