# joojoo!- TodoApp perheille

![sovelluksen logo](https://github.com/nothros/TodoApp-for-families/blob/main/static/logo2.png)

## Sovelluksen käyttötarkoitus

Sovellus on tarkoitettu perheiden kotitöiden jakamiseen ja niiden tekemisen tarkkailuun. Vanhemmat voivat lisätä lapsilleen kotitöitä, 
joita lapset puolestaan voivat merkitä tehdyiksi. Tehtävän voi määrittää yhdelle lapselle kerrallaan. Sovellukseen tulee luoda käyttäjätunnus
ja vanhempi voi lisätä perheen.

## Käyttäjät
Sovelluksella on kaksi käyttäjäroolia. Vanhempi ja lapsi. Vanhempi hallinnoi perheitä ja lapset merkitsevät tehtäviä tehdyiksi.

## Käyttöliittymäluonnos
![ruudunkaappaus kirjautumissivusta](https://raw.githubusercontent.com/nothros/TodoApp-for-families/main/dokumentaatio/loginpagescreenshot.png)
(Yllä kuva sovelluksen kirjautumissivusta) <br />
Sovellus muodostuu kahdesta erityyppisestä näkymästä:
Kirjautumissivusta, jolla
- Käyttäjä voi kirjautua sisään
- Rekisteröityä käyttäjäksi

sekä pääsivusta, jonka toiminnallisuus vaihtelee riippuen onko käyttäjä vanhempi vai lapsi.
- Pääsivun etusivulla käyttäjä voi tarkistella tehtäviä, ja riippuen roolista lisätä niitä.
- Tehtävälista- sivulla käyttäjä voi tarkastella kaikkia tehtyjä tehtäviään. Sovellus näyttää tehtävien määrän. 
- Perhe- sivulla käyttäjä voi tarkistella perhettään. Mikäli käyttäjä on vanhempi, voi hän myös poistaa perheenjäseniä

## Alustava toiminnallisuus

### Ennen kirjautumista

Käyttäjä voi luoda sovellukseen oman tilin

-   Käyttäjätunnus on kirjautumista varten, sen tulee olla uniikki, sovellus ilmoittaa jos näin ei ole
- Käyttäjä antaa nimensä
- Keksii salasanan
- Valitsee roolin vanhempi tai lapsi.
-   Sovellus ilmoittaa virheestä, mikäli kaikkia syöttökenttiä ei ole täytetty

Tai käyttäjä voi kirjautua sovellukseen olemassa olevalla käyttäjätunnuksellaan

-   Ilmoitetaan mikäli käyttäjätunnus tai salasana ei täsmää
-   Jos käyttäjä ei ole täyttänyt vaadittavia kenttiä

### Kirjautumisen jälkeen

#### Vanhempi
- Voi lisätä perheen
- Voi poistaa perheen
- Voi poistaa perheenjäseniä
- Voi poistaa itsensä (tällöin myös perhe poistuu)
- Voi antaa tehtäviä lapselle
- Voi muokata tehtäviä
- Voi poistaa tehtäviä

Kun vanhempi lisää perheen generoidaan avain jolla perheeseen voi liittyä. Lapsi tarvitsee avaimen perheeseen liittymistä varten.

#### Lapsi
- Voi liittyä perheeseen
- Voi merkitä annettuja tehtäviä tehdyiksi
- Voi tarkastella annettuja tehtäviä
- Ei voi poistaa tehtäviä
- Ei voi poistaa itseään

## Alustava tietokantakaavio
:construction: UNDER CONSTRCUTION :construction:

