"""Data model module for Dietary Dating site."""

from google.appengine.ext import ndb

class EaterProfile(ndb.Model):
    """This is model object for each eater."""
    
    name = ndb.StringProperty(Required=True)
    gender = ndb.StringProperty(Required=True)
    vegan = ndb.BooleanProperty(required=True, default=False)
    vegetarian = ndb.BooleanProperty(required=True, default=False)
    paleo = ndb.BooleanProperty(required=True, default=False)
    pescatarian = ndb.BooleanProperty(required=True, default=False)
    peanut_allergy = ndb.BooleanProperty(required=True, default=False)
    tree_nut_allergy = ndb.BooleanProperty(required=True, default=False)
    lactose_intolerant = ndb.BooleanProperty(required=True, default=False)



