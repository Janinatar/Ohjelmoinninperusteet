from datetime import datetime, date, time

def lue_varaus():
    # Luetaan rivin sisältö
    with open("varaukset.txt", "r", encoding="utf-8") as f:
        rivi = f.readline().strip()

    # Erotellaan tiedot | merkillä
    osat = rivi.split("|")

    # Puretaan tiedot muuttujiin
    varausnumero = int(osat[0])                         # int
    varaaja = osat[1]                                   # str

    # Päivämäärä: "2025-10-31" -> datetime.date
    varauspaiva = date.fromisoformat(osat[2])

    # Aika: "10:00" -> datetime.time
    aloitusaika = time.fromisoformat(osat[3])

    tuntimaara = int(osat[4])                           # int
    tuntihinta = float(osat[5])                         # float
    maksettu = osat[6] == "True"                        # bool

    kohde = osat[7]                                     # str
    puhelin = osat[8]                                   # str
    sahkoposti = osat[9]                                # str

    # Lasketaan kokonaishinta
    kokonaishinta = tuntimaara * tuntihinta

    # Tulostetaan vaaditussa muodossa
    print(f"Varausnumero: {varausnumero}")
    print(f"Varaaja: {varaaja}")
    print(f"Päivämäärä: {varauspaiva.day}.{varauspaiva.month}.{varauspaiva.year}")
    print(f"Aloitusaika: {aloitusaika.strftime('%H:%M')}")
    print(f"Tuntimäärä: {tuntimaara}")
    print(f"Tuntihinta: {tuntihinta} €")
    print(f"Kokonaishinta: {kokonaishinta} €")
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    print(f"Kohde: {kohde}")
    print(f"Puhelin: {puhelin}")
    print(f"Sähköposti: {sahkoposti}")


if __name__ == "__main__":
    lue_varaus()
