# BACOWR Workflow

Detta dokument beskriver det exakta arbetsflödet för att generera en SEO-artikel.

---

## Steg 1: PREFLIGHT ANALYSIS

### 1.1 Publisher Analysis

Analysera publisher-domänen för att förstå:

**Nisch-identifiering:**

- Titta på domännamnet för ledtrådar (hemmets.se → hem/inredning)
- Identifiera typisk artikelkategori
- Uppskatta målgrupp

**Ton & Stil:**

| Typ | Ton | Längd |
|-----|-----|-------|
| Nyheter | Formell, faktabaserad | 500-800 ord |
| Livsstil | Vänlig, personlig | 1000-1500 ord |
| B2B | Professionell, saklig | 800-1200 ord |
| E-handel | Säljande, inspirerande | 600-1000 ord |

### 1.2 Target Analysis

Analysera target-URL:en:

**URL-parsing:**

```
https://exempel.se/kategori/produkt-namn
                    ↓
Extrahera: kategori = "produkter", ämne = "produkt-namn"
```

**Identifiera:**

- Primära keywords (från URL och anchor)
- Relaterade entiteter
- **Metadata Analysis:** Vad säger Title/Meta Description om löftet?
- Trolig sökintent (informational, commercial, navigational)

### 1.3 Semantic Intersect

Hitta överlappningen mellan publisher och target:

```
Publisher Topics ∩ Target Topics = Semantic Intersect
     ↓                    ↓                ↓
   [hem]              [verktyg]      [hemförbättring]
 [inredning]         [gör-det-själv]   [renovering]
```

**Topic Bridges:**
Dessa är "bryggor" som kopplar publisher till target naturligt:

| Publisher | Bridge | Target |
|-----------|--------|--------|
| hemmets.se | "hemförbättring" | verktygsbutik |
| recept.se | "köksredskap" | knivslipen |
| träning.se | "kosttillskott" | vitaminbutik |

### 1.4 Competitive Context

Frågor att besvara:

- Vad skriver konkurrenter om detta ämne?
- Vilka frågor ställer användare? (PAA)
- Finns content gap att fylla?

---

## Steg 2: WRITER FACIT

### 2.1 Välj Artikeltyp

| Typ | När | Struktur |
|-----|-----|----------|
| **GUIDE** | Informativt ämne | Intro → Vad → Varför → Hur → Slutsats |
| **HOW_TO** | Praktiskt problem | Intro → Steg 1-5 → Tips → Slutsats |
| **LISTICLE** | Jämförelse/översikt | Intro → Item 1-N → Sammanfattning |
| **DEEP_DIVE** | Komplext ämne | Intro → Bakgrund → Analys → Framtid |

### 2.2 Strukturera Artikeln

```markdown
## Intro (150 ord)
Hook + context + vad artikeln täcker

## Sektion 1: [Huvudämne] (300 ord)
Kärninnehåll relaterat till topic bridge

## Sektion 2: [Fördjupning] (300 ord)  
Mer detaljer, här placeras ofta ANKARLÄNKEN

## Sektion 3: [Praktiska tips] (200 ord)
Handlingsbara råd, trust links här

## Avslutning (100 ord)
Sammanfattning, ingen länk här
```

### 2.3 Planera Länkplacering

**Ankartext-placering:**

- Aldrig i första stycket
- Aldrig i sista stycket
- Bäst i sektion 2 eller 3
- Omgiven av relevant kontext (±2 meningar)

**Trust Links:**

- Minst 1 auktoritativ källa
- Placera i annan sektion än ankarlänk
- Svenska myndigheter, branschorganisationer, forskning
- **ALDRIG** konkurrenter eller affiliates

### 2.4 Required Entities

Lista entiteter som MÅSTE nämnas:

- Från target-URL
- Från anchor text
- Relaterade branschtermer
- Kategori-specifika begrepp

---

## Steg 3: ARTICLE GENERATION

### 3.1 Skriv Intro

**Teknik:** Start med hook, inte bakgrund

```
❌ "I dagens samhälle är det viktigt..."
✅ "Visste du att 73% av svenskar..."
```

### 3.2 Skriv Body

**För varje sektion:**

1. Börja med tydlig H2
2. Första meningen: vad sektionen handlar om
3. Utveckla med fakta, tips, eller steg
4. Avsluta med transition

### 3.3 Placera Ankarlänk

**Optimal kontext:**

```markdown
När du väljer material för ditt projekt är det värt att 
titta på [anchor_text](target_url) som erbjuder hög 
kvalitet till rimligt pris.
```

**INTE:**

```markdown
Klicka här för att läsa mer: [anchor_text](target_url).
```

### 3.4 Lägg till Trust Links

**Format:**

```markdown
Enligt [Konsumentverket](https://konsumentverket.se/...) 
bör du alltid jämföra priser innan köp.
```

---

## Steg 4: VALIDATION

### 4.1 LIX-kontroll

**Beräkning:**

```
LIX = (ord/meningar) + (långa_ord × 100 / ord)
```

| LIX | Nivå | Kommentar |
|-----|------|-----------|
| < 30 | Mycket enkelt | För barnboksaktigt |
| 30-40 | Enkelt | ✓ Idealiskt för SEO |
| 40-50 | Medium | ✓ Acceptabelt |
| > 50 | Svårt | Förenkla meningar |

### 4.2 AI-markör Check

**UNDVIK dessa fraser:**

- "Det är viktigt att notera"
- "I denna artikel kommer vi att"
- "Sammanfattningsvis kan sägas"
- "Låt oss utforska"
- "I dagens digitala värld"

### 4.3 Länk-validering

**Checklista:**

- [ ] Ankartexten förekommer exakt EN gång
- [ ] Ankartexten är länkad till target_url
- [ ] Länken är i informativ kontext
- [ ] Minst 1 trust link finns
- [ ] Länkarna är inte klustrade

### 4.4 Final Check

- [ ] Artikeln matchar publishers ton
- [ ] Längden är lämplig (800-1500 ord)
- [ ] H2-rubriker är beskrivande
- [ ] Ingen lorem ipsum eller placeholder

---

## Quick Reference

```
INPUT: publisher_domain, target_url, anchor_text
↓
PREFLIGHT: Analyze → Intersect → Bridges
↓
FACIT: Type → Structure → Links → Entities
↓
WRITE: Intro → Body → Anchor → Trust Links
↓
VALIDATE: LIX → AI-check → Link-check
↓
OUTPUT: Komplett artikel
```
