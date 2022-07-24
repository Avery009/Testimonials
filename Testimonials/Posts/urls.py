from django.urls import path

from . import views

urlpatterns = [
	path('',views.testimonials, name='testimonials'),
	path('enter/',views.entertestimonial, name='input_testimonial'),
	path('view/<int:testimonial_id>', views.viewtestimonial, name='view_testimonial'),
	path('thank/<int:testimonial_id>', views.thank, name='thank'),
	path('thanks/<int:testimonial_id>/<int:thanks_count>', views.givethanks, name='give_thanks'),
]
