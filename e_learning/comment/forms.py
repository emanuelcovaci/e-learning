from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {'content': forms.Textarea(attrs={'required': 'required','rows':5,
                                                       })
                   }

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(CommentForm, self).__init__(*args, **kwargs)

        def clean_content(self):
            content = self.cleaned_data['content']
            if content.isdigit():
                raise forms.ValidationError("Nu poti avea "
                                            "numa numere in continut")
            elif len(content) < 100:
                raise forms.ValidationError(
                    u'Asigura-te sa '
                    'ai cel putin 100 de caractere ')
            return content