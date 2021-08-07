# joojoo!- TodoApp perheille

![sovelluksen logo](https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/logo2.png)

## Sovelluksen käyttötarkoitus

Sovellus on tarkoitettu perheiden kotitöiden jakamiseen ja niiden tekemisen tarkkailuun. Vanhemmat voivat lisätä lapsilleen kotitöitä, 
joita lapset puolestaan voivat merkitä tehdyiksi. Tehtävän voi määrittää yhdelle lapselle kerrallaan. Sovellukseen tulee luoda käyttäjätunnus
ja vanhempi voi lisätä perheen.

## Linkit sovelluksen dokumentaatioon
[Arkkitehtuurikuvaus](https://github.com/nothros/ToDoApp-for-families/blob/main/dokumentaatio/arkkitehtuuri.md)

## II-viikkopalautus toiminnallisuus (8.8.2021)
- Voidaan luoda uusi käyttäjä
- Voidaan kirjautua sisään
- Voidaan luoda uusi perhe jos sitä ei ole
- Voidaan liittyä perheeseen jos sitä ei ole
- NoFamily- näkymästä voi kirjautua ulos
- Päänäkymästä voi kirjautua ulos


## II-viikkopalautuksen aikaisest puutteet (8.8.2021)

Päänäkymä koostuu yhteisesti navigaatiopalkista, joissa mahdollisuus
Kotinäkymä

Mikäli tehtäviä ei ole
- Mikäli käyttäjä on lapsi
  - Tulee hänelle ilmoitus ettei tehtäviä ole
- Mikäli käyttäjä on vanhempi
  - Tulee hänelle ilmoitus ettei tehtäviä ole, mutta voi silti lisätä tehtäviä

Mikäli tehtäviä on

- Käyttäjä on lapsi
  - Lapsi voi merkata tehtäviä tehdyksi
 - Käyttäjä on vanhempi
  - Voi hän lisätä tehtäviä
  - Näkee hän päivän tehtävät (myös kenelle tehtävät on osoitettu)

Tehtävät

Kummatkin käyttäjät voivat tarkastella annettuja ja tulevia tehtäviä ja niiden päivämääriä, mutta ainoastaan vanhempi näkee kaikki tehtävät, sekä kenelle ne on osoitettu, lapsi näkee vain omat tehtävänsä.

Perhe
- Käyttäjä on lapsi
  - Lapsi näkee perheenjäsensä
- Käyttäjä on vanhempi
  - Näkee perheenjäsenensä
  - Voi poistaa perheenjäsenen
  - Voi poistaa perheen
  - Voi poistaa itsensä (koko perhe poistuu)
        

Tämän lisäksi on erillinen näkymä 404-sivuille.
