from django.shortcuts import get_object_or_404
from django import forms

from .models import Lesson
from domain.models import Domain

class CreateLessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['title', 'description','domain','title_paragraf_1','paragraf_1',
                  'title_paragraf_2','paragraf_2',
                  'image', 'image2', 'image3']
        widgets = {'paragraf_1': forms.Textarea(attrs={'required': 'required',
                                                        }),
                   'paragraf_2': forms.Textarea(attrs={'required': 'required',
                                                       })
                   }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateLessonForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.isdigit():
            raise forms.ValidationError("You can't have only "
                                        "numbers in your title")
        elif len(title) < 5:
            raise forms.ValidationError(
                u'Ensure your title has at '
                'least 5 characters')
        return title

    def clean_title_paragraf_1(self):
        title_paragraf_1 = self.cleaned_data['title_paragraf_1']
        if title_paragraf_1.isdigit():
            raise forms.ValidationError("You can't have only "
                                        "numbers in your title")
        elif len(title_paragraf_1) < 5:
            raise forms.ValidationError(
                u'Ensure your title has at '
                'least 5 characters')
        return title_paragraf_1

    def clean_title_paragraf_2(self):
        title_paragraf_2 = self.cleaned_data['title_paragraf_2']
        if title_paragraf_2.isdigit():
            raise forms.ValidationError("You can't have only "
                                        "numbers in your title")
        elif len(title_paragraf_2) < 5:
            raise forms.ValidationError(
                u'Ensure your title has at '
                'least 5 characters')
        return title_paragraf_2

    def clean_description(self):
        description = self.cleaned_data['description']
        if description.isdigit():
            raise forms.ValidationError("You can't have "
                                        "only numbers in your description")
        elif len(description) < 20:
            raise forms.ValidationError(
                u'Ensure your description has at '
                'least 20 characters')
        return description

    def clean_paragraf_1(self):
        paragraf_1 = self.cleaned_data['paragraf_1']
        if paragraf_1.isdigit():
            raise forms.ValidationError("You can't have "
                                        "only numbers in your description")
        elif len(paragraf_1) < 500:
            raise forms.ValidationError(
                u'Ensure your description has at '
                'least 20 characters')
        return paragraf_1

    def clean_paragraf_2(self):
        paragraf_2 = self.cleaned_data['paragraf_2']
        if paragraf_2.isdigit():
            raise forms.ValidationError("You can't have "
                                        "only numbers in your description")
        elif len(paragraf_2) < 500:
            raise forms.ValidationError(
                u'Ensure your description has at '
                'least 20 characters')
        return paragraf_2


    def clean_domain(self):
        domain = get_object_or_404(Domain,
                                     name=self.cleaned_data['domain'])
        return domain


    def clean_image4(self):
        image = self.cleaned_data['image']
        image2 = self.cleaned_data['image2']
        image3 = self.cleaned_data['image3']
        image_names = []
        if(image):
            image_names.append(image.name)
        if(image2):
            image_names.append(image2.name)
        if(image3):
            image_names.append(image3.name)
        if(len(image_names)-1 == len(set(image_names))):
            raise forms.ValidationError("You can't upload 2 images"
                                        "that are the same")
        return image3