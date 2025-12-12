# BACOWR n8n Integration Guide

Detta paket implementerar "Enforcement Mode" genom n8n, vilket garanterar att varje artikel följer exakt den logik och research som definierats, utan risk för att LLM:et "glömmer av sig".

## 1. Förberedelser

1. **Starta API-servern**:
    Dubbelklicka på `START_API_SERVER.bat` i rotmappen (BACOWR).
    ⚠️ **OBS:** Första gången kan det ta några minuter då den installerar nödvändiga bibliotek (FastAPI, n8n-stöd etc).
    När det står "Uvicorn running on <http://0.0.0.0:8000>" är det klart.
    **Låt detta fönster vara öppet.**

2. **Installera n8n (om du inte redan har det)**:
    - [Ladda ner n8n Desktop](https://n8n.io/) eller kör via Docker.
    - Se till att n8n har tillgång till `localhost:8000`.

## 2. Importera Workflow

1. Öppna n8n.
2. Gå till "Workflows" -> "Import from File".
3. Välj filen `n8n_workflow.json` som ligger i BACOWR-mappen.
4. Du ser nu hela flödet visuellt: `Webhook -> Preflight -> Writer -> Validator`.

## 3. Konfigurera Writer Node

1. Klicka på noden **"Writer Agent (LLM)"**.
2. Du behöver lägga in din OpenAI API Key i n8n ("Credentials").
3. Modellen är inställd på `gpt-4-turbo`. Du kan ändra detta till `gpt-4o` om du vill.

## 4. Kör ett jobb

Du har två sätt att starta ett jobb:

**Alt A: Via Webhook (Postman/Curl)**
Skicka en POST request till webhook-URL:en (som du ser i n8n "Webhook Trigger") med body:

```json
{
  "publisher_domain": "hemmets.se",
  "target_url": "https://belysning.se/led-list",
  "anchor_text": "led-list"
}
```

**Alt B: Via "Test Workflow" i n8n**

1. Ändra "Webhook Trigger" till "Manual Trigger" för testning.
2. Eller klicka bara "Execute Workflow" och mata in testdata manuellt i första noden.

## Hur det fungerar (Enforcement)

1. **Preflight (API)**: Python-koden analyserar siterna och skapar ett "Variabelgifte".
2. **Prompt Construction**: n8n bygger ihop en strikt prompt: "Du MÅSTE använda vinkeln X".
3. **Writer**: Skriver texten.
4. **Validator (API)**: Python-koden kollar LIX, länkar och entities.
5. **Quality Gate**: Om Validatorn ger tummen ner, skickas texten tillbaka för revision automatiskt.
