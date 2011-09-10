# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def insert():
    (db, table) = get_table(request)
    form = SQLFORM(db[table], ignore_rw=ignore_rw)
    if form.accepts(request.vars, session):
        response.flash = T('new record inserted')
    return dict(form=form,table=db[table])

def index():
    
	productos = db().select(db.producto.ALL)
	return dict(productos=productos)

def detalle():
	producto =db(db.producto.idproducto==request.args(0)).select() #request.args()toma en cuenta los datos que se va enviar en get o post
	return dict(producto=producto)
