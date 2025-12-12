# API Action Instructions

Hur GPT:n kan anropa BACOWR-systemets API (om Actions är konfigurerade).

---

## När använda API

**Standalone mode (standard):**

- GPT:n kör hela processen internt
- Använder knowledge-filerna
- Ingen extern kommunikation

**API mode (om konfigurerad):**

- GPT:n kan skapa jobb i huvudsystemet
- Synkar med BACOWR-databasen
- Artiklar lagras permanent

---

## Tillgängliga Actions

### 1. createJob

**Användning:** Skapa ett nytt jobb i BACOWR

**Input:**

```json
{
  "publisher_domain": "hemmets.se",
  "target_url": "https://verktyg.se/borr",
  "anchor_text": "professionell borrmaskin"
}
```

**Output:**

```json
{
  "id": "job_abc123",
  "stage": "INTAKE",
  "status": "pending"
}
```

**När anropa:** När användaren vill spara jobbet i huvudsystemet.

---

### 2. runPreflight

**Användning:** Kör preflight-analys via huvudsystemet

**Input:** job_id

**Output:** Komplett preflight med facit

**När anropa:** Om användaren vill använda systemets fulla analyskapacitet (SERP-data, KB-lookup, etc.)

---

### 3. generateArticle

**Användning:** Generera artikel via systemets Claude-integration

**Input:** job_id

**Output:** Genererad artikel

**När anropa:** Om användaren vill att huvudsystemet genererar istället för GPT:n.

---

### 4. validateArticle

**Användning:** Validera artikel via systemet

**Input:** job_id

**Output:** Valideringsresultat

**När anropa:** För att bekräfta kvalitet innan leverans.

---

## Instruktioner för GPT

### Om Actions är tillgängliga

```
Jag kan ansluta till BACOWR-systemet för att:
- Spara jobbet i databasen
- Köra mer avancerad preflight-analys
- Synka med er historiska data

Vill du att jag använder API:et, eller ska jag 
köra analysen standalone?
```

### Om Actions INTE är tillgängliga

```
Jag kör nu i standalone-läge och analyserar 
med hjälp av mina interna processer. Resultatet 
blir lika kvalitativt, men sparas inte i ert 
huvudsystem.
```

---

## Felsökning

### API returnerar fel

| Fel | Åtgärd |
|-----|--------|
| 401 Unauthorized | API-nyckel saknas eller felaktig |
| 404 Not Found | Job ID existerar inte |
| 500 Server Error | Försök igen eller kör standalone |

### Fallback till standalone

Om API-anrop misslyckas:

```
API-anropet misslyckades. Jag kör processen 
standalone istället och ger dig samma resultat.
```

---

## Säkerhet

- Ingen känslig data skickas utan användarens godkännande
- API-nycklar hanteras av Actions-konfigurationen
- Inga personuppgifter lagras av GPT:n
