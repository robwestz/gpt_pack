# Preflight Engine

⚠️ **ENFORCEMENT-DRIVEN**: Denna fil genererar KONKRET data för ENFORCEMENT LAYER.

---

## Publisher Analysis Algorithm (EXAKT, INTE ABSTRAKT)

### Domän-kategorisering

**Nyckelord → Kategori mapping:**

| Domäninnehåll | Kategori | Ton |
|---------------|----------|-----|
| hem, hus, bo, inred | Hem & Inredning | Varm, inspirerande |
| bil, motor, fordon | Motor | Teknisk, entusiastisk |
| hälsa, vård, medicin | Hälsa | Trovärdig, informativ |
| mat, recept, kök | Mat & Dryck | Avslappnad, personlig |
| teknik, it, digital | Teknik | Modern, kunnig |
| ekonomi, bank, finans | Ekonomi | Formell, auktoritativ |
| resa, semester, flyg | Resa | Drömsk, inspirerande |
| mode, stil, kläder | Mode | Trendig, personlig |
| sport, träning, gym | Sport | Energisk, motiverande |
| barn, familj, förälder | Familj | Omhändertagande, varm |

### Tonanalys

**Indicators för ton:**

```
FORMELL om:
- Domän slutar på .se (myndighet)
- Innehåller: konsument, verket, register
- B2B-orienterat innehåll

INFORMELL om:
- Blog i domännamn
- Livsstilsrelaterat
- Första person vanligt
```

### Typisk Artikellängd

| Kategori | Min | Optimal | Max |
|----------|-----|---------|-----|
| Nyheter | 400 | 600 | 800 |
| Livsstil/Blog | 800 | 1200 | 1800 |
| Guide/How-to | 1000 | 1500 | 2500 |
| Produktjämförelse | 1200 | 1800 | 3000 |
| Kort tips | 300 | 500 | 700 |

---

## Target Analysis Algorithm

### URL Parsing

**Extrahera information:**

```
https://exempel.se/kategori/produkt-namn?param=x
        ↓           ↓        ↓
      domain    category  product
```

**Regler:**

1. Domän → Identifiera varumärke
2. Path segments → Kategorier och ämnen
3. Slug → Primära keywords (ersätt - med mellanslag)

### Metadata Analysis (KRITISK FÖR VARIABELGIFTE!)

**OBLIGATORISK METADATA-EXTRAKTION:**

```python
def extract_target_metadata(url):
    return {
        "title": "[EXAKT title-tag]",  # Ex: "LED-strips för hemmet - Belysning.se"
        "description": "[EXAKT meta desc]",  # Ex: "Upptäck vårt sortiment av LED-strips..."
        "h1": "[EXAKT H1]",  # Ex: "LED-strips som förändrar ditt hem"
        "promise": "[VAD LOVAR DE?]",  # Ex: "Enkel installation, energieffektiv belysning"
        "keywords": "[EXTRAHERADE ORD]"  # Ex: ["LED", "strips", "belysning", "hem"]
    }
```

**ANVÄND METADATA FÖR VARIABELGIFTE:**

- Title avslöjar deras huvudlöfte → Din artikel MÅSTE leverera detta
- Description visar deras USP → Inkludera dessa fördelar
- H1 visar deras vinkel → Matcha eller överträffa

### Keyword Extraction

**Från anchor_text:**

- Dela i ord
- Filtrera stopp-ord (och, i, på, för, etc.)
- Identifiera huvudord

**Från URL-slug:**

- samma-som-anchor → konfirmerar keyword
- nya-ord → sekundära keywords

### Entity Identification

**Entitetstyper:**

| Typ | Exempel | Hur hitta |
|-----|---------|-----------|
| Produkt | iPhone 15 | Produktnamn i URL |
| Kategori | Smartphones | Path segment |
| Attribut | Trådlös | Adjektiv i slug |
| Varumärke | Apple | Domän eller path |
| Material | Aluminium | Produktbeskrivning |

---

## VARIABELGIFTE CALCULATION (ENFORCEMENT-KRITISK!)

### Steg 1: EXAKT Publisher-profil

```python
def analyze_publisher(domain):
    return {
        "core_topic": "[VAD skriver de om]",  # Ex: "skandinavisk design"
        "audience": "[VEM läser]",  # Ex: "designintresserade 25-45"
        "tone_rules": {
            "sentence_length": "max 20 ord",
            "pronouns": ["du", "din"],
            "style": "personlig men kunnig"
        }
    }
```

### Steg 2: EXAKT Target-analys

```python
def analyze_target(url, metadata):
    return {
        "product": "[EXAKT produkt/tjänst]",  # Ex: "LED-strips 5m RGB"
        "usp": "[Unik säljpunkt]",  # Ex: "App-styrning, energiklass A+"
        "promise": metadata["title"],  # Använd FAKTISK title
        "intent": "[commercial/informational]"
    }
```

### Steg 3: SKAPA VARIABELGIFTE (INTE "INTERSECT"!)

```python
def create_variable_marriage(publisher, target, anchor):

    # INGEN ABSTRAKT "HEMFÖRBÄTTRING"!
    # SKAPA KONKRET KOPPLING:

    marriage = {
        "base": f"{publisher.core_topic} möter {target.product}",
        "angle": "[SUPERSPECIFIK vinkel]",
        "examples": [
            "Hur [produkt] löser [publisher-publiks problem]",
            "Varför [publisher-ämne] behöver [target-lösning]"
        ]
    }

    return marriage
```

### KONKRETA VARIABELGIFTE-EXEMPEL

| Publisher | Target | EXAKT Gifte (inte "bridge") |
|-----------|--------|------------------------------|
| elledecoration.se | belysning.se/led | "Hur LED-strips framhäver Skandinaviska möblers linjer och färger" |
| mama.nu | leksaker.se/pussel | "Pedagogiska pussel som växer med barnet - från 1 till 5 år" |
| expressen.se/motor | däck.se/vinterdäck | "Säkerhetstest: Så presterar budgetdäck mot premiumdäck på is" |
| hälsa.se | kosttillskott.se/d-vitamin | "D-vitaminbrist i Norden - vad forskningen säger om dos och timing" |

---

## Risk Assessment

### Link Placement Risk

| Risk | Orsak | Åtgärd |
|------|-------|--------|
| LÅG | Stark intersect, naturlig kontext | Standardplacering |
| MEDIUM | Partiell intersect | Behöver wrapper-kontext |
| HÖG | Svag intersect | Skapa kreativ bridge |
| KRITISK | Ingen logisk koppling | Flagga för manuell granskning |

### Content Risk

**Varningsflaggor:**

- Anchor text är varumärke som publisher konkurrerar med
- Target är i direkt konflikt med publishers värderingar
- Ämnet är kontroversiellt (politik, religion, hälsopåståenden)

## SERP ANALYSIS (TVINGANDE FÖR ENFORCEMENT!)

```python
def analyze_serp_top3(keyword):
    results = []
    for i in range(3):
        results.append({
            "title": "[EXAKT titel]",
            "url": "[URL]",
            "winning_factor": "[VAD gör dem framgångsrika]",
            "structure": "[GUIDE/LISTICLE/HOW-TO]",
            "word_count": "[antal]",
            "sources_used": ["[källa1]", "[källa2]"],
            "key_topics": ["[ämne1]", "[ämne2]", "[ämne3]"],
            "content_gap": "[VAD saknas som vi kan fylla]"
        })

    return {
        "top3": results,
        "average_length": "[snitt ord]",
        "common_structure": "[vanligaste format]",
        "our_edge": "[VAD gör vår artikel unik]"
    }
```

## CONTEXT BOOSTER SELECTION (fd. Trust Links)

```python
def select_context_boosters(topic, serp_sources):

    # VÄLJ KÄLLOR SOM KONKURRENTER INTE ANVÄNDER!

    boosters = {
        "primary": {
            "type": "MYNDIGHET",
            "source": "[Energimyndigheten/Konsumentverket/etc]",
            "url": "[SPECIFIK sida, inte huvuddomän]",
            "supports": "[EXAKT påstående som stöds]"
        },
        "secondary": {
            "type": "BRANSCHORG",
            "source": "[Svensk Form/Byggkeramikrådet/etc]",
            "url": "[SPECIFIK sida]",
            "supports": "[EXAKT påstående]"
        },
        "tertiary": {
            "type": "MAINSTREAM",
            "source": "[DN/SvD/GP - specifik artikel]",
            "url": "[artikelURL]",
            "supports": "[EXAKT påstående]"
        }
    }

    # COMPETITOR FILTER:
    # ALDRIG länka till konkurrenter
    # ALDRIG samma källor som SERP topp 3
    # ALLTID specifika sidor, inte huvuddomäner

    return boosters
```

## LANDING PAGE ANALYSIS (SPECIAL MODE)

### "Winning Factors" Extraction

När vi skapar Landing Pages (Publisher == Target) letar vi INTE efter "Intersect". Vi letar efter **"Winning Factors"** hos konkurrenterna (Top 3 för Main Entity).

```python
def analyze_winning_factors(main_entity):
    competitors = search_google(main_entity, limit=3)
    
    analysis = {
        "intent_gap": "[Vad missar konkurrenterna i användarintention?]",
        "content_structure": "[Vilka sektioner har alla 3? T.ex. FAQ, Recensioner, Tabeller]",
        "brand_opportunity": "[Hur kan VÅRT varumärke göra detta bättre?]",
        "metadata_benchmark": {
            "avg_title_length": 55,
            "common_words": ["bästa", "2025", "test"],
            "suggestion": "Skapa mer klickvänlig och konverterande än dessa."
        }
    }
    return analysis
```

---

## Preflight Output Format

```json
{
  "publisher": {
    "domain": "hemmets.se",
    "category": "Hem & Inredning",
    "tone": "inspirerande",
    "typical_length": 1200
  },
  "target": {
    "url": "https://verktyg.se/borr",
    "primary_keyword": "borrmaskin",
    "entities": ["verktyg", "hemförbättring"],
    "intent": "commercial"
  },
  "variable_marriage": {
    "base": "Inredning möter LED-teknik",
    "angle": "Hur rätt belysning kan förstora små rum",
    "examples": ["Exempel 1", "Exempel 2"]
  },
  "context_boosters": [
    {
      "type": "MYNDIGHET",
      "source": "Energimyndigheten",
      "url": "https://...",
      "supports": "LED sparar 80% energi"
    }
  ],
  "risk_level": "LOW",
  "recommended_article_type": "GUIDE",
  "recommended_length": 1200
}
```
