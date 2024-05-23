Įvadas:

Mano projektas buvo sukurti BirthdayReminder programą. Aš šį projektą pradėjau daryti pythono kalbą, kaip ir yra pagal reikalavimus, naudodamas fastapi framework'ą. Programa jungiama per terminalą, įvedant "uvicorn main:app" komandą - tai įjungia duomenų baze, ir tada prie jos galima prisijungti. Fastapi framework'as valdomas per "localhost/docs" browser'io svetainę.

Dėstymas / analizė:

4 objektinio progromavimo stulpai:

  1 - Abstrakcija
Buvo panaudota kuriant User ir Birthday repositorijas (ju strukturas - User(Abs)Method ir Birthday(Abs)Method)
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/89fe31ef-3b31-48c2-a3f7-daa71e16709d)

  2 - Paveldėjimas
UserRepository ir BdayRepository paveldi iš UserMethod ir BirthdayMethod klasių
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/437d1aed-7726-42e7-b70a-6d60d5b29334)

  3 - Inkapsuliacija
User modelio funkcijos su duomenų baze buvo paskirstitos į user_repository failą ir Birthday modelio funkcijos su duomenų baze buvo paskirstitos į bday_repository failą.
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/c3850aa7-18bd-4804-8bb3-9086ff8dbb85)
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/677cc3cf-aec0-4655-9b88-b4dbd6b8271d)


  4 - Polimorfizmas
BdayRepository ir UserRepository perrašo modulius esančius abstrakčiose klasėse su tokiais pačiais pavadinimais savo klasėse savo naudai\reikalams
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/9707f947-aa24-4117-8f3e-09497949771b)
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/ea29a1e9-c45f-4559-936a-04d7018611fe)


2 dizaino paternai:
  1 Singleton'as
Singleton'as yra panaudotas Database klaseje (kuri yra database.py faile) tam, kad uztikrinti tik viena prisijungima prie duomenu bazes.
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/79fdb5f1-93d6-4723-bd4c-9c8b0de1ec19)

  2 Fabriko metodas
Pastebimas BdayRepository klaseje su jos 4 metodais, kadangi BdayRepository klase laiko savyje visus reikalingus metodus sukurti ir redaguoti Birthday modelio vienetus.
![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/03c2a861-befc-49f2-b70c-acc33de12a3a)

 Įrašymas į failą
 Yra galimybė išsaugoti visus esamus Birthday modelio objektus.
 ![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/305a08d9-77a1-4f10-bcc0-d6c5d4dde9d7)
 ![image](https://github.com/DominukasJ/Objektinis-progromavimas/assets/170512787/090bc348-c8e5-4cda-abea-ea0e7979060b)




Rezultatai:

Kuriant projektą buvo susidurta su dauguma žinių trukumo ir to kas buvo primiršta. Dėl šių problemų, kai kurias kodo vietas reikėdavo truputi pakeisti, naudoti kitus metodus ir t. t. Projektas kaip ir yra baigtas, bet yra dauguma vietų, kuria galima būtų geriau padaryti. Kai kuriuose vietose kodą galima būtų patvarkyti, supaprastinti, panaudoti kitokius veikimus ir t. t.


Išvados:

Rašant projektą buvo susidurta su modulių import'avimo problemomis - buvo problemų import'uojant modelius iš skirtingų package'ų. Mano manymų prokektas yra baigtas, bet daug ką galima patobulinti ir pratęsti. 
