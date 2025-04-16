Vaatimusmäärittely
Opinto-ohjelma: Tietojenkäsittelytiede, kandidaatin tutkinto

Projekti on komentoriviltä käytettävä shakki, jossa voi pelata joko tekoälyä vastaan tai kahden tekoälyn välillä. Pelissä on käytössä Minimax-algoritmi ja Alpha-Beta pruning. Pelissä voidaan tehdä siirtoja joko hiirellä tai automaattisesti tekoälyn kanssa. Ohjelma tunnistaa virheelliset siirrot ja estää niiden tekemisen.

Shakki-peli toimii komentoriviltä ja voidaan käynnistää suorittamalla main.py-tiedoston. Pelissä voidaan pelata joko pelaajaa vastaan tai tekoälyä vastaan. Tekoäly käyttää Minimax-algoritmia ja Alpha-Beta pruningia valitakseen parhaan mahdollisen siirron. Pelissä voidaan myös pelata kahden tekoälyn välillä. Virheelliset siirrot on estetty, joten pelaaja ei voi tehdä laittomia liikkeitä.

Peli hallitsee pelilautaa ja pelinappuloita Shakki-taulu-luokan avulla. Pelissä on erillinen Tekoäly-luokka, joka käyttää Minimax-algoritmia tekoälyn päätöksentekoon ja optimoi sen Alpha-Beta pruningilla. Pelaaja-luokka hoitaa pelaajan vuoroa ja siirtojen tekemistä. Pelissä on myös mahdollisuus tarkistaa matitilanteet ja peli voidaan lopettaa, jos toinen pelaaja on voittanut.

Aikavaativuudet ja suorituskyky
Minimax-algoritmin aikavaativuus on O(b^d), missä b on haarautumiskerroin (siirtojen määrä) ja d on syvyys. Alpha-Beta pruning optimoi tätä vähentämällä tutkittavien siirtojen määrää, jolloin aikavaativuus on parhaimmillaan O(b^(d/2)). Aikavaativuus riippuu siitä, kuinka pitkälle tekoäly menee miettimään siirtoja. Checkmate-algoritmi ja tornittaminen vaativat lisää optimointia ja debuggausta, koska ne eivät aina tunnista tarkasti matissa tai tornittamisessa olevia tilanteita.

Tekniset vaatimukset

Sovellus toimii unix-pohjaisissa käyttöjärjestelmissä.
Python-version tulee olla vähintään 3.10.
Sovelluksen kieli on suomi.
Toiminnalliset vaatimukset

Shakki voidaan käynnistää komentoriviltä.
Peli voi pelata joko pelaajaa vastaan tai kahden tekoälyn välillä.
Tekoäly käyttää Minimax-algoritmia ja Alpha-Beta pruningia päätöksentekoon.
Pelaaja voi tehdä siirtoja joko hiirellä.
Virheelliset siirrot estetään eikä niitä voida tehdä.
Pelissä voidaan tarkistaa matitilanteet ja peli voi päättyä mattiin.
Tornittaminen on tuettu, mutta se tarvitsee tarkempaa virheiden käsittelyä.
Pelissä voi pelata kahden tekoälyn välillä ja tarkistaa pelitilanteen.
Sovellus voi tarjota käyttöliittymän, jossa näkyy pelin tila ja siirrot.
Sovellus tarjoaa myös mahdollisuuden tulostaa pelin tilan ja analysoida tekoälyn siirtojen tehokkuutta.
Puutteet ja parannusehdotukset

Checkmate-algoritmi ja tornittaminen tarvitsevat lisää debuggausta ja optimointia. Tällä hetkellä algoritmit eivät aina tunnista tarkasti matissa tai tornittamisessa olevia tilanteita, mikä voi johtaa virheellisiin pelitiloihin.
Tekoälyn päätöksenteko voisi hyötyä entistä paremmasta syvyyden optimoinnista, jotta se ei mene liian syvälle tilanteissa, joissa ei ole järkeä.
Pelissä voisi olla graafinen käyttöliittymä, mutta se ei ole toteutettu tällä hetkellä. Sen sijaan komentorivikäyttöliittymä tarjoaa joustavuutta, mutta vaatii virheiden hallinnan parantamista.