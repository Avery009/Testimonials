from django import forms
from ..models import Testimonial

class Testimonial(forms.ModelForm):
	class Meta:
		model = Testimonial
		fields = '__all__'
	testimonial_id = forms.CharField(required=True)
	testimonial_date = forms.DateField(required=True)
	testimonial_title = forms.CharField(required=True, max_length=100)
	testimonial_description = forms.CharField(required=True, max_length=10000)
	thanks_count = forms.CharField(max_length=1000,required=True)
class Thanks(forms.Form):
	testimonial_title = forms.CharField(max_length=100, required = True)
	testimonial_description = forms.CharField(max_length = 10000, required = True, widget=forms.Textarea)
	thanks_count = forms.CharField(max_length=100, required = True)
class TestimonialEntry(forms.Form):
	testimonial_title = forms.CharField(max_length=100, required = True)
	testimonial_description = forms.CharField(max_length = 10000, required = True, widget=forms.Textarea)
