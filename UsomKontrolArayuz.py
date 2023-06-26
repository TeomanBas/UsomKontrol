# gui aray�z� olu�turmak i�in tkinter mod�l�n� dahil ediyoruz.
from tkinter import *
import datetime

#Kontrol butonu fonksiyonu
def KontrolEt():
    # usom dosyas�n� read modunda a��yoruz
    dosya=open("usom.txt","r")
    # okunan usom.txt i�eri�ini icerik de�i�kenine at�yoruz
    icerik=dosya.read()
    # dosyay� kapat�yoruz
    dosya.close()
    # entry1 i�erisne girdi�imiz ip veya domain de�erini ip de�i�kenine all�yoruz
    ip=entry1.get()
    # bugun de�i�keninin i�erisine zaman bilgisini al�yoruz
    bugun=datetime.datetime.now()
    # e�er ip de�eri icerik degiskeni i�erisinde varsa a�a��daki i�lemler uygulan�r
    if str(ip) in icerik:
        # log dosyas� a�t�k append (a) modunda
        dosya=open("log.txt","a")
        # ip nin yan�na tarih ekleyerek yazi de�i�kenini tan�mlad�k
        yazi=str(ip)+"zararli\nTarih:"+str(bugun)+"\n"
        # dosya de�i�keni i�erisindeki log dosyam�za yazi de�i�keninin i�eri�ini ekledik
        dosya.write(yazi)
        #dosyayi kapatt�k
        dosya.close()
        # v de�i�kenimizin i�erisine mesaj�m�z� ekledik
        v.set("ip zararlidir")

    else:
        dosya=open("log.txt","a")
        yazi=str(ip)+"zararli degil \n Tarih"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararli degildir")

# tk fonksiyonunu top degiskenine ekledik ve top aray�z� i�in gerekli olan widget lar� bunun �zerinde tan�mlayaca��z
top=Tk()
# top aray�z� i�in windows ba�l��� olu�turuldu
top.title("USOM Ip Kontrol")
# top aray�z� kontrol butonu i�in text ve fonksiyon tan�mland�
KontrolBtn=Button(top,text="Kontrol Et",command=KontrolEt)
# kontrol butonu i�in konum kordinatlar� girildi
KontrolBtn.place(x=50,y=50)
# butonu geometrik olarak  �st orta k��eye hizalar ve place boyutuna g�re dinamik olarak hizanabilir
KontrolBtn.pack()

label1=Label(top,text="Kontrol Edilecek Ip Adreslerini Giriniz")
label1.place(x=50,y=100)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=110)
entry1.pack()

# stringvar de�i�keni her de�i�ti�inde textvariable de de�i�ecektir
v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()





# program� ba�lat�r
top.mainloop()





top.mainloop()

top1=Tk()
top1.title("USOM Ip Kontrol2")