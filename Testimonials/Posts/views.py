from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Testimonial
from .forms import forms
from django.template import loader
import datetime



def testimonials(request):
	#Load completed and current as separate lists
	user_current_list = Testimonial.objects.all().order_by('testimonial_date')
	template = loader.get_template('testimonials.html')
	context = {
		'testimonial_list' : user_current_list,
	}
	return HttpResponse(template.render(context,request))

def entertestimonial(request):
	if request.method == 'GET':
		form = forms.TestimonialEntry()
		context = {
			'form': form,
			'reqGet': True
		}
		template = loader.get_template('testimonialform.html')
	elif request.method == 'POST':
		form = forms.TestimonialEntry(request.POST)
		if form.is_valid():
			td = datetime.datetime.now()
			tt = form.cleaned_data['testimonial_title']
			ted = form.cleaned_data['testimonial_description']
			tc = '1'
			try:
				p = Testimonial(testimonial_title=tt,testimonial_date=td,testimonial_description=ted,thanks_count=tc)
				p.save()
				return redirect('/')
			except Exception as e:
				template = loader.get_template('error.html')
				context = {
					'error' : str(e)
				}
		else:
			context = {		
				'error' : 'Form Validation Error',
			}
			template = loader.get_template('error.html')
	else:
		template = loader.get_template('error.html')
		context = {
			'error' : '501 Invalid Request Protocol',
		}
	return HttpResponse(template.render(context,request))

def viewtestimonial(request,testimonial_id):
	#View an individual testimonial to pray for it
	if request.method == 'GET':
		try:
			testimonial = Testimonial.objects.get(pk=testimonial_id)
			template = loader.get_template('testimonial.html')
			context = {
				'testimonial' : testimonial
			}
		except Exception as e:
			template = loader.get_template('error.html')
			context = {
				'error' : str(e)
			}
	else:
		context = {
			'error' : '501 Invalid Request Protocol'
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))

def thank(request, testimonial_id):
	if request.method == 'GET':
		try:
			testimonial = Testimonial.objects.get(pk=testimonial_id)
			form = forms.Thanks()
			template = loader.get_template('thank.html')
			context = {
				'testimonial_id' : testimonial_id,
				'testimonial_title' : testimonial.testimonial_title,
				'testimonial_description' : testiomonial.testimonial_description,
				'thanks_count' : testimonial.thanks_count
			}
		except Exception:
			form = forms.Testimonial()
			context = {
				'error' : str(Exception)
			}
			template = loader.get_template('error.html')
	else:
		context = {
			'error' : '501 Invalid Request Protocol' #protocol error
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))

def givethanks(request, testimonial_id, thanks_count):
	if request.method == 'POST':
		try:
			testimonial = Testimonial.objects.get(pk=testimonial_id)
			#potentially reference other fields in prayer object to populate the rest of the form
			#increment prayer count
			count = thanks_count
			count = count + 1
			testimonial.thanks_count = count
			testimonial.save()
			return redirect('/')
		except Exception as e:
			context = {
				'error' : str(e)
			}
			template = loader.get_template('error.html')
	else:
		context = {
			'error' : '501 Invalid Request Protocol' #protocol error
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))
