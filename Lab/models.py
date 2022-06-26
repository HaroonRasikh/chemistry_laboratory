from django.db import models

# Create your models here.

class Material(models.Model): 
	adi = models.CharField('Malzeme Ismi', max_length=120, default='', blank=True, null=True)  # 1 malzemelerin ismi
	miktar = models.IntegerField(default='0', blank=True, null=True)  # malzemelerin miktari
	CHOICES = (('kati','katı'),
		      ('sivi','sıvı'),
		      ('gaz', 'gaz'),
		      )
	Materialtype = models.CharField('Malzeme Turu',max_length=5, default='', blank=True, null=True,choices=CHOICES)
	kati = models.CharField('Katı',max_length=120, default='', blank=True, null=True)
	sivi = models.IntegerField('Sıvı',default='0', blank=True, null=True)
	deger  = models.IntegerField('Değer',default='0', blank=True, null=True)
	özgünlük = models.IntegerField('Özgünlük', default='0', blank=True, null=True)
	# malzemetürü = models.ForeignKey(type, null=True, on_delete=models.SET_NULL)  # malzemelerin Türler
	  # Malzamalarin kayit ettigi tarihi
	# tehlike = models.BooleanField(default=NO,choices=YES_NO_CHOICES)
	tehlike = models.BooleanField(default=False)
	acidli = models.FloatField(default='0', blank=True, null=True)

	# searchfields = ['adi']
	# listdisplay = ['adi','miktar','malzemetürü','özgünlük','tehlike','acidli','tarih']
	# listeditable = ['miktar','malzemetürü','özgünlük','tehlike','acidli']
	# listfilter = ['tehlike']
	class Meta:
		verbose_name_plural='Malzemeler'
	def __str__(self):     # bu fonksiyonda bu listenin ismini unvan olarak kullanılıyor

		return self.adi












# class type(models.Model):
# 	CHOICES =(('katı','katı'),
# 		('sıvı','sıvı'),
# 		('gaz', 'gaz')
# 		)
# 	hal = models.CharField(max_length = 20,choices=CHOICES)
# 	#hal = models.CharField(max_length=100, choices=Tur_CHOICES)
# 	katı = models.CharField(max_length =20)
# 	sıvı = models.IntegerField()
# 	değer  = models.PositiveSmallIntegerField()
# 	DisplayFields = ['hal','katı','sıvı','değer']
# 	SearchFields = ['hal']
# 	#is_deleted = models.BooleanField(default=False)

# 	class Meta:
# 		verbose_name_plural='Türler'



# 	def __str__(self):
# 		return self.hal

		
# class Material(models.Model):  # Malzemelerin listesi
# 	adi = models.CharField('Malzemenin_Ismi', max_length=120)  # 1 malzemelerin ismi
# 	miktar = models.IntegerField()  # malzemelerin miktari
# 	özgünlük = models.FloatField()
# 	malzemetürü = models.ForeignKey(type, null=True, on_delete=models.SET_NULL)  # malzemelerin Türler
# 	tarih = models.DateTimeField('Kayit_Tarihi')  # Malzamaların kayıt ettiği tarıhı
# 	# tehlike = models.BooleanField(default=NO,choices=YES_NO_CHOICES)
# 	tehlike = models.BooleanField(default=True)
# 	acidli = models.FloatField()
# 	searchfields = ['adi']
# 	listdisplay = ['adi','miktar','malzemetürü','özgünlük','tehlike','acidli','tarih']
# 	listeditable = ['miktar','malzemetürü','özgünlük','tehlike','acidli']
# 	listfilter = ['tehlike']
# 	class Meta:
# 		verbose_name_plural='Malzemeler'

# 	def __str__(self):
# 		return self.adi
class Experiment(models.Model):   # Deneyi listesi deneyileri girilen deneyiler adi,lazım olan malzemeler, ve Tanimlari
	adi = models. CharField('Deneyi Adı', max_length=120, default='', blank=True, null=True)																					#masaSayisi = models.CharField(max_length = 120)
	malzeme = models.ManyToManyField(Material, blank = True)
	description = models.FileField('Föyler',upload_to='files',null=True,default=None)
	is_verified = models.BooleanField('doğrulandı',default=False)
	DisplayFields = ['adi', 'Malzemeler', 'description','is_verified']
	SearchFields = ['adi']
	class Meta:
		verbose_name_plural='Deneyiler'

	def __str__(self):               # bu fonksiyonda bu listenin ismini unvan olarak kullanılıyor
		return self.adi

	def Malzemeler(self):
		return ",".join([str(p) for p in self.malzeme.all()])




class DeneyiUygula(models.Model): # verilen masa sayısına göre toplam malzeme hesaplaması
 	#mazlm= models.ForeignKey(Malzemeler,null = True,on_delete = models.CASCADE)
 	mazlm = models.ManyToManyField(Material,blank=True,related_name='DeneyiUygulas')
 	#deneySec = models.ManyToManyField(deneyi,blank=True) # deneyi listesinden seçmek isteyen deneyi
 	denenyiSec = models.ForeignKey(Experiment,null=True,on_delete = models.CASCADE)
 	masaSayisi = models.IntegerField(default=50)
 	a = models.IntegerField(default=20)
 	b = models.BooleanField(default=False)
 	def save(self, * args, ** kwargs):
 		a = 0
 		if self.b == True:
 			a = self.mazlm.miktar * self.masaSayisi
 		return a
 		super(DeneyiUygula,self).save(* args, ** kwargs)