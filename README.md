# ArdicTECH March 2020

Soru 1: Soruda n. değere kadar hesaplanan fibonacci sayilariyla olusturulan fibonacci polinomunun x'in 0..100 degerleri almasiyla elde edilecek degerin 15 faktoriyele gore modunun alinmasi istenmistir.

Cozumun islem maliyetinin en aza indirilebilmesi icin problem parcalara bolunmustur ve uygulanmasi gereken adimlar su sekildedir:

  1 - n. degere kadar fibonacci sayilarini hesapla ve modunu al
  2 - x^n degerini hesapla ve modunu al
  3 - tum degerleri topla ve modunu al

1 - Burada n. degere kadar fibonacci sayilarinin hesaplanip modunun alinmasi icin pisano periyodu kullanilmistir. Fibonacci sayilarinin C sayisina gore modu alindiginda kalanlar bir periyot olusturur, bu sayede C = 15! degerini kullanarak pisano periyodunu hesapladik ve bu sayede tum fibonacci sayilarinin modunu hesaplamak yerine pisano periyoduna kadar olan degerlerin modunu hesaplayip bu degerleri her periyotta kullandik.

2 - x^n degeri n = 10^15 'e kadar buyuyeceginden ustel sayilarin modunun hesaplanmasinda recursive bir yaklasim kullandik. Bu yontem gercekten inanilmaz sekilde isimizi kolaylastirdi
(https://www.youtube.com/watch?v=C7gHx2StFi8)

3 - Son olarak tum degerleri toplayip 15! 'e gore modunu aldik.

#

Soru 2: Soruda veriseti olarak 1-100 arasi dogal sayilar kullanarak bir modelin carpma islemini yapmak uzere egitilmesi istenmistir.

Burada veriseti %80 training, %10 test ve %10 validation olarak ayrilmistir. 
Verilerimizin etiketleri, verilerdeki ikili degerlerin carpimidir, X: [4, 5], Y: [20] gibi.

Optimizer olarak Adam, loss fonksiyonu olarak mean squared error kullanılmıstır.
Model olarak kerasta 2 > 32 > 64 > 32 > 1 neuron'a sahip Dense modeli olusturulmustur.
