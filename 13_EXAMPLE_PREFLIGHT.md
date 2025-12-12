# Example: Complete Preflight

Ett komplett exempel på preflight-analys.

---

## INPUT

```
publisher_domain: hemmets.se
target_url: https://verktygsbutiken.se/borrmaskiner/bosch-gsb-18v
anchor_text: professionell slagborr
```

---

## STEG 1: Publisher Analysis

### Domain: hemmets.se

**Identifierad kategori:** Hem & Inredning

**Nyckelord i domän:**

- "hemmets" → hem, bostad, inredning

**Ton-bedömning:**

- Varm, inspirerande
- Du-tilltal
- Personlig stil

**Typisk artikellängd:** 1000-1500 ord

**Vanliga ämnen:**

- Inredning
- Renovering
- Trädgård
- Hemförbättring

---

## STEG 2: Target Analysis

### URL: verktygsbutiken.se/borrmaskiner/bosch-gsb-18v

**URL-parsing:**

```
Domain: verktygsbutiken.se → verktyg, e-handel
Path 1: borrmaskiner → produktkategori
Path 2: bosch-gsb-18v → produktnamn, varumärke
```

**Extraherade entiteter:**

- borrmaskin, slagborr
- Bosch (varumärke)
- 18V (specifikation)
- verktyg
- hemförbättring

**Primary keyword:** slagborr

**Secondary keywords:**

- borrmaskin
- Bosch
- elverktyg

**Sökintent:** Commercial/Transactional

---

## STEG 3: Semantic Intersect

### Publisher Topics

```
[hem, inredning, renovering, trädgård, design, 
förvaring, belysning, hushåll, gör-det-själv]
```

### Target Topics

```
[verktyg, borrmaskin, slagborr, hemförbättring, 
konstruktion, Bosch, elverktyg, gör-det-själv]
```

### Matching Topics

```
✓ hemförbättring/renovering
✓ gör-det-själv
✓ hem + verktyg = hemmafix
```

### Intersect Score: STRONG (3 matches)

### Primary Bridge: "hemförbättring"

### Bridge Formulation

```
"För dig som renoverar hemmet är rätt verktyg 
avgörande. En [professionell slagborr] gör stor 
skillnad för både effektivitet och resultat."
```

---

## STEG 4: Risk Assessment

| Faktor | Bedömning |
|--------|-----------|
| Relevans | ✓ Stark koppling hem → verktyg |
| Konkurrens | ✓ Ingen direkt konflikt |
| Länkplacering | ✓ Naturlig i renoveringskontext |
| Ton-match | ✓ Kan skrivas inspirerande |

**Risknivå: LÅG**

---

## PREFLIGHT OUTPUT

```json
{
  "preflight_complete": true,
  
  "publisher": {
    "domain": "hemmets.se",
    "category": "Hem & Inredning",
    "tone": "varm, inspirerande",
    "typical_length": 1200,
    "topics": ["hem", "renovering", "inredning", "trädgård"]
  },
  
  "target": {
    "url": "https://verktygsbutiken.se/borrmaskiner/bosch-gsb-18v",
    "product": "Bosch GSB 18V Slagborr",
    "primary_keyword": "slagborr",
    "secondary_keywords": ["borrmaskin", "Bosch", "verktyg"],
    "intent": "commercial"
  },
  
  "anchor": {
    "text": "professionell slagborr",
    "type": "partial_match",
    "keyword_alignment": "strong"
  },
  
  "semantic_intersect": {
    "score": "STRONG",
    "matching_topics": ["hemförbättring", "gör-det-själv", "renovering"],
    "primary_bridge": "hemförbättring",
    "secondary_bridges": ["gör-det-själv", "hemmafix"]
  },
  
  "risk_assessment": {
    "level": "LOW",
    "flags": [],
    "confidence": 0.92
  },
  
  "recommendations": {
    "article_type": "GUIDE",
    "suggested_length": 1200,
    "suggested_angle": "Verktygsguide för hemmarenoveraren",
    "required_entities": [
      "borrmaskin", "slagborr", "renovering", 
      "hemförbättring", "verktyg", "kvalitet"
    ],
    "anchor_placement": "section_2",
    "trust_link_suggestions": [
      "Boverket - bygglov",
      "Konsumentverket - reklamation"
    ]
  }
}
```

---

## NÄSTA STEG

Med denna preflight kan vi nu skapa Writer Facit
(se 14_EXAMPLE_FACIT.md) och sedan generera
artikeln (se 15_EXAMPLE_ARTICLE.md).
