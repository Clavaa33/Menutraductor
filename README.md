# Menutraductor

**Aplicació web per traduir menús de restaurant mitjançant Intel·ligència Artificial**  
Pràctica 4 · Microsoft Azure · GDDV 2026

---

## Descripció

Menutraductor és una aplicació web que permet pujar una foto d'un menú de restaurant en qualsevol idioma i obtenir-ne la traducció automàtica a l'instant. L'aplicació combina dos serveis d'Azure AI per fer-ho possible:

1. **Azure Computer Vision** extreu el text de la imatge (OCR)
2. **Azure Translator** tradueix el text a l'idioma escollit

---

## Serveis d'Azure utilitzats

| Servei | Pla | Funció |
|--------|-----|--------|
| Azure App Service | Free F1 | Allotja i serveix l'aplicació web |
| Azure Computer Vision | Free F0 | Extreu el text de les imatges (OCR) |
| Azure Translator | Free F0 | Tradueix el text a l'idioma destí |

---

## Arquitectura

```
Usuari (navegador)
      │
      ▼
Azure App Service (Flask/Python)
      │
      ├──► Azure Computer Vision ──► Text extret
      │
      └──► Azure Translator ──► Text traduït
```

---

## Com desplegar el projecte

### Prerequisits

- Compte Azure (Azure for Students recomanat)
- Python 3.11+
- Git

### 1. Clona el repositori

```bash
git clone https://github.com/Clavaa33/Menutraductor.git
cd Menutraductor
```

### 2. Crea l'entorn virtual i instal·la dependències

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

### 3. Configura les variables d'entorn

Crea un fitxer `.env` a l'arrel del projecte:

```env
VISION_KEY=la_teva_clau_de_computer_vision
VISION_ENDPOINT=https://nom-recurs.cognitiveservices.azure.com/
TRANSLATOR_KEY=la_teva_clau_de_translator
TRANSLATOR_REGION=germanywestcentral
```

### 4. Executa en local

```bash
python app.py
```

Obre el navegador a `http://localhost:5000`

---

## Desplegament a Azure

### Recursos necessaris (Azure Portal)

1. **Resource Group**: `rg-traductor-menus` (regió: Germany West Central)
2. **Computer Vision**: pla Free F0
3. **Translator**: pla Free F0  
4. **App Service**: Python 3.11, Linux, pla Free F1

### Variables d'entorn a Azure

A l'App Service → Environment variables, afegeix:

```
VISION_KEY         = [clau de Computer Vision]
VISION_ENDPOINT    = [endpoint de Computer Vision]
TRANSLATOR_KEY     = [clau de Translator]
TRANSLATOR_REGION  = germanywestcentral
```

### Desplegament continu des de GitHub

App Service → Deployment Center → Source: GitHub → selecciona aquest repositori → branca `main` → Save.

---

## 📁 Estructura del projecte

```
Menutraductor/
├── templates/
│   └── index.html        # Interfície web
├── app.py                # Backend Flask (rutes OCR i traducció)
├── requirements.txt      # Dependències Python
├── startup.txt           # Configuració de gunicorn per Azure
├── .gitignore
└── README.md
```

---

## Idiomes suportats

Català · Castellà · Anglès · Francès · Alemany · Italià · Japonès · Xinès

Podem afegir més en funció de la demanda.

---

## Com utilitzar l'aplicació

1. Puja una foto d'un menú (JPG, PNG, WEBP)
2. Fes clic a **"Extreure text"** per detectar el text amb OCR
3. Selecciona l'idioma de destí
4. Fes clic a **"Traduir"**
5. Copia el resultat amb el botó **"Copiar"**

---

## Cost estimat

Tots els serveis fan servir el pla **Free** d'Azure:
- Computer Vision F0: 20 crides/minut, 5.000 crides/mes
- Translator F0: 2.000.000 caràcters/mes
- App Service F1: gratuït (60 minuts CPU/dia)

**Cost total: 0€**

---

## Autors

David Clavaguera Gomez (u1997650) i Àlex Cantos Gilabert (u1995380) · GDDV · Universitat de Girona · 2026
