# AlgoritmideKodutoo1

Koostanud: Taiger Kala

**1.	Raamatute järjestamis algoritm** <br>

Teame koheselt raamatu kõrgust peale vaadates. Samuti on riiulil fikseeritud pikkus.
Kastutaksin Insertion sorti raamatute järjestamiseks. Vasakule poole hakkan ehitama sorteeritud järjekorda. Igat järgnevat raamatut võrdlen riiulis vasakul olevate raamatutega ning asetan õigesse kohta.

Koodi näide <br>
![Screenshot 2023-10-04 154427](https://github.com/TaigerKala/AlgoritmideKodutoo1/assets/124361451/3e2e547f-2993-4661-812d-46a87b4ce2e6)

Koodi diagramm <br>
![InsertionSort drawio](https://github.com/TaigerKala/AlgoritmideKodutoo1/assets/124361451/e15669e2-37d0-41c2-b8b3-056289dd3df9)

Kasutatud allikad: https://www.geeksforgeeks.org/python-program-for-insertion-sort/

**2.	LIFO andmestruktuur** <br>

Tegu on listidel põhineva stackiga. Lisan append funktsiooniga listi lõppu uue elemendi. Viimane element on ühtlasi ka viimati lisatud element ning selle kustutamiseks kasutan indeksi -1 mis viitab viimasele elemendile listis.

Add_item funktsiooni ajaline keerukus on O(1), kuna meil on teada juba listi suurus ning lisame uue elemendi listi lõppu.

Delete_last on samuti ajalise keerukusega O(1), kuna tsükleid meil ei toimu vaid kustutame -1 indeksiga elemendi listist.

Funktsioonide kood <br>
![Screenshot 2023-10-04 163534](https://github.com/TaigerKala/AlgoritmideKodutoo1/assets/124361451/3cfa8375-01a3-4ea0-8ea9-f8d66c8d2f1c)

**3.	Rekursiivne Fibonacci funktsioon** <br>

Teame, et Fibonacci reas esimesed kaks elementi on 0 ja 1 ehk võime tagastada sisendi kui tegu on nende arvudega. Järgnevad elemendid on kahe eelmise elemendi summa.
Kutsume funktsioonis funktsiooni nii kaua välja kuniks saame funktsioonis kätte kas 0 või 1 ning liidame arvud kokku.

Koodi näide <br>
![Screenshot 2023-10-04 170814](https://github.com/TaigerKala/AlgoritmideKodutoo1/assets/124361451/dc50eeac-ab82-42d5-a105-74e2d3333ba0)

Fibonacci rekursioon arvuga 5 <br>
![CamScanner 2023-10-04 17 28](https://github.com/TaigerKala/AlgoritmideKodutoo1/assets/124361451/02795f5a-d655-41ed-b9ea-fd2e0d496239)

**4.	Binaarne otsingualgoritm** <br>

Binaar otsing iteratsiooniga. Jagame listi kaheks ja võrdleme kas otsitav number on keskpunktist mid suurem või väiksem. Kui otsitav number on suurem keskmisest võtame uueks miinimumiks, koodis low, keskmise tulemuse. Kui otsitav number on väiksem keskmisest võtame uueks maksimumiks, koodis high, keskmise. Jaotame listi nii kaua kuniks muutujad vastavad otsitavale numbrile.

Koodi näide <br>
![Screenshot 2023-10-04 180846](https://github.com/TaigerKala/AlgoritmideKodutoo1/assets/124361451/d8269e80-bda7-420a-bd34-ab822986c211)

Kasutatud materjal: https://www.geeksforgeeks.org/python-program-for-binary-search/ <br>


**5.	Puu joonistamine** <br>

![puu joonestamine drawio](https://github.com/TaigerKala/AlgoritmideKodutoo1/assets/124361451/b690f6c8-9a19-4ec7-be0d-cdc7679d3023)

Kõik puud on graafid aga kõik graafid ei ole puud. Puudes ei esine tsükleid ning kaared on suunamata. 
