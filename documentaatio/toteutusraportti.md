Toteutusraportti

Työssä ei ole käytetty laajoja kielimalleja.

Ohjelman rakenne
Sovellus on shakki, jossa peli alkaa käynnistämällä main.py tiedosto VSCode-ympäristössä. Pelissä voi pelata joko tekoälyä vastaan tai kahden tekoälyn välillä. Pelissä käytetään Minimax-algoritmia ja Alpha-Beta pruningiä, mikä mahdollistaa tehokkaan päätöksenteon. Peli tukee siirtojen tekemistä hiirellä, ja virheelliset siirrot on estetty.

Ohjelman rakenne koostuu useista luokista. Pelaaja-luokka hallitsee pelaajan vuoroa, ja Peli-luokka hoitaa pelin logiikan, kuten siirrot, pelitilanteet ja pelin lopettamisen. Tekoäly-luokka käyttää Minimax- ja Alpha-Beta pruningiä valitakseen parhaan siirron. Pelissä on myös Shakki-taulu-luokka, joka pitää kirjaa laudalla olevista pelinappuloista ja tarkistaa sallitut siirrot.

Aikavaativuudet ja suorituskyky
Aikavaativuudet riippuvat siitä, kuinka syvälle tekoäly menee miettimään siirtoja. Minimax-algoritmi ilman optimointia toimii aikavaativuudella O(b^d), missä b on haarautumiskerroin ja d on syvyys, johon algoritmi menee. Alpha-Beta pruning optimoi tätä vähentämällä osan siirroista, mikä laskee aikavaativuuden parhaimmillaan O(b^(d/2)), mutta käytännössä tämä riippuu pelitilanteesta ja siitä, kuinka monta mahdollista siirtoa arvioidaan.

Pelissä oleva checkmate-algoritmi ja tornittamisen logiikka vaativat vielä lisädebuggausta ja optimointia. Tällä hetkellä algoritmi ei aina tunnista tarkasti tilanteita, joissa pelaaja on asettanut vastustajan shakkiin ja tehnyt matissa olevan siirron. Tämä voi johtaa virheellisiin pelitiloihin, joissa peli ei tunnista oikeanlaista lopetusta. Lisäksi tornittaminen saattaa epäonnistua tai aiheuttaa virheellisiä pelitiloja, erityisesti kuningas tai torni on liikkunut aiemmin. Tämä osuus tarvitsee tarkempaa virheiden käsittelyä ja optimointia.

Käytettävyys ja syötteiden validointi
Sovellusta käytetään sekä hiirellä että klikkamalla laudan ruutuja, jolloin pelaaja voi siirtää nappuloitaan. Koska ohjelma estää virheelliset siirrot, pelaajat eivät voi tehdä laittomia liikkeitä. Käytettävissä on myös pikakomennot, jotka ohjaavat peliä.

Puutteet ja parannusehdotukset
Checkmate-algoritmi vaatii lisää debuggausta ja optimointia, koska se ei aina tunnista tarkasti tilanteita, joissa peli päättyy mattiin. Tämä johtaa virheellisiin pelitiloihin, joissa peli ei tunnista oikeanlaista lopetusta. Tornittaminen tarvitsee tarkempaa logiikkaa ja virheidenhallintaa, erityisesti silloin, kun kuningas tai torni on liikkunut aiemmin.

Kehityksessä voisi parantaa myös käyttöliittymää tarjoamalla selkeämmän tavan hallita pelin tilaa ja siirtoja, kuten visuaalisia ilmoituksia matista tai pelin päättymisestä. Tämä parantaisi pelin käytettävyyttä ja tekisi siitä entistä intuitiivisemman.