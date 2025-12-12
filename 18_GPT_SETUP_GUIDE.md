# GPT Setup Guide

Steg-för-steg guide för att skapa Custom GPT.

---

## 1. Skapa ny GPT

1. Gå till <https://chat.openai.com/gpts/editor>
2. Klicka "Create a GPT"
3. Välj "Configure" (inte "Create")

---

## 2. Grundinställningar

### Name

```
BACOWR SEO Writer
```

### Description

```
Genererar SEO-optimerade artiklar med naturlig länkplacering. 
Tar emot publisher, target URL och ankartext.
```

### Instructions (System Prompt)

**VIKTIGT: Börja med denna rad överst:**
```
⚠️ KRITISKT: Läs 00_ENFORCEMENT_LAYER.md FÖRST! Det dokumentet innehåller ABSOLUTA REGLER som övertrumfar allt annat.
```

Sedan kopiera hela innehållet från `00_MASTER_ORCHESTRATOR.md`

---

## 3. Ladda upp Knowledge-filer

**Ordning för uppladdning:**

1. **`00_ENFORCEMENT_LAYER.md`** ⚠️ KRITISK - MÅSTE VARA FÖRST!
2. `02_WORKFLOW.md`
3. `03_PREFLIGHT_ENGINE.md` (uppdaterad med variabelgifte)
4. `04_WRITER_ENGINE.md` (uppdaterad med checkpoints)
5. `05_VALIDATOR.md` (uppdaterad med poängsystem)
6. `06_PUBLISHER_PROFILES.md`
7. `07_SEO_BEST_PRACTICES.md`
8. `08_ENTITY_DATABASE.md`
9. `09_TRUST_LINKS.md`
10. `10_ARTICLE_TEMPLATES.md`
11. `11_SECTION_PATTERNS.md`
12. `12_INTRO_CTA_PATTERNS.md`
13. `13_EXAMPLE_PREFLIGHT.md`
14. `14_EXAMPLE_FACIT.md`
15. `15_EXAMPLE_ARTICLE.md`
16. `16_API_SCHEMA.json` (om Actions används)
17. `17_ACTION_INSTRUCTIONS.md` (om Actions används)
18. `18_GPT_SETUP_GUIDE.md` (denna fil, för referens)

> **Notera:** `00_MASTER_ORCHESTRATOR.md` ligger i Instructions (inte som fil). `01_SYSTEM_PROMPT.md` är nu uppdaterad med enforcement-referenser.

---

## 4. Conversation Starters

Lägg till dessa förslag:

```
Skapa en artikel för hemmets.se som länkar till verktygsbutiken.se med ankartexten "bästa borrmaskin"
```

```
Jag har publisher: ekonomibloggen.se, target: försäkringsbolaget.se, anchor: "billigaste hemförsäkringen"
```

```
Kör preflight-analys för livsstil.se och https://kosttillskott.se/vitaminer
```

---

## 5. Capabilities

**Aktivera:**

- ✅ Web Browsing (för att verifiera publishers)
- ✅ Code Interpreter (för LIX-beräkning om nödvändigt)

**Avaktivera:**

- ❌ DALL-E (behövs inte)

---

## 6. Actions (Valfritt)

Om du vill integrera med huvudsystemet:

1. Klicka "Create new action"
2. Importera `16_API_SCHEMA.json`
3. Konfigurera autentisering:
   - Authentication: API Key
   - Auth Type: Bearer

---

## 7. Testa GPT:n

### Test 1: Enkel artikel

```
Input: hemmets.se, https://verktyg.se/borr, "professionell borrmaskin"
Förväntat: Komplett artikel ~1000 ord
```

### Test 2: Preflight endast

```
Input: "Kör bara preflight för techbloggen.se och apple.se/iphone"
Förväntat: Preflight-analys utan artikel
```

### Test 3: Annan nisch

```
Input: resor.se, https://hotell.se/paris, "bästa hotellet i Paris"
Förväntat: Artikel med rese-ton
```

---

## 8. Finjustering

### Om artiklar är för korta

- Justera "typical_length" i instruktionerna
- Be om längre format

### Om tonen är fel

- Var mer specifik om publisher i input
- Referera till PUBLISHER_PROFILES

### Om länkplacering är konstlad

- Studera SECTION_PATTERNS för bättre kontext
- Ge feedback till GPT:n

---

## Checklista

```
□ Name och description satt
□ System prompt kopierat från 01_SYSTEM_PROMPT.md
□ Alla 15-18 filer uppladdade som Knowledge
□ Conversation starters konfigurerade
□ Web Browsing aktiverat
□ GPT testad med exempeljobb
□ (Valfritt) Actions konfigurerade
```

---

## Underhåll

**Uppdatera Knowledge-filer när:**

- Nya publishers läggs till
- SEO-praxis förändras
- Nya artikeltyper behövs
- Trust links blir inaktuella

**Backup:**
Behåll gpt_package/ mappen synkad med GPT:ns Knowledge.
