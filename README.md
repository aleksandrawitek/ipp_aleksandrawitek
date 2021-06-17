# ipp_aleksandrawitek
## Indywidualny Projekt Programistyczny

### Harmonogram

#### 04.02 - 28.03

- [x] stworzenie wyglądu strony jako kalendarza (GUI) <br />
- [x] opracowanie struktury baz danych

#### 29.03 - 11.04

- [x] dodanie możliwości tworzenia konta oraz logowania się <br />
- [x] sprawdzanie poprawności formularza wypełnionych danych 

#### 11.04 - 09.05 

- [x] dodawanie spotkania do kalendarza <br />
- [x] zautomatyzowane wysyłanie emaili z potwierdzeniem umówienia wizyty

#### 10.05 - 23.05 

- [x] dopracowanie zakładki konta użytkownika <br />
- [x] dodanie opcji odwołania spotkania <br />
- [x] przeglądanie historii <br />
- [x] wysyłanie emaila z przypomnieniem o spotkaniu

#### 24.05 - 17.06

- [x] dopracowanie detali <br />
- [x] sprawdzenie poprawności działania strony i ewentualne poprawienie błędów <br />
- [x] przygotowanie podsumowania oraz prezentacji końcowej

### Używane technologie:

- Python 3.8.4
- Django 3.1.7
- SQLite
- DBrowser for SQLite
- HTML
- CSS
- JavaScript

### Szczegółowa historia zmian (na bieżąco uzupełniana)


#### 04.02 - 28.03
- konfiguracja django, zapoznanie się z funkcjonalnościami (https://docs.djangoproject.com/pl/3.1/intro/tutorial01/)
- https://www.youtube.com/watch?v=ZsJRXS_vrw0&t=29s
- opracowanie grafik strony głównej
- opracowanie strony głównej, która wyświetla bieżący miesiąc
- opracowanie przycisków "wstecz", "naprzód"
- wyświetlanie wybranego miesiąca, roku
- dopasowanie ilości dni do wybranego miesiąca i roku oraz przypasowanie odpowiednich nazw "poniedziałek" itp.
- opracowanie tabeli w bazie danych "db.sqlite3"
#### 29.03 - 11.04
- zapoznanie się z wieloma poradnikami dot. tworzenia kont w django oraz panelu administratora (m.in kurs django girls, https://rk.edu.pl/pl/wprowadzenie-do-django-10/)
- dodanie możliwości tworzenia konta
- dodanie możliwości logowania
- sprawdzanie formularza danych (np. czy dany użytkownik juz istnieje, czy podany email jest prawidłowy)
- dodanie opcji braku możliwości interakcji na stronie bez wcześniejszego zalogowania
#### 11.04 - 09.05 
- opcja z dodaniem spotkania (przycisk - sam wygląd będzie jeszcze dopracowany)
- połączenie bazy danych z plikami html oraz informacjami wprowadzanymi przez użytkownika (input)
- pobieranie informacji o emailu zalogowanej osoby
- wysłanie na podany adres email wiadomosci z danymi dotyczacymi umówionej w danym momencie wizyty
- utworzenie adresu email na potrzeby projektu oraz konfiguracja zabezpieczeń (tak aby możliwe było wysyłanie zautomatyzowanych wiadomości)
- do dopracowania są jeszcze sprawdzanie poprawności umawianych dat, godzin itp. natomiast większość czasu spędziłam na połączeniu bazy danych z plikami html (był to konieczny krok aby w przyszłości móc wyświetlać umówione już spotkania w kalendarzu startowym). Natomiast czas na tego typu poprawki założyłam w końcowym etapie projektu.
#### 10.05 - 23.05 
- dodanie do strony głównej navigation bar (interaktywnego)
- dopracowanie zakładki konta użytkownika wraz z dodaniem zdjęcia profilowego
- oglądanie historii umówionych spotkań
- dodanie opcji odwołania spotkania - do dopracowania
- wysyłanie emaili z przypomnieniem (zautomatyzowane z użyciem celery)
#### 24.05 - 17.06
- dopracowanie zakładki z kontem użytkownika - edytowanie informacji oraz sprawdzanie ich poprawności
