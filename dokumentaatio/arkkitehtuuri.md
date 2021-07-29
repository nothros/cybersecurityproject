# Käyttöliittymäarkkitehtuuri ja toiminnallisuudet

<img src ="https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/pagesplan.png" width="750">

Kyseisessä luonnoksessa välissä oleva punainen viiva tarkoittaa, että riippuen käyttäjän roolista, on näkymä erilainen.


<img src ="https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/flow.png">


## Login/Register

- Näkymä koostuu yhteisestä layout.html sivusta.
- Alkunäkymässä näkyy Kirjautumisvaihtoehto, josta
-- voi kirjautua sisään
--  voi vaihtaa rekisteröintinäkymään
- Rekisteröintivaihtoehosta, josta voi
-- luoda käyttäjän jolloin uudelleen ohjaudutaan takaisin
-- voi vaihtaa takaisin kirjautumisnäkymään

- Sovellus antaa viesti-ilmoituksen kirjautuessa
-- mikäli käyttäjätunnus tai salasana ei täsmää
- Sovellus antaa viesti-ilmoituksen rekisteröityessä
-- mikäli käyttäjätunnus on jo käytössä
-- jokin kentistä on tyhjä
-- salasana on liian lyhyt
-- käyttäjätunnus on luotu onnistuneesti 

## Näkymä, kun perhettä ei ole luotu

- Mikäli käyttäjä on vanhempi
-- Voidaan luoda uusi perhe, perheelle annetaan nimi ja koodi, jolla perheeseen liitytään
-- Annetaan hänelle mahdollisuus liittyä olevassa olevaan perheeseen koodilla
- Mikäli käyttäjä on lapsi
-- Annetaan hänelle mahdollisuus liittyä olevassa olevaan perheeseen koodilla
Tästä näkymästä voidaan kirjautua ulos ja kirjautua eteenpäin itse sovellukseen.

## Päänäkymä

Päänäkymä koostuu yhteisesti navigaatiopalkista, joissa mahdollisuus

### Kotinäkymä

Mikäli tehtäviä ei ole
- Mikäli käyttäjä on lapsi
	-- Tulee hänelle ilmoitus ettei tehtäviä ole
- Mikäli käyttäjä on vanhempi 
	-- Tulee hänelle ilmoitus ettei tehtäviä ole, mutta voi silti lisätä tehtäviä
	
Mikäli tehtäviä on
- Käyttäjä on lapsi
-- Lapsi voi merkata tehtäviä tehdyksi
- Käyttäjä on vanhempi
-- Voi hän lisätä tehtäviä
-- Näkee hän päivän tehtävät (myös kenelle tehtävät on osoitettu)


### Tehtävät

Kummatkin käyttäjät voivat tarkastella annettuja ja tulevia tehtäviä ja niiden päivämääriä, mutta ainoastaan vanhempi näkee kaikki tehtävät, sekä kenelle ne on osoitettu, lapsi näkee vain omat tehtävänsä.

### Perhe

- Käyttäjä on lapsi
-- Lapsi näkee perheenjäsensä
- Käyttäjä on vanhempi
-- Näkee perheenjäsenensä
-- Voi poistaa perheenjäsenen
-- Voi poistaa perheen
-- Voi poistaa itsensä (koko perhe poistuu)


### Kirjaudu ulos
- Käyttäjä saa alert:n että haluaako hän kirjautua ulos


Tämän lisäksi on erillinen näkymä 404-sivuille.

