from django import forms 
from .models import Topic , Post




class NewTopicForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Whats on your Mind :)'}),
                                max_length=4000,
                                help_text="MAx Length 4000 words")


    class Meta:
        model = Topic
        fields = ['subject','message']



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message',]