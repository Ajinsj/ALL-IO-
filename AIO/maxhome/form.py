from django.forms import ModelForm
from maxhome.models import userregister


# Create the form cla
class userregForm(ModelForm):
        class Meta:
          model =  userregister
          fields = "__all__"