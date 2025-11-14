def lue_varaus():
    # Luetaan tiedosto
    with open("varaukset.txt", "r", encoding="utf-8") as f:
        rivi = f.readline().strip()

    
    osat = rivi.split("|")

    varausnumero = osat[0]
    varaaja = osat[1]
    pvm = osat[2]
    aloitusaika = osat[3]
    tuntimaara = float(osat[4])
    tuntihinta = float(osat[5])
    maksettu = osat[6]
    kohde = osat[7]
    puhelin = osat[8]
    sahkoposti = osat[9]

    # Laske kokonaishinta
    kokonaishinta = tuntimaara * tuntihinta

    # Tulostus täsmälleen vaaditussa muodossa
    print(f"Varausnumero: {varausnumero}")
    print(f"Varaaja: {varaaja}")
    print(f"Päivämäärä: {pvm}")
    print(f"Aloitusaika: {aloitusaika}")
    print(f"Tuntimäärä: {tuntimaara:g}")
    print(f"Tuntihinta: {tuntihinta} €")
    print(f"Kokonaishinta: {kokonaishinta} €")
    print(f"Maksettu: {maksettu}")
    print(f"Kohde: {kohde}")
    print(f"Puhelin: {puhelin}")
    print(f"Sähköposti: {sahkoposti}")


if __name__ == "__main__":
    lue_varaus()
