from django import forms
from recruitertests.models import Test

class TestForm(forms.ModelForm):

    class Meta():
        model = Test
        fields = ('testname','userlevel')
