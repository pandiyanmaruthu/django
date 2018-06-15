from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'what\'s in your mind?' }),max_length=400,help_text='The max length of the text is 400.')
    class Meta:
        model=Topic
        fields=['subject','message']