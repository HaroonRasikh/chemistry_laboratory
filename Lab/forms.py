from django import forms
# from dropdown.models import DropdownModel
from django.forms import ModelForm
from .models import *

# class typeForm(ModelForm):
# 	class Meta:
# 		model = type  # models ta oluşturduğumuz classı çağrıyoruz
# 		#fields = " __all__"
# 		fields = ('hal','katı', 'sıvı','değer' ) # o classın bütün değişkenleri
# 		labels = {   # labels kütüphanesi kullandık web sayfımızda isimleri sağlamak için
# 			'hal': 'Hal',
# 			'katı':'',
# 			'sıvı':'',
# 			'değer': '',
# 		}

# 		widgets = {  # bu da başka bir kütüphane sayfamızı tablonun çevirini düzeltmek için

# 				'hal':forms.SelectMultiple(attrs ={'class':'form-control','placeholder':'Hal'}),
# 				'katı':forms.TextInput(attrs ={'class':'form-control','placeholder':'Katı'}),
# 				'sıvı':forms.TextInput(attrs ={'class':'form-control','placeholder':'Sıvı'}),
# 				'değer':forms.TextInput(attrs ={'class':'form-control','placeholder':'Gaz'}),

# 		}
class ExperimentUpdateForm(forms.ModelForm):
	class Meta:
		model = Experiment
		fields = ['adi', 'malzeme', 'description']

class MalzemeUpdateForm(forms.ModelForm):
	class Meta:
		model = Material
		fields = [
					'adi','miktar','özgünlük',
					'Materialtype','kati','sivi',
					'deger','tehlike','acidli',
			]




class ExperimentForm(forms.ModelForm):
	class Meta:
		model = Experiment
		fields = ['adi', 'malzeme', 'description']

class MalzemeForm(forms.ModelForm):
	class Meta:
		model = Material
		fields = [
					'adi','miktar','özgünlük',
					'Materialtype','kati','sivi',
					'deger','tehlike','acidli',
			]
class MalzemeSearchForm(forms.ModelForm):
	class Meta:
		model = Material
		fields = ['adi']

class ExperimentSearchForm(forms.ModelForm):
	class Meta:
		model = Experiment
		fields = ['adi']
# class MalzemeForm(ModelForm):
# 	class Meta:
# 		model = Material  # models ta oluşturduğumuz classı çağrıyoruz
# 		#fields = " __all__"
# 		fields = ('adi','miktar','özgünlük','malzemetürü','tarih' ) # o classın bütün değişkenleri
# 		labels = {   # labels kütüphanesi kullandık web sayfımızda isimleri sağlamak için
# 			'adi': '',
# 			'miktar':'',
# 			'özgünlük':'',
# 			'malzemetürü':'malzemetürü',
# 			'tarih': '',
# 		}

# 		widgets = {
			 
# 		# bu da başka bir kütüphane sayfamızı tablonun çevirini düzeltmek için

# 				'adi':forms.TextInput(attrs ={'class':'form-control','placeholder':'Adi'}),
# 				'miktar':forms.TextInput(attrs ={'class':'form-control','placeholder':'Miktar'}),
# 				'özgünlük':forms.TextInput(attrs ={'class':'form-control','placeholder':'özgünlük'}),
# 				'malzemetürü ':forms.SelectMultiple(attrs ={'class':'form-control','placeholder':'malzemetürü'}),
# 				'tarih':forms.TextInput(attrs ={'class':'form-control','placeholder':'Gün,ay,yil'}),

# 	  }
		         
class DeneyiForm(ModelForm):
	class Meta:

		model = Experiment
		#fields = " __all__"
		fields = ('adi','malzeme')

		labels = {
			'adi': '',
			'malzeme':'Malzeme',
		#	'malzeme1': 'Malzeme 1',
		#	'malzeme2':'Malzeme 2',
		#	'Malzeme3': 'Malzeme 3',
			'description':'',
		}

		widgets = {

				'adi':forms.TextInput(attrs ={'class':'form-control','placeholder':'Adi'}),
				'masaSayisi':forms.TextInput(attrs ={'class':'form-control','placeholder':'masaSayisi'}),
				'malzeme':forms.SelectMultiple(attrs={'class':'form-select','placeholder':'Malzeme'}),
				#'malzeme1':forms.Select(attrs ={'class':'form-select','placeholder':'Malzeme 1'}),
				#'malzeme2':forms.Select(attrs = {'class':'form-select','placeholder':'Malzeme 2'}),
				#'malzeme3':forms.Select(attrs = {'class':'form-select','placeholder':'Malzeme 3'}),
				'description':forms.Textarea(attrs={'class':'form-control','placeholder':'DeneyiTanımlama'}),

		}


# class UygulaForm(ModelForm):
# 	class Meta:
# 		model = DeneyiUygula
# 		#fields = " __all__"
# 		fields = ('deneySec','masaSayisi')
#
# 		labels = {
# 		 	'deneySec': 'deneyiSec',
# 		 	'masaSayisi':'',
# 		 }
#
# 		widgets = {
#
# 		 		'deneySec':forms.SelectMultiple(attrs ={'class':'form-control','placeholder':'deneyiSec'}),
# 		 		'masaSayisi':forms.TextInput(attrs ={'class':'form-control','placeholder':'masasayisi'}),
#
# 		 }

# class malzemeTuru(ModelForm):
#
# 	class Meta:
# 		model = type
# 		#fields = " __all__"
# 		fields = ('tur','aralik' )
#
# 		labels = {
# 			'tur': '',
# 			'aralik':'',
#
# 		}
#
# 		widgets = {
#
# 				'tur':forms.TextInput(attrs ={'class':'form-control','placeholder':'Tür'}),
# 				'aralik':forms.TextInput(attrs ={'class':'form-control','placeholder':'aralıklar'}),
#
#
# 		}

