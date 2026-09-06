# dashboard

Osobný dashboard na sledovanie váhy, obvodov a tréningov, publikovaný cez GitHub Pages.

Stránka je statická a **dáta v nej sú zašifrované (AES-256-GCM)**. Dešifrovací kľúč
nie je v repozitári — je súčasťou URL fragmentu (`#k=…`), ktorý prehliadač neodosiela
na server. Bez neho je `data.json` len nečitateľný blok bajtov.

| Súbor | Obsah |
|---|---|
| `index.html` | statická schránka dashboardu (grafy, výpočty, rozhranie) |
| `data.json` | zašifrované merania — jediný súbor, ktorý sa mení pri novom zázname |
| `build.py` | zašifruje `measurements.json` do `data.json` |

`measurements.json` (čitateľné merania) a `key.txt` (kľúč) sú zámerne mimo
repozitára — sú uložené len v tomto Claude projekte.

## Zostavenie

```
python3 build.py        # measurements.json + key.txt -> out/data.json
```
