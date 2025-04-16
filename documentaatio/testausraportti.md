Testausraportti
26.02.2025

Yksikkötestaus
Yksikkötestauksessa testataan Shakki-luokka sekä peliin liittyvät toiminnot. Virheelliset siirrot on otettu pois ohjelmasta, joten ne eivät ole enää testattavia. Testauksessa keskitytään sovelluksen toimintaan oikeanmuotoisilla syötteillä.

Käyttöliittymätestaus
Käyttöliittymätestaus toteutetaan manuaalisesti erikseen suunniteltuja testitapauksia hyödyntäen. Manuaalitestauksessa keskitytään erityisesti pelin toimintaan ja käytettävyyteen.

Käyttöliittymätestauksen testitapaukset

Sovelluksen peruskäyttö:
Peli käynnistyy VSCode:sta main.py-tiedoston suorittamisella. Käyttäjä voi pelata joko itse tai valita AI:n pelaamaan hänen kanssaan tai toisen AI:n kanssa. Pelissä ei ole mahdollista tehdä virheellisiä siirtoja, vaan peli hylkää virheelliset siirrot automaattisesti.

Siirtojen toimivuus:
Pelin aikana käyttäjä tekee siirron, kuten e2-e4. Jos siirto on laillinen, se toteutuu ja peli jatkuu. Jos siirto on virheellinen, ohjelma estää sen.

AI:n toiminta:
AI pelaa joko käyttäjän kanssa tai toista AI:tä vastaan. Pelissä valitaan vaikeustaso ja AI pelaa sen mukaan.

Pelin lopetus:
Peli päättyy, kun toinen pelaaja antaa shaakin tai matinkin, tai jos peli päättyy tasapeliin. Tämä huomioidaan pelin logiikassa ja loppu näkyy selkeästi pelissä.

Aikavaativuus
Pelissä käytetään Minimax-algoritmia päätöksenteon tukena, jossa AI arvioi mahdollisia siirtoja ja valitsee parhaimman vaihtoehdon. Minimaxin aikavaativuus kasvaa siirtojen syvyyden myötä, ja sen aikavaativuus on O(b^d), missä b on haarautumistekijä (mahdollisten siirtojen määrä kussakin tilanteessa) ja d on syvyyden määrä (siirtojen määrä, jonka AI arvioi). Tämä tarkoittaa, että mitä syvemmälle AI menee pohdinnassaan, sitä enemmän laskentatehoa tarvitaan.

Alpha-Beta pruning on optimointi Minimax-algoritmille, joka vähentää turhien haarojen tutkimista. Tämä vähentää laskentatehoa ja parantaa suorituskykyä. Alpha-Beta pruningin aikavaativuus on keskimäärin O(b^(d/2)), mutta se voi parhaimmillaan kutistua lähemmäs O(b^d), jos optimointi ei toimi tehokkaasti.

AI:n laskentatehon tarve riippuu siitä, kuinka pitkälle AI päättää miettiä siirtojaan. Mitä syvemmälle AI menee analyysissään, sitä suuremmaksi aikavaativuus kasvaa. Tämän vuoksi käyttäjä voi valita vaikeustason, joka määrittää, kuinka pitkälle AI menee siirron arvioinnissa ja kuinka paljon laskentatehoa käytetään.

Muu testaus
Shakin pelin käyttämät tietorakenneoperaatiot toimivat aikavaativuudella O(1). Pääosa pelin toiminnoista, kuten siirtojen tarkistaminen ja pelilauta, toimii aikavaativuudella O(n), missä n on siirtojen määrä.

Suorituskykytestaus ei ole tarpeen, sillä pelissä käsiteltävien siirtojen määrä ei ole suuri, mutta AI:n syvyysparametrin mukaan pelin vaikeusaste ja tarvittava laskentateho voivat vaihdella.