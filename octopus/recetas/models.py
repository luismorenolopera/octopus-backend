from mongoengine import Document, DynamicDocument, EmbeddedDocument, fields


class Ingrediente(EmbeddedDocument):
    cantidad = fields.IntField()
    cuantificador = fields.StringField()
    nombre = fields.StringField()


class Autor(DynamicDocument):
    nombre = fields.StringField()
    edad = fields.IntField()


class Receta(Document):
    contenido = fields.StringField()
    imagen = fields.URLField()
    me_gusta = fields.ListField(fields.DynamicField())
    nombre = fields.StringField()
    autor = fields.ReferenceField(Autor, reverse_delete_rule=2)
    ingredientes = fields.EmbeddedDocumentListField(Ingrediente)
