# joojoo!- TodoApp perheille

![sovelluksen logo](https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/logo2.png)

## Sovelluksen käyttötarkoitus

Sovellus on tarkoitettu perheiden kotitöiden jakamiseen ja niiden tekemisen tarkkailuun. Vanhemmat voivat lisätä lapsilleen kotitöitä, 
joita lapset puolestaan voivat merkitä tehdyiksi. Tehtävän voi määrittää yhdelle lapselle kerrallaan. Sovellukseen tulee luoda käyttäjätunnus
ja vanhempi voi lisätä perheen johon lapsi voi liittyä. Lapsen toiminta sovelluksessa on rajoitetumpaa, hän ei voi poistaa omaa käyttäjätunnustaan, eikä poistua perheestä.


## Linkki sovellukseen
[https://joojoo-app.herokuapp.com/](https://joojoo-app.herokuapp.com/)


## Linkit sovelluksen dokumentaatioon


[Toiminnallisuus](#toiminnallisuus)

[Käyttöohje](#käyttöohje)

[Puutteet](#puutteet)

[Arkkitehtuurikuvaus](https://github.com/nothros/ToDoApp-for-families/blob/main/dokumentaatio/arkkitehtuuri.md) (linkki ohjaa toiseen tiedostoon)


# Toiminnallisuus
### (22.8.2021)

### Kirjautuminen/Rekisteröinti
- Voidaan luoda uusi käyttäjä
- Voidaan kirjautua sisään
### Mikäli perhettä ei ole vielä luotu
- Voidaan luoda uusi perhe (aikuinen)
- Voidaan liittyä perheeseen (lapsi)
- Näkymästä voi kirjautua ulos
### Päänäkymä 
#### Koti
- Voidaan lisätä uusi tehtävä (aikuinen) 
- Päivän tehtävät näkyvät listana, aikuisella kaikkien lapsella vain omat
- Tehtävät voidaan merkitä tehtävä tehdyksi, tai kumota (lapsi)
#### Tehtävät
- Kaikkien käyttäjien tehtävät näkyvät (aikuinen)
- Tehtäviä voidaan poistaa (aikuinen)
- Kaikki omat tehtävät näkyvät, menneet ja tulevat (lapsi)
#### Perhe
- Kaikki perheenjäsenet näkyvät (lapsi ja aikuinen)
- Aikuinen voi poistaa perheenjäseniä (aikuinen)
#### Kirjaudu ulos 
- Sovelluksesta voidaan kirjautua ulos
### 404
- Sovellus antaa errorsivuston 404,  mikäli sivulle ei pääse tai sitä ei ole olemassa.


# Käyttöohje
### Rekisteröinti
- Voit rekisteröidä uuden käyttäjän painamalla etusivulla näkyvää Rekisteröidy- linkkiä

- Rekisteröimisvaiheessa, mikäli olet tehnyt jotain väärin, sovellus ilmoittaa siitä asiaankuuluvalla virheviestillä.
- Mikäli rekisteröinti onnistuu, sovellus ohjaa takaisin etusivulle.

### Kirjautuminen ja perheen lisäys
- Voit kirjautua tunnuksellasi sisään. Sovellus ilmoittaa "Käyttäjätunnus tai salasana ei täsmää" mikäli syötät vääriä syötteitä.

- Mikäli valitsit käyttäjärooliksi aikuisen, voit luoda perheen. Perheelle tulee olla yksilöllinen nimi ja koodi, jolla lapsi voi liittyä perheeseen.
  - Voit kokeilla valmista perhettä kirjautumalla aikuisena
  -- Käyttäjätunnus: testi Salasana: testi
  
- Mikäli valitsit käyttäjärooliksi lapsen, voit liittyä jo valmiiksi luotuun perheeseen 
  - Voit kokeilla liittyä valmiiseen perheeseen perheen nimi: testi koodi: testi
  - (Tai voit luoda aikuisen, tehdä perheen, ja liityä tähän lapsikäyttäjänä)

- Voit kirjautua perheen luonnin yhteydessä ulos, sovellus ohjaa takaisin kirjautumissivulle.
### Kirjautuneena

#### Koti
- Aikuisena näät kaikki perheenjäsenten tehtävät tältä päivältä listassa
- Aikuisena voit lisätä tehtävän perheenjäsenelle

- Lapsena näät kaikki sinulle annetut tehtävät
- Voit lapsena kirjata tehtävät tehdyksi

#### Tehtävälista
- Aikuisena voit tarkastella kaikkien perheenjäsenten kaikkia tehtäviä
- Lapsena voit tarkastella kaikkia omia tehtäviäsi (tehtyjä ja tekemättömiä ja tulevia)

#### Perhe
- Aikuisena näät kaikki perheenjäsenet ja voit poistaa perheenjäsenen kokonaan (muttet itseäsi)
- Lapsena näät kaikki perheenjäsenesi

#### Asetukset
- Sivulla ei ole vielä toimintaa

#### Kirjaudu ulos 
- Pääsivulle päästessäsi, voit kirjautua ulos sivulta oikeasta yläkulmasta navigaatiopalkista.


## Puutteet

### Puutteet jotka korjataan sovellukseen
- Kirjautumisen jälkeinen ulkoasu (esim lomakkeilla) ei vastaa lopullista!
- Asetukset- sivu uupuu
- Yksi tietokantataulu (tasklists) putosi huonon suunnittelun tuloksena. Tilalle on tulossa status- taulu, jolla tehtyjen tehtävien statukset selkeyttää näkymää
- Oikeuksissa puutteita (Toteutettu hassusti ilman tokenia, korjataan)
- Mikäli palataan sivulle, jonne ei ole oikeutta, ei tulekaan 404- sivua. Korjataan.
- Tietoturvaa en ole tarkastellut
- Koodin muotoilu ei ole lopullinen

### Kehitysideat jotka on otettu huomioon ja jotka korjataan jos aikaa jää
- Salasanaa tulisi rekisteröintivaiheessa kysyä kahdesti (saavutettavuus)
- Lapsen liittyessä perheeseen voisi kysyä vain koodia, eikä perhettä (saavutettavuus)
- Validointivirheilmoitukset annetaan yksi kerrallaan. Kaikki relevantit virheilmoitukset olisi hyvä näyttää kerralla. (käytettävyys)
