# ArdicTECH March 2020 (Turkish version below)

Question 1: In question n. The value to be obtained by taking the values of 0..100 of the Fibonacci polynomial formed by the Fibonacci numbers calculated up to the value of 15 was requested to be modulated according to 15 factorials.

To minimize the processing cost of the solution, the problem is divided into parts and the steps to be implemented are as follows:

  1 - n. calculate Fibonacci numbers up to value and get mod
  2 - Calculate x^n and get its mod
  3 - add all values and get mod

1 - Here n. The Pisano period is used to calculate the Fibonacci numbers up to the value and take the mode. When the Fibonacci numbers are modded for the C number, the remainders form a period, so C = 15! We calculated the Pisano period using the value of the Pisano period, and thus, instead of calculating the mode of all Fibonacci numbers, we calculated the mode of the values ​​up to the Pisano period and used these values ​​in each period.

2 - Since the value of x^n will grow up to n = 10^15, we used a recursive approach to calculating the mode of exponential numbers. This method made our job incredibly easy
(https://www.youtube.com/watch?v=C7gHx2StFi8)

3 - Finally, add all the values and get 15! We got the mod according to.


Question 2: In the question, it is requested to train a model to perform multiplication using natural numbers between 1-100 as a dataset.

Here, the dataset is divided into 80% training, 10% testing, and 10% validation.
The labels of our data are the product of the binary values in the data, such as X: [4, 5], Y: [20].

Adam is used as the optimizer and mean squared error is used as the loss function.
As a model, a Dense model with 2 > 32 > 64 > 32 > 1 neuron was created in Keras.

############ Turkish Version

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
