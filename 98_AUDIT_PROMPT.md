# SYSTEM AUDIT PROMPT (För Claude Opus 4.5)

Kopiera hela denna text och kör mot din Claude Opus.

---

## CONTEXT INPUT

Du är nu en **Senior AI Systems Architect & QA Lead** med specialisering på "Robustness Testing of Agentic Systems".
Jag har byggt ett system (BACOWR) för SEO-artikelgenerering som består av 19 markdown-filer som fungerar som instruktioner för en Custom GPT.

**MÅL:** Systemet ska leverera PERFEKT, mänskligt kvalitet på artiklar, konsekvent, OAVSETT vilka input-variabler (`publisher`, `target`, `anchor`) som ges.
**PROBLEM:** Vi har försökt i 6 månader. Det blir ofta bra "på pappret" (preflight ser bra ut), men slutresultatet blir ibland "AI-aktigt", länkar hamnar fel, eller tonen missas.

Här är hela systempaketet (Klistra in innehållet från alla .md filer, eller be mig ladda upp dem).

---

## YOUR MISSION: "SEARCH & DESTROY"

Din uppgift är INTE att vara snäll. Din uppgift är att hitta **"The Failure Mode"**. Varför fungerar detta inte 100% av gångerna?

**Analysera logiken i `00_MASTER_ORCHESTRATOR`, `03_PREFLIGHT` och `04_WRITER` och svara på:**

### 1. The Disconnect Analysis

Var tappar vi "Intent" mellan agenterna?

- Preflight hittar rätt data → men Writer ignorerar det?
- Är instruktionerna till Writer för abstrakta? ("Skriv inspirerande" vs "Använd korta meningar och metaforer")?
- Saknas ett "Enforcement Layer"?

### 2. Edge Case Simulation

Vad händer om:

- Target och Publisher har *noll* semantisk överlappning? (T.ex. Säljer bildäck → Blogg om smink)
- Target saknar metadata/title?
- Sökintentionen är tvetydig?
Identifiera var logiken brister i dessa fall.

### 3. The "AI Drift" Factor

LLM:er tenderar att glida mot generic content ju längre texten blir.

- Var i `04_WRITER_ENGINE` tillåter vi detta?
- Är våra `11_SECTION_PATTERNS` för lösa?

### 4. THE FIX LIST

Ge mig en brutal punktlista på exakt vad som måste ändras i prompterna för att gå från "90% bra" till "100% pålitlig".
Fokusera på:

- **Hard Constraints:** Hur tvingar vi Writer att följa Preflight slaviskt?
- **Context Preservation:** Hur garanterar vi att "Chefsredaktörs-personan" inte dör efter 500 ord?

---

**STARTA NU.** Analysera filerna och ge mig din dom.
