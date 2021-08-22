# joojoo!- TodoApp perheille

![sovelluksen logo](https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/logo2.png)

## Sovelluksen käyttötarkoitus

Sovellus on tarkoitettu perheiden kotitöiden jakamiseen ja niiden tekemisen tarkkailuun. Vanhemmat voivat lisätä lapsilleen kotitöitä, 
joita lapset puolestaan voivat merkitä tehdyiksi. Tehtävän voi määrittää yhdelle lapselle kerrallaan. Sovellukseen tulee luoda käyttäjätunnus
ja vanhempi voi lisätä perheen johon lapsi voi liittyä


## Linkki sovellukseen
[https://joojoo-app.herokuapp.com/](https://joojoo-app.herokuapp.com/)


## Linkit sovelluksen dokumentaatioon

[Arkkitehtuurikuvaus](https://github.com/nothros/ToDoApp-for-families/blob/main/dokumentaatio/arkkitehtuuri.md)

[Toiminnallisuus](#toiminnallisuus)

[Käyttöohje](#käyttöohje)

[Puutteet](#puutteet)


# Toiminnallisuus
### (22.8.2021)

### Kirjautuminen/Rekisteröinti
- Voidaan luoda uusi käyttäjä
- Voidaan kirjautua sisään
### Mikäli perhettä ei ole vielä luotu
- Voidaan luoda uusi perhe (aikuinen)
- Voidaan liittyä perheeseen (lapsi)
- NoFamily- näkymästä voi kirjautua ulos
### Päänäkymä 
#### Koti
- Voidaan lisätä uusi tehtävä (aikuinen) 
- Päivän tehtävät näkyvät listana
- Voidaan merkitä tehtävä tehdyksi ( lapsi)
#### Tehtävät
- Kaikkien käyttäjien tehtävät näkyvät (aikuinen)
- Tehtäviä voidaan poistaa (aikuinen)
- Kaikki omat tehtävät näkyvät (lapsi)
#### Perhe
- Kaikki perheenjäsenet näkyvät
- Aikuinen voi poistaa perheenjäseniä
#### Kirjaudu ulos 
- Sovelluksesta voidaan kirjautua ulos
### 404
- Sovellus antaa errorsivuston 404,  mikäli sivulle ei pääse


# Käyttöohje
### Rekisteröinti
- Voit rekisteröidä uuden käyttäjän painamalla etusivulla näkyvää Rekisteröidy- linkkiä

- Rekisteröimisvaiheessa, mikäli olet tehnyt jotain väärin, sovellus ilmoittaa siitä asiaankuuluvalla virheviestillä.
- Mikäli rekisteröinti onnistuu, sovellus ohjaa takaisin etusivulle.

### Kirjautuminen ja perheen lisäys
- Voit kirjautua tunnuksellasi sisään, ja sovellus ilmoittaa "Käyttäjätunnus tai salasana ei täsmää" mikäli syötät vääriä syötteitä.

- Mikäli valitsit käyttäjärooliksi aikuisen, voit luoda perheen. Perheelle tulee olla yksilöllinen nimi ja koodi, jolla lapsi voi liittyä perheeseen.
  - Voit kokeilla valmista perhettä käyttäjänimi:koodi salasana: koodi
  - 
- Mikäli valitsit käyttäjärooliksi lapsen, voit liittyä jo valmiiksi luotuun perheeseen 
  - Voit kokeilla liittyä valmiiseen perheeseen perheen nimi: testi koodi: testi1 
  - (Tai voit luoda aikuisen, tehdä perheen, ja liityä tähän lapsikäyttäjänä)

- Voit kirjautua perheen luonnin yhteydessä ulos, sovellus ohjaa takaisin kirjautumissivulle.
### Kirjautuneena

#### Koti
- Aikuisena näät kaikki perheenjäsenten tehtävät tältä päivältä listassa
- Aikuisena voit lisätä tehtävän perheenjäsenelle

- Pääsivulle päästessäsi, voit kirjautua ulos sivulta oikeasta yläkulmasta navigaatiopalkista.


## Puutteet

### Puutteet jotka korjataan sovellukseen
- Reititys ei toimi ( mikäli hakee sivua joka ei ole olemassa, tulee 404-error. Mutta muuten tulee ongelmia, jos ei ole sisäänkirjatunut. (tämän selvitän maanantaina)
- Oikeuksissa puutteita
- Tietoturvaa en ole tarkastellut
- Kirjautumisen jälkeinen ulkoasu (esim lomakkeilla) ei vastaa lopullista!
- Asetukset- sivu uupuu
- Yksi tietokantataulu (tasklists) putosi huonon suunnittelun tuloksena. Tilalle on tulossa jotain kunhan keksin mitä...
- Koodin muotoilu ei ole lopullinen! (eikös vscodeen ollut joku lisäke- joka taiteilee nuo ylimääräiset whitesp

### Kehitysideat jotka on otettu huomioon ja jotka korjataan jos aikaa jää
- Salasanaa tulisi rekisteröintivaiheessa kysyä kahdesti (saavutettavuus)
- Lapsen liittyessä perheeseen voisi kysyä vain koodia, eikä perhettä (saavutettavuus)
- Validointivirheilmoitukset annetaan yksi kerrallaan. Kaikki relevantit virheilmoitukset olisi hyvä näyttää kerralla. (käytettävyys)
