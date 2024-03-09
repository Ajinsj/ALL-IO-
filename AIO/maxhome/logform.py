from django.forms import ModelForm
from maxhome.models import login


# Create the form cla
class userlogForm(ModelForm):
        class Meta:
          model =  login
          fields = "__all__"