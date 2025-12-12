# Validator

⚠️ **ENFORCEMENT-DRIVEN SCORING**: Minst 80 poäng krävs för godkänt!

---

## 🎯 NYTT KVALITETSPOÄNG-SYSTEM (100 poäng totalt)

```python
def calculate_quality_score(article):
    score = 100  # Börja med full poäng

    # NEGATIVA POÄNG (dras av)
    score -= 10 * count_ai_markers(article)
    score -= 5 * count_long_sentences(article)  # >25 ord
    score -= 5 * count_passive_voice(article)
    score -= 10 if not anchor_naturally_placed
    score -= 10 if entity_coverage < 0.7
    score -= 15 if not variable_marriage_clear
    score -= 10 if no_serp_insights_used
    score -= 5 if lix_score > 50 or lix_score < 30

    # POSITIVA POÄNG (bonus)
    score += 5 if unique_angle_clear
    score += 5 if context_boosters >= 2
    score += 5 if word_count in range(900, 1300)

    # ENFORCEMENT RULE
    if score < 80:
        return "REJECTED - REWRITE REQUIRED"

    return f"APPROVED - Score: {score}/100"
```

---

## 1. LIX-beräkning

### Formel

```
LIX = (antal_ord / antal_meningar) + (långa_ord × 100 / antal_ord)
```

**Där:**

- Mening = slutar med . ! ?
- Långt ord = > 6 tecken

### Målintervall

| LIX | Nivå | Åtgärd |
|-----|------|--------|
| < 25 | Mycket enkelt | ⚠️ Lägg till komplexitet |
| 25-30 | Enkelt | ✓ OK för korta artiklar |
| **30-40** | **Lättläst** | ✅ **IDEALT** |
| **40-50** | **Medium** | ✅ **ACCEPTABELT** |
| 50-55 | Svårt | ⚠️ Förenkla meningar |
| > 55 | Akademiskt | ❌ Skriv om |

### Hur justera LIX

**Om för högt (> 50):**

- Dela långa meningar
- Ersätt långa ord
- Ta bort parenteser
- Korta ner listor

**Om för lågt (< 30):**

- Lägg till specifikitet
- Använd fler facktermer (naturligt)
- Längre meningar ibland

---

## 2. AI-markör Detektion

### Förbjudna fraser (AUTOMATISK REJECTION)

```python
FORBIDDEN_PHRASES = [
    "det är viktigt att notera",     # -10 poäng
    "i denna artikel kommer vi att",  # -10 poäng
    "sammanfattningsvis kan sägas",   # -10 poäng
    "låt oss utforska",               # -10 poäng
    "i dagens digitala värld",        # -10 poäng
    "som vi alla vet",                # -10 poäng
    "det finns många aspekter av",    # -10 poäng
    "i slutändan",                    # -10 poäng
    "det har blivit allt viktigare"   # -10 poäng
]

# ENFORCEMENT: En enda förbjuden fras = -10 poäng!
```

### Orange flaggor (varning)

```
□ "Generellt sett"
□ "I alla händelser"
□ "Det kan sägas att"
□ "Oavsett om"
□ "I kombination med"
□ Samma övergångsord > 3 gånger (dessutom, därför, dock)
```

### Mönster att undvika

**Repetitiv struktur:**

```
❌ "För det första... För det andra... För det tredje..."
✓ Variera med: "Dessutom", "Utöver detta", "Ytterligare en aspekt"
```

**Över-kvalificering:**

```
❌ "Det är viktigt, om inte avgörande, att..."
✓ "Tänk på att..."
```

---

## 3. Länkvalidering

### Ankarlänk Check

**Obligatoriska kontroller:**

| Check | Krav |
|-------|------|
| Förekommer | Exakt 1 gång |
| Länkad | Korrekt markdown [text](url) |
| Position | Ej i intro (första 150 ord) |
| Position | Ej i outro (sista 100 ord) |
| Kontext | Omgiven av relevant text |

**Kontextvalidering:**

```markdown
✅ BRA:
"För hemförbättring kan [anchor_text](url) vara 
ett bra alternativ tack vare sin kvalitet."

❌ DÅLIGT:
"Klicka här: [anchor_text](url)"

❌ DÅLIGT:
"[anchor_text](url) är bra."
```

### Trust Links Check

| Check | Krav |
|-------|------|
| Antal | Minst 1, max 3 |
| Placering | Ej samma stycke som ankarlänk |
| URL | Går till trovärdig källa |
| Relevans | Stödjer artikelns påståenden |

**Trovärdiga domäner:**

- .gov.se, .se (myndigheter)
- Etablerade nyhetskällor
- Branschorganisationer
- .gov.se, .se (myndigheter)
- Etablerade nyhetskällor
- Branschorganisationer
- Forskningsinstitut

### Competitor Link Validation (CRITICAL)

Kontrollera **varje** trust link:

1. Säljer sajten samma produkt som target? → UNDERKÄND
2. Är det en affiliate-sajt (toplists, recensioner)? → UNDERKÄND
3. Konkurrerar den med publishern? → UNDERKÄND

**Regel:** Om tveksam, underkänn. Endast neutrala källor tillåtna.

---

## 4. Strukturvalidering

### Rubriker

| Check | Krav |
|-------|------|
| H1 | Exakt 1 (titeln) |
| H2 | Minst 3 |
| Längd | H2 max 10 ord |
| Keywords | H2 innehåller relevant term |

### Längd per sektion

| Sektion | Min | Max |
|---------|-----|-----|
| Intro | 100 | 250 |
| Body section | 150 | 400 |
| Outro | 50 | 150 |
| Total | 800 | 1800 |

### Stycken

- Max 5 meningar per stycke
- Inga ensamma meningar (undvik 1-meningsstycken)
- Variera längd mellan stycken

---

## 5. Entitetsvalidering

### Required Entities Check

Kontrollera att följande nämns:

| Entitet | Källa |
|---------|-------|
| Primary keyword | anchor_text |
| Secondary keywords | URL slug |
| Category terms | Publisher nisch + target kategori |
| Bridge topic | Semantic intersect |

**Minimum täckning:** 70% av required entities

---

## Validerings-Checklist

### ✅ Före leverans

```markdown
## Obligatoriska
- [ ] LIX mellan 30-50
- [ ] Inga förbjudna AI-fraser
- [ ] Ankarlänk förekommer exakt 1 gång
- [ ] Ankarlänk är korrekt formaterad
- [ ] Ankarlänk ej i intro/outro
- [ ] Minst 1 trust link
- [ ] Trust link till relevant källa
- [ ] Minst 3 H2-rubriker
- [ ] Minst 1 trust link
- [ ] Trust link till relevant källa
- [ ] INGA länkar till konkurrenter/affiliates
- [ ] Minst 3 H2-rubriker
- [ ] Total längd 800-1800 ord

## Rekommenderade
- [ ] Entity coverage > 70%
- [ ] Varierande meningslängd
- [ ] Inga repetitiva övergångsord
- [ ] Naturlig svensk ton
```

---

## ENFORCEMENT VALIDATION OUTPUT

```json
{
  "quality_score": 85,
  "status": "APPROVED/REJECTED",

  "enforcement_checks": {
    "variabelgifte_established": true,
    "checkpoints_passed": [200, 400, 600, 800, 1000],
    "ai_markers_found": 0,
    "forbidden_phrases": [],
    "average_sentence_length": 18
  },

  "detailed_scores": {
    "lix": 38,
    "entity_coverage": 0.85,
    "context_boosters": 2,
    "anchor_placement": "natural",
    "serp_insights_used": true
  },

  "penalties": [
    {"reason": "långt stycke", "points": -5},
    {"reason": "passiv form", "points": -5}
  ],

  "bonuses": [
    {"reason": "unik vinkel", "points": +5},
    {"reason": "optimal längd", "points": +5}
  ],

  "rejection_reasons": [],
  "rewrite_instructions": []
}
```
