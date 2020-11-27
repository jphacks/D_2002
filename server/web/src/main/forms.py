from django import forms
from .models import Product

class ProductRegistrationForm(forms.ModelForm):
    """プロダクト登録用フォーム"""

    class Meta:
        model = Product
        fields = ('name', 'amount', 'price', 'intro', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'