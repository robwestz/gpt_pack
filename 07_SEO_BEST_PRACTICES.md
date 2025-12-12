# SEO Best Practices

Riktlinjer för SEO-optimerad artikelskrivning och länkplacering.

---

## Ankartextpolicy

### Typer av ankartexter

| Typ | Beskrivning | Max % | Exempel |
|-----|-------------|-------|---------|
| **Exact match** | Exakt keyword | 10-15% | "bästa borrmaskin" |
| **Partial match** | Innehåller keyword | 25-35% | "tips för att välja borrmaskin" |
| **Brand** | Varumärkesnamn | 20-30% | "Bosch" |
| **Generic** | Generisk text | 15-25% | "klicka här", "läs mer" |
| **URL** | Ren URL | 5-10% | "verktyg.se" |

### Optimal fördelning

```
Exact Match:    ███░░░░░░░  10-15%
Partial Match:  ███████░░░  25-35%
Brand:          █████░░░░░  20-30%
Generic:        ████░░░░░░  15-25%
URL:            ██░░░░░░░░   5-10%
```

### Regler för ankartext

**DO:**

- Variera ankartexten mellan artiklar
- Matcha ankartexten med målsidans huvudkeyword
- Använd naturliga formuleringar

**DON'T:**

- Överanvända exact match
- Placera samma ankartext i flera artiklar
- Använda orelaterade ankartexter

---

## Länkplacering

### Optimal position

```
Intro (150 ord)     ❌ Aldrig länk här
                    
Sektion 1           ⚠️ Trust link OK
                    
Sektion 2           ✅ BÄST för ankarlänk
                    
Sektion 3           ✅ Bra för ankarlänk
                    
Tips/FAQ            ⚠️ Trust link OK
                    
Avslutning          ❌ Aldrig länk här
```

### Länkkontext

**Optimal kontext (2-3 meningar):**

```markdown
Mening 1: Etablera ämnet
[LÄNK inom mening 2]
Mening 3: Följ upp med relaterad information
```

**Exempel:**

```markdown
När du renoverar ditt hem är rätt verktyg avgörande 
för resultatet. Med en [professionell borrmaskin](url) 
kan du spara både tid och frustration. Kvalitetsverktyg 
betalar sig ofta tillbaka över tid.
```

### Länkdensitet

**Rekommenderat:**

- 1 ankarlänk per artikel
- 1-3 trust links per artikel
- Max 1 länk per 200-300 ord

**Fördelning:**

| Artikellängd | Ankarlänk | Trust links |
|--------------|-----------|-------------|
| 600 ord | 1 | 1 |
| 1000 ord | 1 | 2 |
| 1500 ord | 1 | 2-3 |

---

## Rubriker (H-tags)

### H1 (Titel)

**Regler:**

- Exakt 1 per artikel
- Inkludera huvudkeyword
- Max 60 tecken för sökresultat
- Locka till klick utan clickbait

**Format:**

```markdown
# [Keyword]: [Löfte/Vinkel] - [År om relevant]
# Bästa borrmaskinen: Guide för hemmarenoveraren 2024
```

### H2 (Sektionsrubriker)

**Regler:**

- 3-6 per artikel
- Beskrivande, ej generiska
- Inkludera secondary keywords naturligt

**Bra exempel:**

```markdown
## Så väljer du rätt borrmaskin för ditt behov
## Vanliga misstag vid köp av verktyg
## Vad kostar en kvalitetsborrmaskin?
```

**Dåliga exempel:**

```markdown
## Inledning        ❌ För generiskt
## Mer information  ❌ Säger ingenting
## Läs vidare       ❌ Clickbait
```

### H3 (Underrubriker)

**Användning:**

- Vid listor inom sektion
- Vid comparison/jämförelser
- Max 3-4 per H2

---

## Content Length

### Per artikeltyp

| Typ | Min | Optimal | Max |
|-----|-----|---------|-----|
| Nyhetsartikel | 400 | 600 | 800 |
| Guide | 1000 | 1500 | 2500 |
| How-to | 800 | 1200 | 1800 |
| Listicle | 1200 | 1800 | 3000 |
| Produktrecension | 600 | 1000 | 1500 |

### Kvalitet > Längd

**Fler ord ≠ bättre ranking**

Principen:

1. Täck ämnet fullständigt
2. Besvara användarens frågor
3. Ge mervärde jämfört med konkurrenter
4. Stoppa när du upprepat dig

---

## E-E-A-T Signaler

### Experience (Erfarenhet)

- Inkludera personliga erfarenheter/perspektiv
- "När jag själv testade..."
- Praktiska tips från användning

### Expertise (Expertis)

- Visa kunskap om ämnet
- Använd korrekta termer
- Referera till branschstandards

### Authority (Auktoritet)

- Länka till trovärdiga källor (Myndigheter/Org)
- ⛔ **NO COMPETITOR RULE:** Aldrig länka till konkurrenter/affiliates
- Citera experter/myndigheter
- Stöd påståenden med data

### Trust (Trovärdighet)

- Tydlig författarbyline (om relevant)
- Korrekta fakta
- Uppdaterad information

---

## Keyword-användning

### Primärt keyword

**Placering:**

- [ ] I titel (H1)
- [ ] Inom första 100 ord
- [ ] I minst 1 H2
- [ ] I meta description (om relevant)

### Sekundära keywords

**Naturlig spridning:**

- I body text
- I H2/H3 där relevant
- I bildtexter (om bilder finns)

### Keyword-densitet

**Mål:** 1-2% för primärt keyword

**Beräkning:**

```
Keyword appearances × 100 / Total words = Density %
```

**Varning:** Över 3% = keyword stuffing risk
