# Encoding/Decoding
======
### Plik ‘main.py’
Do szyfrowania tekstu służy funkcja „encode()”.  
Do deszyfrowania tekstu służy funkcja „decode()”.  
**Funkcja encode()** – przyjmuje jako parametr tekst do szyfrowania. Zwraca słownik, którego kluczami są „encoded” – zaszyfrowany tekst, oraz „key” – losowo wygenerowany klucz.

Na początku ta funkcja tworzy losowy klucz od 5 do 10 znaków, który będzie potrzebny do deszyfrowania tekstu. Dalej jest szyfrowany każdy znak po kolei:
Kroki szyfrowania:
1)	Oblicza się suma kodów każdego znaku klucza
2)	Oblicza się suma cyfr wcześniej obliczonej sumy
3)	Zmienna last_digit jest ostatnią cyfrą pierwszej obliczonej sumy, dalej jest wartość zmiennej jest zwiększona o 1. Ta wartość odpowiada za liczbę znaków, które będą szyfrować każdy kolejny znak.
4)	Do zmiennej temp_key jest przypisywany znak, wartością którego jest suma kodu szyfrowanego znaku oraz drugiej obliczonej sumy.
5)	Do zmiennej temp_key dodaje się znaki losowe, liczba których jest równa last_digit – 1
6)	Wartość zmiennej temp_key jest przypisana do zmiennej last_key, wartość której będzie kluczem dla następnego szyfrowanego znaku.
7)	Wartość zmiennej temp_key jest dodawana do zmiennej, która będzie przechowywać cały szyfrowany tekst.

**Funkcja decode()** – przyjmuje jako parametry zaszyfrowany tekst oraz klucz.
Deszyfrowanie polega na tym samym, jak działa funkcja „encode()”, ale w sposób odwrotny. Zwraca słownik, kluczem którego jest deszyfrowany tekst.
**Funkcja rand()** – zwraca liczbę losową z zakresu od a do b, przekazanych jako parametry.


### Plik ‘test.py’
Aby sprawdzić działanie funkcji encode/decode można zainstalować moduł „uvicorn”. Aby uruchomić lokalnie serwer należy wpisać do konsoli „uvicorn main:app --reload”
Wykorzystując bibliotekę requests można wysyłać żądania na serwer lokalny. W pliku ‘test.py’ jest zaimplementowany taki przykład.

Jeżeli zmienna ‘text’ będzie miała wartość 'Hello, apple!\n New line \t tab char', to czasami serwer może nie zwrócić deszyfrowanego tekstu. 
Jednak, przy tym samym kluczu i tekście szyfrowanym, metoda ‘decode’ będzie działać dobrze, jeżeli uruchamiać te funkcje bez używania serwera. Również będzie działać, jeżeli ręcznie wprowadzić te dane i uruchomić te funkcje klikając przycisk w przeglądarce (np. FastAPI - http://127.0.0.1:8000/docs#/).


