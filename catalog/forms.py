from django.forms import ModelForm, forms
from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get['name', 'description']
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, использовано запрещенное слово в названии!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get['description']
        forbidden_description = ('казино', 'криптовалюта', 'крипта', 'биржа',
                                 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        for word in forbidden_description:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, использовано запрещенное слово в описании!')
        return cleaned_data
