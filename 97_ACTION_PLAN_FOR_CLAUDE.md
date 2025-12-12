# FINAL SYSTEM SPECIFICATION: "THE V2 STANDARD"

**Bakgrund:**
Efter att ha stress-testat systemet mot tre scenarion (Starkt, Rimligt, Svagt variabelgifte) står det klart att systemet är strategiskt "rätt" men taktiskt för "snällt".
Vi såg i "Tech/Elskling"-caset att för att nå *Golden Standard* på första försöket, måste reglerna som applicerades i efterhand (v2) gälla från start.

Denna specifikation definierar exakt vilka ändringar som krävs i filer `04`, `05`, `10` och `11` för att systemet ska leverera v2-kvalitet på första försöket, varje gång.

---

## 1. WRITER ENGINE (`04_WRITER_ENGINE.md`) - TIGHTENING THE SCREWS

**Analys:** Writern är för fri. Den tillåts skapa "textväggar" och "hängande länkar".
**Krav:** Inför "Hard Constraints" baserat på lärdomarna.

### 1.1 Struktur-tvång (Anti-Wall-of-Text)

* **Regel:** Varje H2-sektion som överstiger 250 ord *MÅSTE* innehålla en uppbrytande faktor:
  * Antingen minst två **H3-underrubriker**.
  * Eller en **punktlista** (3-5 punkter).
* **Mål:** Aldrig mer än 3 stycken text utan visuell paus.

### 1.2 Trust Link Integration (Anti-Dangling-Links)

* **Regel:** Trust Links får *aldrig* placeras som "läs mer" i slutet av ett stycke.
* **Formatet "Evidence-Based Claim":**
  * ❌ FEL: "Elpriser varierar. Läs mer hos Energimarknadsinspektionen."
  * ✅ RÄTT: "Enligt **Energimarknadsinspektionens senaste rapport** [LÄNK] har de rörliga priserna ökat, vilket gör att konsumenter bör vara vaksamma."
* **Krav:** Minst 2 Trust Links per artikel. Minst 1 måste vara "Integrated Evidence" (enligt ovan).

### 1.3 Sentence Variance (Anti-AI-Drone)

* **Regel:** "Variations-kravet".
  * Förbjudet att börja två meningar i rad med samma ord.
  * Förbjudet att börja mer än 2 stycken i rad med "Det..." eller "När...".
  * Blanda *Power Statements* (korta, <10 ord) med förklarande meningar.

---

## 2. VALIDATOR ENGINE (`05_VALIDATOR.md`) - SHARPENING THE TEETH

**Analys:** Validatorn är för konceptuell ("kolla täckning"). Den måste bli binär ("Pass/Fail").
**Krav:** Definiera exakta gränsvärden som leder till REJECT.

### 2.1 Mätbara Trösklar

* **Structure Fail:** Om artikeln (< 1300 ord) har färre än 5 st H2 → **REJECT**.
* **Formatting Fail:** Om en H2-sektion är >300 ord utan H3/lista → **REJECT**.
* **Link Fail:** Om trust links ligger i separata "Källor"-sektioner istället för i texten → **REJECT**.

### 2.2 Seriousness Check

* Om `serp_status` var OK i Preflight, måste Validatorn kolla att Writern *faktiskt* använt "Winning Factors" från analysen.
  * Saknas "Content Gap"-fyllnaden? → **REJECT**.

---

## 3. TEMPLATES & PATTERNS (`10` & `11`) - THE BLUEPRINTS

**Analys:** Mallarna måste stödja de nya hårda reglerna visuellt.

### 3.1 Uppdatera `10_ARTICLE_TEMPLATES.md`

* Skriv om *alla* mallar (Guide, Listicle, etc) så att de explicit visar H3-strukturen.
* Exempel:

    ```markdown
    ## H2: [Huvudämne]
    [Intro till sektionen]
    ### H3: [Underaspekt 1]
    [Text med Trust Link]
    ### H3: [Underaspekt 2]
    [Text]
    ```

### 3.2 Uppdatera `11_SECTION_PATTERNS.md`

* Lägg till mönstret **"The Evidence Weave"**:
  * Instruktion för hur man flätar in en källa mitt i en mening för att ge tyngd åt ett påstående.

---

## 4. INSTRUKTION TILL CLAUDE (IMPLEMENTATION)

Du (Claude) ska nu generera de kompletta, uppdaterade filinnehållen för:

1. `04_WRITER_ENGINE.md`
2. `05_VALIDATOR.md`
3. `10_ARTICLE_TEMPLATES.md`
4. `11_SECTION_PATTERNS.md`

**Utförande:**
Gå igenom punkt 1-3 ovan. Skriv om filerna så att dessa regler inte är "förslag" utan "lag". Använd versaler och "MUST"-språk i prompterna där det behövs. Vi bygger v2-standarden nu.
