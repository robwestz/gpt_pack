# Writer Engine

⚠️ **ENFORCEMENT-DRIVEN**: OBLIGATORISKA CHECKPOINTS & ABORT CONDITIONS!

---

## 🔴 KRITISKA REGLER FRÅN ENFORCEMENT LAYER

1. **PAUSA var 200:e ord** för checkpoint-validering
2. **ABORT om AI-markörer detekteras**
3. **VARIABELGIFTE måste etableras inom 300 ord**
4. **Ankarlänk MÅSTE placeras före 800 ord**

---

## 🌊 FLOW ENFORCEMENT (NY KRITISK REGEL)

**KÄRNPROBLEMET:** AI tenderar att skriva "blockigt" (Intro -> H2 -> H2) utan sammanhang.
**LÖSNINGEN:** Du måste väva en "Röd Tråd".

1. **Inga isolerade öar:** Varje nytt stycke måste referera tillbaka till det föregående. Använd inte "Nästa steg är..." utan "När du har gjort detta, blir det naturligt att...".
2. **Berättande Jag:** Använd ett konsekvent berättarröst. Om du är en expert, behåll den rollen mellan sektionerna. Skifta inte till Wikipedia-ton.
3. **Substans över Struktur:** Struktur (H2) är bara ett skelett. Din text är kroppen. Fyll den med kött (fakta) och blod (känsla), inte bara hud (ord).
4. **Förbud mot Start-Stopp:** Varje rubrik ska kännas som en naturlig fortsättning på resonemanget, inte en ny start.

---

## Artikeltyper

### GUIDE (Informativ)

**När användas:**

- Ämnet kräver förklaring
- Läsaren vill lära sig
- Sökintent: informational

**Struktur:**

```markdown
## [Ämne]: Komplett guide för [målgrupp]

### Vad är [ämne]?
[Förklaring + kontext]

### Varför är [ämne] viktigt?
[Fördelar + relevans]

### Hur väljer du rätt [ämne]?
[Tips + faktorer att tänka på]
← ANKARLÄNK PLACERAS HÄR

### Vanliga misstag att undvika
[Warnings + praktiska råd]

### Sammanfattning
[Kort recap]
```

### HOW_TO (Praktisk)

**När användas:**

- Konkret problem att lösa
- Steg-för-steg process
- Sökintent: navigational/transactional

**Struktur:**

```markdown
## Så gör du: [handling] - steg för steg

### Innan du börjar
[Förberedelser + vad du behöver]

### Steg 1: [Första åtgärden]
[Instruktion]

### Steg 2: [Andra åtgärden]
[Instruktion]
← ANKARLÄNK PLACERAS HÄR

### Steg 3: [Tredje åtgärden]
[Instruktion]

### Tips för bästa resultat
[Extra råd]
```

### LISTICLE (Jämförelse)

**När användas:**

- Jämföra alternativ
- Ge översikt
- Sökintent: commercial investigation

**Struktur:**

```markdown
## X bästa [kategori] 2024

### Varför [kategori] är viktigt
[Intro + kontext]

### 1. [Alternativ A]
[Beskrivning + för/nackdelar]
← TRUST LINK

### 2. [Alternativ B]
[Beskrivning + för/nackdelar]
← ANKARLÄNK PLACERAS HÄR

### 3. [Alternativ C]
[Beskrivning + för/nackdelar]

### Så väljer du rätt för dig
[Köpguide]
```

---

## Skrivregler med ENFORCEMENT CHECKPOINTS

### CHECKPOINT @ 200 ORD ✓

```python
def checkpoint_200():
    validate = {
        "variabelgifte_etablerat": True/False,
        "entities_nämnda": count >= 2,
        "persona_korrekt": True/False,
        "ai_markörer": count == 0
    }
    if not all(validate.values()):
        ABORT_AND_RESTART()
```

### Inledning (150-200 ord)

**TVINGANDE KRAV:**

- MÅSTE etablera variabelgifte inom första 150 ord
- MÅSTE nämna minst 1 required entity
- MÅSTE matcha publisher-ton från ord 1

**FÖRBJUDNA FRASER (=OMEDELBAR ABORT):**

- ❌ "I dagens samhälle..."
- ❌ "Det har blivit allt viktigare..."
- ❌ "Har du någonsin undrat..."
- ❌ "Det är viktigt att notera..."
- ❌ "Låt oss utforska..."

**OBLIGATORISKA intro-varianter (välj 1):**

```
STATISTIK: "[Siffra]% av [målgrupp] [relevant fakta]..."
SCENARIO: "Du står i [situation] och [problem/behov]..."
DIREKT: "[Ämne] har [utveckling/förändring]..."
FRÅGA: "Visste du att [överraskande men sant faktum]?"
BERÄTTELSE: "När [person/jag] [händelse], blev det tydligt att..."
```

### Mellanrubriker (H2)

**Regler:**

- Beskrivande, inte clickbait
- Inkludera keyword om naturligt
- Max 8 ord

**DO:** "Så väljer du rätt borrmaskin för ditt hem"
**DON'T:** "Detta kommer förändra allt"

### Stycken

**Regler:**

- Max 4-5 meningar per stycke
- Variera meningslängd
- Undvik passiv form

### Meningar

**Target LIX 35-45:**

- Blanda korta (8-12 ord) och längre (15-25 ord)
- Undvik meningar över 30 ord
- Aktiv form: "Du bör" istället för "Det bör"

---

## Länkplacering med ENFORCEMENT

### CHECKPOINT @ 400 ORD ✓

```python
def checkpoint_400():
    validate = {
        "fortfarande_rätt_persona": True/False,
        "serp_insights_används": count >= 1,
        "förbereder_för_ankarlänk": True/False,
        "ingen_ai_drift": True/False
    }
    if not all(validate.values()):
        ABORT_AND_RESTART()
```

### CHECKPOINT @ 600 ORD ✓ (ANKARLÄNK MÅSTE VARA PLACERAD!)

```python
def checkpoint_600():
    if not anchor_placed:
        ABORT("Ankarlänk saknas vid 600 ord!")
    if not context_booster_1_placed:
        WARNING("Context booster #1 bör vara placerad")
```

### Ankarlänk (TVINGANDE REGLER)

**MÅSTE placeras:**

- Mellan ord 400-700
- I naturlig kontext relaterad till variabelgiftet
- Med en av dessa 5 obligatoriska mönster:

```markdown
# REKOMMENDATION
"För [specifikt behov] är [anchor_text](url) ett smart val eftersom [konkret fördel]."

# JÄMFÖRELSE
"Till skillnad från [alternativ] erbjuder [anchor_text](url) [unik fördel]."

# EXPERT
"Professionella inom [bransch] föredrar ofta [anchor_text](url) tack vare [teknisk fördel]."

# PRAKTISK
"I praktiken fungerar [anchor_text](url) bäst när du [specifik situation]."

# VÄRDE
"Vill du investera i [kvalitet/resultat] är [anchor_text](url) värt att överväga."
```

### Trust Links

**Auktoritativa svenska källor:**

| Kategori | Lämpliga källor |
|----------|-----------------|
| Konsument | Konsumentverket, Hallå Konsument |
| Hälsa | 1177, Folkhälsomyndigheten |
| Ekonomi | Finansinspektionen, Skatteverket |
| Miljö | Naturvårdsverket |
| Juridik | Domstol.se |
| Utbildning | Skolverket |
| Arbete | Arbetsförmedlingen |

**Placering:**

- Annan sektion än ankarlänken
- Maximum 2-3 trust links per artikel
- Aldrig i samma stycke som ankarlänk

**⛔ NO COMPETITOR RULE:**
Aldrig länka till en sida som säljer samma produkt/tjänst som Kunden (Target).
Om Kunden är ett Casino → Länka ALDRIG till andra Casinon eller Affiliates.
Länka endast till Spelinspektionen eller Stödlinjen.

---

## Ordval och Ton

### Undvik AI-markörer

**Förbjudna fraser:**

- "Det är viktigt att notera"
- "Sammanfattningsvis kan sägas"
- "Låt oss utforska"
- "I denna artikel kommer vi"
- "Det finns många aspekter"

**Ersättningar:**

| Undvik | Använd istället |
|--------|-----------------|
| "Det är viktigt att" | "Tänk på att" |
| "Sammanfattningsvis" | "Kort sagt" / skippa |
| "Låt oss titta på" | "Här är" / bara börja |
| "Det finns många" | Var specifik: "Fem vanliga" |

### Svenskt naturligt språk

**Preferenser:**

- "Du" istället för "man"
- Korta svenska ord före långa latinska
- Vardagligt före akademiskt

---

## Avslutning med FINAL CHECKPOINT

### CHECKPOINT @ 800 ORD ✓

```python
def checkpoint_800():
    validate = {
        "entity_coverage": percentage >= 70,
        "context_booster_2": True/False,
        "förbereder_avslutning": True/False,
        "inga_upprepningar": True/False
    }
    if not all(validate.values()):
        FIX_BEFORE_CONTINUING()
```

### CHECKPOINT @ 1000+ ORD ✓ (FINAL)

```python
def final_checkpoint():
    requirements = {
        "alla_entities_nämnda": True/False,
        "lix_score": 35 <= score <= 45,
        "context_boosters": count >= 2,
        "ankarlänk_placerad": True,
        "variabelgifte_tydligt": True,
        "ai_markörer": count == 0
    }

    if not all(requirements.values()):
        REJECT_AND_REWRITE()

    quality_score = calculate_score()
    if quality_score < 80:
        REJECT("Kvalitetspoäng under 80!")
```

**Avslutning (50-100 ord):**

**TVINGANDE KRAV:**

- INGEN ny information
- INGEN länk (varken target eller andra)
- MÅSTE koppla tillbaka till variabelgiftet

**OBLIGATORISKA avslutnings-varianter (välj 1):**

```
SAMMANFATTNING: "Kort sagt handlar [ämne] om [kärna]. Med [nyckelinsikt] kan du [resultat]."

UPPMUNTRAN: "Nu har du verktygen för att [handling]. Nästa steg är att [första åtgärd]."

FRAMTID: "Utvecklingen inom [område] går snabbt framåt. [Trend/möjlighet] kommer förändra hur vi [handling]."
```
