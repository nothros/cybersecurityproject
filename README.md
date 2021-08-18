# joojoo!- TodoApp perheille

![sovelluksen logo](https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/logo2.png)

## Sovelluksen käyttötarkoitus

Sovellus on tarkoitettu perheiden kotitöiden jakamiseen ja niiden tekemisen tarkkailuun. Vanhemmat voivat lisätä lapsilleen kotitöitä, 
joita lapset puolestaan voivat merkitä tehdyiksi. Tehtävän voi määrittää yhdelle lapselle kerrallaan. Sovellukseen tulee luoda käyttäjätunnus
ja vanhempi voi lisätä perheen johon lapsi voi liittyä

## Linkit sovelluksen dokumentaatioon
[Arkkitehtuurikuvaus](https://github.com/nothros/ToDoApp-for-families/blob/main/dokumentaatio/arkkitehtuuri.md)

## II-viikkopalautus toiminnallisuus (8.8.2021)
- Voidaan luoda uusi käyttäjä
- Voidaan kirjautua sisään
- Voidaan luoda uusi perhe jos sitä ei ole (aikuinen)
- Voidaan liittyä perheeseen jos sitä ei ole (lapsi)
- NoFamily- näkymästä voi kirjautua ulos
- Päänäkymästä voi kirjautua ulos

## Linkki sovellukseen
[https://joojoo-app.herokuapp.com/](https://joojoo-app.herokuapp.com/)

## Käyttöohje
- Voit rekisteröidä uuden käyttäjän painamalla etusivulla näkyvää Rekisteröidy- linkkiä

- Rekisteröimisvaiheessa, mikäli olet tehnyt jotain väärin, sovellus ilmoittaa siitä asiaankuuluvalla virheviestillä.
- Mikäli rekisteröinti onnistuu, sovellus ohjaa takaisin etusivulle.

- Voit kirjautua tunnuksellasi sisään, ja sovellus ilmoittaa "Käyttäjätunnus tai salasana ei täsmää" mikäli syötät vääriä syötteitä.

- Mikäli valitsit käyttäjärooliksi aikuisen, voif luoda perheen. Perheelle tulee olla yksilöllinen nimi ja koodi
- Mikäli valitsit käyttäjärooliksi lapsen, voit liittyä jo valmiiksi luotuun perheeseen 
  - Voit kokeilla liittyä valmiiseen perheeseen perheen nimi: testi koodi: testi 

- Voit kirjautua perheen luonnin yhteydessä ulos.

- Pääsivulle päästessäsi, voit kirjautua ulos sivulta oikeasta yläkulmasta navigaatiopalkista.


## II-viikkopalautuksen aikaiset kriittiset puutteet (8.8.2021)

- Kaikki lopputoiminnallisuus itse sovellukselta (näitä voit tarkastella [Arkkitehtuurikuvaus](https://github.com/nothros/ToDoApp-for-families/blob/main/dokumentaatio/arkkitehtuuri.md) osiosta
- **pääsivustolla näkyvä käyttäjän nimi ja perheen nimi, sekä perheenjäsenten määrä eivät ole jäämässä sivulle**
