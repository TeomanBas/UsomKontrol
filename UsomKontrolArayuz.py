# gui arayüzü oluþturmak için tkinter modülünü dahil ediyoruz.
from tkinter import *
import datetime

#Kontrol butonu fonksiyonu
def KontrolEt():
    # usom dosyasýný read modunda açýyoruz
    dosya=open("usom.txt","r")
    # okunan usom.txt içeriðini icerik deðiþkenine atýyoruz
    icerik=dosya.read()
    # dosyayý kapatýyoruz
    dosya.close()
    # entry1 içerisne girdiðimiz ip veya domain deðerini ip deðiþkenine allýyoruz
    ip=entry1.get()
    # bugun deðiþkeninin içerisine zaman bilgisini alýyoruz
    bugun=datetime.datetime.now()
    # eðer ip deðeri icerik degiskeni içerisinde varsa aþaðýdaki iþlemler uygulanýr
    if str(ip) in icerik:
        # log dosyasý açtýk append (a) modunda
        dosya=open("log.txt","a")
        # ip nin yanýna tarih ekleyerek yazi deðiþkenini tanýmladýk
        yazi=str(ip)+"zararli\nTarih:"+str(bugun)+"\n"
        # dosya deðiþkeni içerisindeki log dosyamýza yazi deðiþkeninin içeriðini ekledik
        dosya.write(yazi)
        #dosyayi kapattýk
        dosya.close()
        # v deðiþkenimizin içerisine mesajýmýzý ekledik
        v.set("ip zararlidir")

    else:
        dosya=open("log.txt","a")
        yazi=str(ip)+"zararli degil \n Tarih"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararli degildir")

# tk fonksiyonunu top degiskenine ekledik ve top arayüzü için gerekli olan widget larý bunun üzerinde tanýmlayacaðýz
top=Tk()
# top arayüzü için windows baþlýðý oluþturuldu
top.title("USOM Ip Kontrol")
# top arayüzü kontrol butonu için text ve fonksiyon tanýmlandý
KontrolBtn=Button(top,text="Kontrol Et",command=KontrolEt)
# kontrol butonu için konum kordinatlarý girildi
KontrolBtn.place(x=50,y=50)
# butonu geometrik olarak  üst orta köþeye hizalar ve place boyutuna göre dinamik olarak hizanabilir
KontrolBtn.pack()

label1=Label(top,text="Kontrol Edilecek Ip Adreslerini Giriniz")
label1.place(x=50,y=100)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=110)
entry1.pack()

# stringvar deðiþkeni her deðiþtiðinde textvariable de deðiþecektir
v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()





# programý baþlatýr
top.mainloop()





top.mainloop()

top1=Tk()
top1.title("USOM Ip Kontrol2")