from datetime import date, time
import os

def parse_bool(s):
    s = s.strip()
    return s in ("True", "true", "1", "Kyllä", "kyllä", "yes", "Yes")

def fmt_number_trim(x):
    # Muotoile numero niin että turhat nollat katoavat (39.90 -> 39.9, 40.00 -> 40)
    s = f"{x:.2f}"
    s = s.rstrip("0").rstrip(".")
    return s

def käsittele_rivi(rivi, lineno):
    parts = rivi.strip().split("|")
    if len(parts) < 10:
        print(f"[Rivi {lineno}] Virhe: odotettiin 10 saraketta, löytyi {len(parts)}. Rivi: {rivi!r}")
        return

    try:
        varausnumero = int(parts[0].strip())
    except ValueError:
        print(f"[Rivi {lineno}] Virhe: varausnumero ei ole int: {parts[0]!r}")
        return

    varaaja = parts[1].strip()

    # Päivämäärä: yyy-mm-dd -> date
    try:
        varauspaiva = date.fromisoformat(parts[2].strip())
    except Exception as e:
        print(f"[Rivi {lineno}] Virhe päivämäärän parsinnassa ({parts[2]!r}): {e}")
        return

    # Aika: HH:MM -> time
    try:
        aloitusaika = time.fromisoformat(parts[3].strip())
    except Exception as e:
        print(f"[Rivi {lineno}] Virhe ajan parsinnassa ({parts[3]!r}): {e}")
        return

    try:
        tuntimaara = int(parts[4].strip())
    except ValueError:
        print(f"[Rivi {lineno}] Virhe: tuntimäärä ei ole int: {parts[4]!r}")
        return

    try:
        tuntihinta = float(parts[5].strip())
    except ValueError:
        print(f"[Rivi {lineno}] Virhe: tuntihinta ei ole float: {parts[5]!r}")
        return

    maksettu_raw = parts[6].strip()
    maksettu_bool = parse_bool(maksettu_raw)
    maksettu = "Kyllä" if maksettu_bool else "Ei"

    kohde = parts[7].strip()
    puhelin = parts[8].strip()
    sahkoposti = parts[9].strip()

    kokonaishinta = tuntimaara * tuntihinta

    # Tulostus
    print(f"Varausnumero: {varausnumero}")
    print(f"Varaaja: {varaaja}")
    print(f"Päivämäärä: {varauspaiva.day}.{varauspaiva.month}.{varauspaiva.year}")
    print(f"Aloitusaika: {aloitusaika.strftime('%H:%M')}")
    print(f"Tuntimäärä: {tuntimaara}")
    print(f"Tuntihinta: {fmt_number_trim(tuntihinta)} €")
    print(f"Kokonaishinta: {fmt_number_trim(kokonaishinta)} €")
    print(f"Maksettu: {maksettu}")
    print(f"Kohde: {kohde}")
    print(f"Puhelin: {puhelin}")
    print(f"Sähköposti: {sahkoposti}")
    print()  # tyhjä rivi rivien väliin

def main():
    path = "varaukset.txt"
    if not os.path.exists(path):
        print(f"Virhe: tiedostoa '{path}' ei löytynyt. Varmista että se on samassa kansiossa skriptin kanssa.")
        return

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Varoitus: tiedosto on tyhjä.")
        return

    for i, line in enumerate(lines, start=1):
        if line.strip() == "":
            continue
        käsittele_rivi(line, i)

if __name__ == "__main__":
    main()

  
