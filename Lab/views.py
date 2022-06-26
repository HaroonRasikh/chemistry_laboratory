from django.shortcuts import render,redirect
#from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# *****
from django.http import HttpResponseRedirect
#from .forms import DeneyiForm
#from .forms import InvoiceForm,InvoiceSearchForm,ExperimentSearchForm
from .forms import *
from .models import *


# Create your views here.
#def a (deneyi):
#	return deneyi.malzeme * 5
# def update_malzeme(request, malzeme_id):
# 	malzeme = Malzemeler.objects.get(pk = malzeme_id)


# def update_deneyi(request, deneyi_id): # deneyi_listesinde ki vergileri güncelmesini yapıyor
# 	e = Experiment.objects.get(pk = deneyi_id)

# 	form = DeneyiForm(request.POST or None, instance = e) # request.post means that we want to post to our page or nothing and instance means that show us the before data during updating
# 	if form.is_valid(): # 1these codes check and save our data to the deneyi listesi database on page
# 		form.save()  # 2
# 		return redirect('deneyi-listesi') # 3
# 	return render(request,'update_deneyi.html',{'e': e, 'form':form})


# def show_deneyi(request, deneyi_id): # deneyile_listesinin içindeki verileri gösteriyor
# 	d = Experiment.objects.get(pk = deneyi_id)
# 	return 	render (request, 'show_deneyi.html', {'d': d})

#def deneyiler_listesi(request):# eklediğmiz deneyileri listesini gösteriyor
#	b = Experiment.objects.all()
def update_deneyi(request, pk):
	queryset = Experiment.objects.get(id=pk)
	form = ExperimentUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ExperimentUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('deneyi-listesi')

	context = {
		'form':form
	}
	return render(request, 'add_deneyi.html', context)
	
def update_malzeme(request, pk):
	queryset = Material.objects.get(id=pk)
	form = MalzemeUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = MalzemeUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('malzeme-listesi')

	context = {
		'form':form
	}
	return render(request, 'add_malzeme.html', context)


def deneyiler_listesi(request):
	title2 = 'Deneyler'
	queryset2 = Experiment.objects.all()
	form = ExperimentSearchForm(request.POST or None)
	context = {
		"title2": title2,
		"queryset2": queryset2,
		"form": form,
		}
	if request.method == 'POST':
		queryset2 = Experiment.objects.filter(adi__icontains=form['adi'].value())
		context = {
		"form": form,
		"title2": title2,
		"queryset2": queryset2,
		}


	return render(request, "deneyi_list.html", context)


# def deneyiUygula(request):
# 	submitted = False
# 	if request.method == "POST":
# 		form = UygulaForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/uygula?submitted=True')
# 	else:
# 		form = UygulaForm
# 		if 'submitted' in request.GET:
# 			submitted = True
# 	return render(request,'uygula.html',{'form':form,'submitted':submitted})


# def show_malzeme(request, malzeme_id):# 'malzeme_listesi'indaki verileri belgelerini göster
# 	a = Material.objects.get(pk = malzeme_id) # bu da hangi verilere tıkladığmız numaralarını gösteriyor
# 	return render(request,'show_malzeme.html',{'a':a})
#def show_malzeme(request):
def delete_deneyi(request, pk):
	queryset = Experiment.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('deneyi-listesi')
	return render(request, 'delete_deneyi.html')



def delete_malzeme(request, pk):
	queryset = Material.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('malzeme-listesi')
	return render(request, 'delete_malzeme.html')


def malzeme_listesi(request):
	title = 'Malzeme Listesi'
	queryset = Material.objects.all()

	form = MalzemeSearchForm(request.POST or None)

	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		}
	if request.method == 'POST':
	 	queryset = Material.objects.filter(adi__icontains=form['adi'].value())
	 	context = {
	 	"form": form,
	 	"title": title,
	 	"queryset": queryset,
	 	}
	return render(request, "malzeme_list.html", context)



# def update_malzeme(request,malzeme_id): # 'malzeme_listesi' verilerinin güncelenmesini sağlıyor
# 	update = Material.objects.get(pk = malzeme_id) # hangi verilere gittiğmizde sayfa adresinde numaralarını gösteriyor
# 	form = MalzemeForm(request.POST or None, instance = update )
# 	if form.is_valid():
# 		form.save()
# 		return redirect('malzeme-listesi')
# 	return render(request,'update_malzeme.html',{'update':update, 'form':form})


# def malzeme_listesi(request): # bütün eklediğimiz malzemeleri listesidir
# 	malzeme_liste = Material.objects.all() #  model kısmında 'Malzemler' adına olan classın(tablo) değişkenleri çağrıyor
# 	return render(request,'malzeme_list.html',{'malzeme_liste':malzeme_liste})


# def add_deneyi(request): # bu da sayfamıza deneyilerin eklenmesini sağlıyor
# 	submitted = False
# 	if request.method == "POST":
# 		form = DeneyiForm(request.POST)
# 		if form.is_valid():

# 			form.save()
# 			return HttpResponseRedirect('/add_deneyi?submitted=True') # formu doldur ve onu tekrar sayfa yönlendir anlama geliyor
# 	else:
# 		form = DeneyiForm
# 		if 'submitted' in request.GET:
# 			submitted = True
# 	return render(request,'add_deneyi.html',{'form':form,'submitted':submitted})

def add_deneyi(request):
	form = ExperimentForm(request.POST or None,request.FILES)
	if form.is_valid():
		form.save()
		return redirect('deneyi-listesi')
	context = {
		"form": form,
		"title": "Deneyi Ekleme",
	}

	return render(request, "add_deneyi.html", context)



def add_malzeme(request):

	form = MalzemeForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('malzeme-listesi')
	context = {
	"form": form,
	}
	#return render(request, "add_malzeme.html", context)
	return render(request,'add_malzeme.html', context) # burasi ise bu class ait olan html dosyasini ve formu cagirmasidir

# def add_malzeme(request):
# 	submitted = False
# 	if request.method == "POST":
# 		form = MalzemeForm(request.POST)   # bu da forms dan çağırdığımız class
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/add_malzeme?submitted=True')
# 	else:
# 		form = MalzemeForm
# 		if 'submitted' in request.GET:
# 			submitted = True


# 	# bu code ise 'malzeme ekle' menusunda tablolarımızın doldurmasını sağlayalan kode

# 	return render(request,'add_malzeme.html',{'form':form,'submitted':submitted}) # burasi ise bu class ait olan html dosyasini ve formu cagirmasidir

# def malzemeTürü(request): # malzemenin türünü belirliyor ve aşağıdakı kodlarda yukarıye benziyor
# 	submitted = False
# 	if request.method == "POST":
# 		form = typeForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/malzemeturu?submitted=True')
# 	else:
# 		form = typeForm
# 		if 'submitted' in request.GET:
# 			submitted = True
# 	return render(request,'malzemeturu.html',{'form':form,'submitted':submitted})


def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
	# convert month from name to number
	name = "Haroon"
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)
	cal = HTMLCalendar().formatmonth(year, month_number)
	# current year

	now = datetime.now()
	current_year = now.year
	time = now.strftime('%I:%M %p')


	return render(request,
		'home.html',{
		"name": name,
		"year":  year,
		"month": month,
		"month_number": month_number,
		"cal": cal,
		"current_year": current_year,
		"time": time,
		})