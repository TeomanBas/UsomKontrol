# http istekleri yapabilmek ve http ile ilgili fonksiyonlari kullanabilmek icin request modulunu import ettik
import requests 

# get metodu ile belirtilen url bir istek yapiyoruz ve gelen cevabi bir degisken icerisine aliyoruz
response=requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)
# response degiskeninin icindekileri yazdirmak icin yazma modunda  metin dosyasi aciyoruz
dosya=open("usom.txt","w")
# response icerigini dosya icerisine yazdiriyoruz
dosya.write(str(response.content))
# dosyayi kapatiyoruz
dosya.close()
