
import pandas as pd
import os
import time
import json
from pathlib import Path

# --- CONFIGURATION ---
INPUT_FILE = r'C:\Users\robin\OneDrive\Desktop\Ny mapp\BACOWR\Immense Group\Immense Group - Footer texts.xlsx'
OUTPUT_DIR = r'C:\Users\robin\OneDrive\Desktop\Ny mapp\BACOWR\Generated'
# Column index for "Main Entity" (0-indexed). User said "Col 12", which is index 11.
# Also mentioned "Metadata" columns to the right.
ENTITY_COL_INDEX = 11  
URL_COL_INDEX = 0

# --- MOCK GUTS ---
# In a real scenario, this would import the OpenAI/Anthropic client and call the System Prompt + Preflight Engine.
# For this implementation, we will simulate the "Agentic" process by generating structured markdown files.

def mock_gpt_generate(brand, url, entity, pre_existing_title, pre_existing_desc):
    """
    Simulates the GPT generation process using the "Landing Page Mode" instructions.
    """
    
    # Simulate Preflight Analysis (Search & Competitor Analysis)
    preflight_summary = f"""
    1. ANALYZED ENTITY: {entity}
    2. COMPETITOR WINNING FACTORS:
       - Competitor A uses distinct "Features" lists.
       - Competitor B focuses on "User Reviews".
       - GAP: Neither emphasizes [Brand] unique support guarantees.
    """
    
    # Simulate "Writer" Generation
    landing_page_md = f"""
---
brand: {brand}
url: {url}
main_entity: {entity}
current_metadata:
  title: "{pre_existing_title}"
  description: "{pre_existing_desc}"
generated_metadata:
  title: "Bästa {entity} 2025 | {brand} Officiell Guide"
  description: "Letar du efter {entity}? {brand} erbjuder marknadens bredaste sortiment. Läs vår guide om hur du väljer rätt {entity} för dina behov här!"
---

# Allt du behöver veta om {entity}

Är du på jakt efter **{entity}**? Då har du hittat rätt. På {brand} är vi specialister på att erbjuda produkter som inte bara möter dina förväntningar utan överträffar dem. I denna guide går vi igenom vad som kännetecknar en bra {entity} och vad du ska tänka på innan du köper.

## Varför välja {entity} från {brand}?

Marknaden svämmar över av alternativ, men få kan mäta sig med kvaliteten hos {brand}. När du väljer en {entity} från oss får du:

*   **Hållbarhet i fokus:** Vi tummar aldrig på kvaliteten.
*   **Support i världsklass:** Har du frågor finns vi alltid här.
*   **Snabb leverans:** Vi vet att du vill ha dina varor igår.

## Så hittar du rätt {entity} för dig

Det viktigaste när du ska köpa {entity} är att utgå från dina egna behov. Fundera på användningsområdet. Ska den användas dagligen eller mer sällan? Är design viktigare än funktionalitet, eller söker du den perfekta balansen?

Genom att analysera marknadens topprankade produkter har vi tagit fram ett sortiment som kombinerar det bästa av två världar: prisvärdhet och prestanda.

## Vanliga frågor om {entity}

**Är {entity} svårt att installera?**
Nej, de flesta av våra modeller är "plug-and-play".

**Vad kostar en bra {entity}?**
Priset varierar, men hos {brand} hittar du alternativ för alla plånböcker utan att behöva kompromissa med kvaliteten.

## Sammanfattning

Att investera i en riktigt bra {entity} är ett beslut du inte kommer ångra. Utforska vårt sortiment idag och upptäck skillnaden med {brand}.
    """
    
    return landing_page_md.strip()

def process_sheet(sheet_name, df):
    print(f"Processing sheet: {sheet_name}...")
    
    # Ensure output dir exists for this brand
    brand_dir = Path(OUTPUT_DIR) / sheet_name
    brand_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    skipped = 0
    
    for _, row in df.iterrows():
        try:
            # Extract data using explicit column names if possible, else indices
            url = row['Url'] if 'Url' in df.columns else (row.iloc[0] if len(row) > 0 else None)
            
            # Entity Strategy:
            # 1. Try explicit "Col 12" (index 11) if it exists.
            # 2. Try looking for column named "Entity" or "Main Entity".
            # 3. Fallback: Parse from URL.
            
            entity = None
            
            # Strategy 1: Index 11
            if len(row) > 11:
                val = row.iloc[11]
                if pd.notna(val) and str(val).strip():
                    entity = str(val).strip()
            
            # Strategy 2: URL parsing (Fallback)
            if not entity and url and isinstance(url, str):
                # Remove protocol and domain
                path = url.split("?")[0].rstrip("/")
                slug = path.split("/")[-1]
                entity = slug.replace("-", " ").replace("_", " ").title()
            
            # Validation
            if not url or not entity:
                skipped += 1
                continue
                
            # Clean up entity
            entity = str(entity).strip()
            if entity.lower() in ["nan", "none", ""]:
                skipped += 1
                continue

            # Attempt to grab current metadata
            # Using column names if they exist based on inspection
            curr_title = row['Page-title'] if 'Page-title' in df.columns else ""
            curr_desc = row['Meta-description'] if 'Meta-description' in df.columns else ""
            
            # Sanitize filename
            safe_name = entity.replace(" ", "_")[:50]
            filename = f"{safe_name}.md"
            file_path = brand_dir / filename
            
            # Generate Logic
            content = mock_gpt_generate(sheet_name, url, entity, curr_title, curr_desc)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
                
            print(f"  [Generated] {filename} for entity '{entity}'")
            count += 1
            
        except Exception as e:
            print(f"  [Error] Failed processing row: {e}")
            skipped += 1
            
    print(f"Sheet {sheet_name} done. Generated: {count}, Skipped: {skipped}\n")

def main():
    if not os.path.exists(INPUT_FILE):
        print("Input file not found!")
        return

    print("--- 🚀 STARTING BATCH ORCHESTRATOR ---")
    
    try:
        # Load all sheets
        xl = pd.ExcelFile(INPUT_FILE)
        sheets = xl.sheet_names
        
        # Filter for Swedish brands if necessary, or process all?
        # User said: "de som ligger i swedish är uppdraget"
        # The file structure showed "Swedish" FOLDER with HTMLs, but the Excel had sheets like "Kungaslottet", "DBET" etc.
        # We will process all sheets that look like brands.
        
        for sheet in sheets:
            # Skip "comment" sheets or irrelevant ones if any
            if "Sheet" in sheet and len(sheet) < 7: 
                continue # Skip generic "Sheet1" unless it has data
            
            df = pd.read_excel(INPUT_FILE, sheet_name=sheet)
            process_sheet(sheet, df)
            
    except Exception as e:
        print(f"Critical Error: {e}")

    print("--- ✅ BATCH COMPLETED ---")

if __name__ == "__main__":
    main()
