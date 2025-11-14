def lue_varaus():
    # Luetaan tiedoston ensimmäinen rivi
    with open("varaukset.txt", "r", encoding="utf-8") as f:
        rivi = f.readline().strip()

    # Erotellaan tiedot |-merkin perusteella
    (
        varausnumero,
        varaaja,
        pvm_raw,
        aloitusaika,
        tuntimaara_raw,
        tuntihinta_raw,
        maksettu_raw,
        kohde,
        puhelin,
        sahkoposti
    ) = rivi.split("|")

    # Muunnetaan tietotyypit
    # Päivämäärä muotoon DD.MM.YYYY
    yyyy, mm, dd = pvm_raw.split("-")
    pvm = f"{dd}.{mm}.{yyyy}"

    tuntimaara = float(tuntimaara_raw)
    tuntihinta = float(tuntihinta_raw)
    kokonaishinta = tuntimaara * tuntihinta

    # Muutetaan True/False -> Kyllä/Ei
    maksettu = "Kyllä" if maksettu_raw == "True" else "Ei"

    # Tulostus vaaditussa muodossa
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