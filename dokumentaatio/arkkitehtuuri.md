# Käyttöliittymäarkkitehtuuri ja toiminnallisuudet

## Sovelluksen käyttötarkoitus

Sovellus on tarkoitettu perheiden kotitöiden jakamiseen ja niiden tekemisen tarkkailuun. Vanhemmat voivat lisätä lapsilleen kotitöitä, 
joita lapset puolestaan voivat merkitä tehdyiksi. Tehtävän voi määrittää yhdelle lapselle kerrallaan. Sovellukseen tulee luoda käyttäjätunnus
ja vanhempi voi lisätä perheen.

## Käyttäjät
Sovelluksella on kaksi käyttäjäroolia. Vanhempi ja lapsi. Vanhempi hallinnoi perheitä ja lapset merkitsevät tehtäviä tehdyiksi.

## Käyttöliittymäluonnos
![ruudunkaappaus kirjautumissivusta](https://raw.githubusercontent.com/nothros/TodoApp-for-families/main/dokumentaatio/loginpagescreenshot.png)
(Yllä kuva sovelluksen kirjautumissivusta) <br />


<img src ="https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/pagesplan2.png" width="750">

Kyseisessä luonnoksessa välissä oleva punainen viiva tarkoittaa, että riippuen käyttäjän roolista, on näkymä erilainen. Vuokaavio kuvaa sivujen yhteyttä toisiinsa.


<img src ="https://raw.githubusercontent.com/nothros/ToDoApp-for-families/main/dokumentaatio/flow.png">


## Login/Register

- Näkymä koostuu yhteisestä layout.html sivusta.
- Alkunäkymässä näkyy Kirjautumisvaihtoehto, josta
	- voi kirjautua sisään
	- voi vaihtaa rekisteröintinäkymään
- Rekisteröintivaihtoehosta, josta voi
	- luoda käyttäjän jolloin uudelleen ohjaudutaan takaisin
	- voi vaihtaa takaisin kirjautumisnäkymään

- Sovellus antaa viesti-ilmoituksen kirjautuessa
	- mikäli käyttäjätunnus tai salasana ei täsmää
- Sovellus antaa viesti-ilmoituksen rekisteröityessä
	- mikäli käyttäjätunnus on jo käytössä
	- jokin kentistä on tyhjä
	- salasana on liian lyhyt

## Näkymä, kun perhettä ei ole luotu

- Mikäli käyttäjä on vanhempi
	- Voidaan luoda uusi perhe, perheelle annetaan nimi ja koodi, jolla perheeseen liitytään
- Mikäli käyttäjä on lapsi
	- Annetaan hänelle mahdollisuus liittyä olevassa olevaan perheeseen koodilla
Tästä näkymästä voidaan kirjautua ulos ja kirjautua eteenpäin itse sovellukseen.

## Päänäkymä

Päänäkymä koostuu yhteisesti navigaatiopalkista, joissa mahdollisuus

### Kotinäkymä

Mikäli tehtäviä ei ole
- Mikäli käyttäjä on lapsi
	- Tulee hänelle ilmoitus ettei tehtäviä ole
- Mikäli käyttäjä on vanhempi 
	- Tulee hänelle ilmoitus ettei tehtäviä ole, mutta voi silti lisätä tehtäviä
	
Mikäli tehtäviä on
- Käyttäjä on lapsi
	- Lapsi voi merkata tehtäviä tehdyksi
	- Lapsi näkee tehtäväedistymisen palkissa
- Käyttäjä on vanhempi
	- Voi hän lisätä tehtäviä
	- Näkee hän päivän tehtävät (myös kenelle tehtävät on osoitettu)


### Tehtävät

Kummatkin käyttäjät voivat tarkastella annettuja ja tulevia tehtäviä ja niiden päivämääriä, mutta ainoastaan vanhempi näkee kaikki tehtävät, sekä kenelle ne on osoitettu, lapsi näkee vain omat tehtävänsä.
Aikuinen voi myös poistaa tehtäviä

### Perhe

- Käyttäjä on lapsi
	- Lapsi näkee perheenjäsensä
- Käyttäjä on vanhempi
	- Näkee perheenjäsenensä
	- Voi poistaa perheenjäsenen
	- Voi poistaa itsensä (jolloin perhe poistuu)


### Kirjaudu ulos

Tämän lisäksi on erillinen näkymä 404-sivuille.

