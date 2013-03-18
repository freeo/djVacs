from modeltranslation.translator import translator, TranslationOptions
from eyevacs.models import Attribute, Level

class AttributeTranslationOptions(TranslationOptions):
    #requires a tuple!!! add a colon...
    fields = ('name',)

class LevelTranslationOptions(TranslationOptions):
    #requires a tuple!!! add a colon...
    fields = ('name',)

translator.register(Attribute, AttributeTranslationOptions)
translator.register(Level, LevelTranslationOptions)
