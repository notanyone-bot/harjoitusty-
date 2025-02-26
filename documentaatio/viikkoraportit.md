Viikkoraportti 1: Projektin aloitus ja suunnittelu
Tavoitteet:

Aloittaa shakkipelin tekoälyprojektin kehitys.
Suunnitella pelin peruslogiikka, pelin säännöt ja tekoälyn rakenne.
Työn eteneminen:

Suunniteltiin pelin peruslogiikka ja säännöt. Käsiteltiin shakki-pelin säännöt, siirrot, tarkistettiin kuinka pelissä voi liikkua eri nappuloilla, ja määriteltiin pelin voittokriteerit (esim. matti ja tasapeli).
Tekoälyn rakenteen suunnittelu aloitettiin. Päätettiin käyttää Minimax-algoritmia pelin tekoälyn toimintaan.
Haasteet ja ratkaisut:

Shakin sääntöjen täydellinen ymmärtäminen ja niiden ohjelmallinen toteuttaminen oli haaste. Ratkaisuksi päätettiin lähestyä ongelmaa yksinkertaisilla siirtojen tarkasteluilla ja sitten laajentaa pelin sääntöjä asteittain.
Tekoälyn rakenteen suunnittelu oli myös hankalaa, mutta päädyimme Minimax-algoritmiin.
Päivitykset GitHubiin:

Päivityksiä on tehty peruspelilogiikan ja shakin sääntöjen osalta, mutta eivät ole järjestyksessä.


Viikkoraportti 2: Pelin logiikka ja alustus
Tavoitteet:

Aloittaa pelin logiikan toteutus.
Luoda pelilauta ja perustoiminnot, kuten siirrot ja tarkistukset.
Työn eteneminen:

Pelilauta on toteutettu 2D-taulukon avulla, jossa sijoitetaan kaikki nappulat alkuasemiin.
Perustoiminnot, kuten siirtojen tarkistaminen ja pelin edistyminen (vuoron vaihto), on aloitettu.
Toteutettiin myös erillinen tarkistus shakin ja matinkin tilanteille.
Haasteet ja ratkaisut:

Nappuloiden liikkumisen tarkistaminen ja erityisesti erikoissiirrot, kuten tornitus, olivat aluksi haasteellisia. Tämä ratkaistiin lisäämällä tarkistuksia ja sääntöjä, jotka käsittelevät erityistilanteet.
Pelin edistyminen ja vuoron vaihtaminen vaativat huolellista suunnittelua, jotta peli voi siirtyä ilman virheitä.
Päivitykset GitHubiin:

Pelilauta ja peruslogiikka on lisätty, mutta ei täysin järjestyksessä.


Viikkoraportti 3: Tekoälyn Minimax-algoritmi
Tavoitteet:

Implementoida Minimax-algoritmi tekoälylle.
Arvioida siirrot ja valita paras mahdollinen siirto.
Työn eteneminen:

Minimax-algoritmi on aloitettu. Tekoäly käy läpi kaikki mahdolliset siirrot ja arvioi ne sen perusteella, miten ne vaikuttavat pelin lopputulokseen.
Pelissä käytettiin perus Minimax-tekniikkaa, jossa arvioitiin siirrot syvemmällä tasolla ja valittiin paras siirto.
Haasteet ja ratkaisut:

Minimax-algoritmin optimointi oli haastavaa, koska siirtojen määrän kasvaessa laskentateho oli suuri. Tätä ratkaistiin tekemällä optimointeja ja rajoittamalla syvyyttä.
Koodin toiminta ja suorituskyky parannettiin lisäämällä tehokkaampia algoritmeja siirtojen valintaan.
Päivitykset GitHubiin:

Minimax-algoritmi on lisätty projektiin, mutta ei järjestyksessä.


Viikkoraportti 4: Minimax-algoritmi ja syvyysoptimointi
Tavoitteet:

Jatkaa Minimax-algoritmin optimointia ja syvyyksien hallintaa.
Parantaa tekoälyn päätöksentekoa ja nopeuttaa sen toimintoja.
Työn eteneminen:

Minimax-algoritmi on optimoitu syvyyksien osalta, ja se alkaa rajoittaa arvioitavien siirtojen määrää, jotta laskenta-aikaa saataisiin vähennettyä.
Tekoäly pystyy nyt tekemään päätöksiä tehokkaammin ja paremmin, arvioimalla syvempiä siirtoja ilman liiallista suorituskyvyn heikkenemistä.
Haasteet ja ratkaisut:

Syvyyksien optimointi oli tärkeää, koska pelissä saattaa olla useita siirtoja, joiden laskenta vie paljon aikaa. Tähän tehtiin parannuksia, jotta tekoäly pystyy arvioimaan syvempiä siirtoja ilman huomattavaa suorituskyvyn heikkenemistä.
Pelissä esiintyvien virheiden korjaaminen ja tarkistusten lisääminen varmistivat, että peli toimii sujuvasti.
Päivitykset GitHubiin:

Syvyysoptimointi ja parannuksia Minimax-algoritmiin on lisätty, mutta ei täydellisessä järjestyksessä.


Viikkoraportti 5: Alpha-Beta Pruning ja optimointi
Tavoitteet:

Lisää Minimax-algoritmiin Alpha-Beta pruning, joka parantaa sen suorituskykyä.
Optimoida tekoälyn siirtojen arviointi ja nopeuttaa päätöksentekoa.
Työn eteneminen:

Alpha-Beta pruning lisättiin Minimax-algoritmiin. Tämä parantaa pelin tekoälyn suorituskykyä leikkaamalla pois turhat haaraumat ja nopeuttamalla päätöksentekoa.
Käytimme Alpha- ja Beta-arvoja, jotka estivät epärelevanttien pelitilanteiden tarkastelun ja paransivat tekoälyn reagointia pelissä.
Haasteet ja ratkaisut:

Alpha-Beta pruningin integrointi Minimaxiin vaati tarkkaa haaraumien hallintaa. Tämä onnistuttiin hyvin, ja peli voi nyt tarkastella siirtoja tehokkaammin.
Tekoäly reagoi nyt huomattavasti nopeammin ja pystyy tekemään parempia päätöksiä syvemmillä pelitilanteilla.
Päivitykset GitHubiin:

Päivitykset Alpha-Beta pruning -integraatiosta on lisätty, mutta ne eivät ole täysin järjestyksessä.