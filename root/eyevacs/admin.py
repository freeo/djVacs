from eyevacs.models import Experiment, Scale, Scale_Question, Experiment, Participant, External_Order_Scale, Attribute, Level, External_Source_Data, External_Choice_Task, External_Baseline_Choice_Task, Grouping
from django.contrib import admin

class ChoiceTaskAdmin(admin.ModelAdmin):
    fields = ['ext_src_data_name','amount','a1','a2','a3','a4','a5','a6','a7','a8']
    list_display = ('id','ext_src_data','amount')

class AttributeAdmin(admin.ModelAdmin):
    fields = ['name','position']
    list_display = ('id','name','position')

class LevelAdmin(admin.ModelAdmin):
    fields = ['link_attribute','name','value']
    list_display = ('id','name','value')

admin.site.register(Experiment)
admin.site.register(Grouping)
admin.site.register(External_Source_Data)
admin.site.register(External_Choice_Task, ChoiceTaskAdmin)
admin.site.register(External_Baseline_Choice_Task)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Scale)
admin.site.register(Scale_Question)
admin.site.register(External_Order_Scale)
admin.site.register(Participant)

