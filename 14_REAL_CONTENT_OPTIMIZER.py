
import requests
import os
from bs4 import BeautifulSoup
import re
import argparse
import sys
import time

# --- CONFIGURATION ---
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

class RealContentOptimizer:
    def __init__(self):
        print("🔧 Initializing Real Content Optimizer...")

    def search_competitor(self, keyword):
        """
        Finds the #1 organic ranking URL for the keyword.
        Uses DuckDuckGo HTML to avoid API constraints.
        """
        print(f"🔍 Searching for top competitor for: '{keyword}'...")
        try:
            url = f"https://html.duckduckgo.com/html/?q={keyword}"
            resp = requests.get(url, headers=HEADERS, timeout=10)
            
            # Extract first non-ad result
            # DDG HTML result structure: <a class="result__a" href="...">
            soup = BeautifulSoup(resp.text, 'html.parser')
            results = soup.find_all('a', class_='result__a')
            
            for res in results:
                link = res['href']
                # Filter out ads or irrelevant links if possible
                if "http" in link and "duckduckgo" not in link:
                    print(f"   🏆 Top Competitor Found: {link}")
                    return link
            
            print("   ⚠️ No competitor found in search results.")
            return None
        except Exception as e:
            print(f"   ❌ Search failed: {e}")
            return None

    def scrape_page(self, url, is_client=True):
        """
        Scrapes Title, H1, Meta Desc, and Main Content from a URL.
        """
        label = "Client" if is_client else "Competitor"
        print(f"📄 Scraping {label}: {url}...")
        
        try:
            resp = requests.get(url, headers=HEADERS, timeout=15)
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            # Extract Metadata
            title = soup.title.string.strip() if soup.title else "No Title"
            
            # Try to find meta description
            meta_desc = ""
            meta_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
            if meta_tag:
                meta_desc = meta_tag.get('content', '').strip()
                
            # Extract H1
            h1 = soup.find('h1').get_text().strip() if soup.find('h1') else "No H1"
            
            # Extract Main Content (Generic heuristic)
            # Try to find the biggest container of text
            content_text = ""
            # Common article containers
            article = soup.find('article') or soup.find('main') or soup.find('div', class_='content') or soup.find('div', class_='entry-content') or soup.body
            
            if article:
                # Remove scripts and styles
                for script in article(["script", "style", "nav", "footer", "header"]):
                    script.decompose()
                content_text = article.get_text(separator="\n").strip()
                # Truncate for sanity in logs/prompts
                content_text_preview = content_text[:200].replace('\n', ' ') + "..."
            else:
                content_text_preview = "Could not parse main content."

            data = {
                "url": url,
                "title": title,
                "description": meta_desc,
                "h1": h1,
                "content_preview": content_text_preview,
                "full_text_length": len(content_text)
            }
            
            print(f"   ✅ Fetched: '{title}' (Len: {len(content_text)} chars)")
            return data

        except Exception as e:
            print(f"   ❌ Scraping failed: {e}")
            return None

    def generate_superior_version(self, client_data, competitor_data, keyword):
        """
        Calls OpenAI to generate the superior version based on real data analysis.
        """
        print("\n🧠 ORCHESTRATING SUPERIOR CONTENT (VIA LLM)...")
        
        # Check for OpenAI Key
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("   ⚠️ CRITICAL: OPENAI_API_KEY not found in environment.")
            print("   Please set it (e.g., `set/export OPENAI_API_KEY=sk-...`) to generate real text.")
            print("   Returning placeholder for now.")
            return self._get_placeholder_output(client_data, competitor_data, keyword)

        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
        except ImportError:
            print("   ⚠️ CRITICAL: 'openai' library not installed.")
            print("   Please run `pip install openai`.")
            return self._get_placeholder_output(client_data, competitor_data, keyword)

        # Construct the "Superior Version" Prompt
        # This mirrors the user's "Real Optimizer" mindset: 
        # "Look at competitor X, look at us Y, make Y > X using X's structure but Y's voice."
        
        system_prompt = """
        You are an elite SEO Copywriter & Content Optimizer. 
        Your goal is to create a 'Superior Version' of a landing page.
        
        PROCESS:
        1. Analyze the Competitor's "Winning Factors" (Structure, topics, metadata).
        2. Analyze the Client's "Brand Voice" (from their current text).
        3. Generate a NEW page that objectively outperforms the competitor by covering their topics BETTER, 
           while maintaining the Client's brand identity.
        
        OUTPUT FORMAT:
        Return ONLY valid Markdown.
        Include Frontmatter with 'generated_metadata'.
        """

        user_prompt = f"""
        TARGET KEYWORD: {keyword}
        
        ================
        DO REAL RESEARCH
        ================
        
        COMPETITOR (The #1 Ranking Page):
        URL: {competitor_data['url']}
        TITLE: {competitor_data['title']}
        H1: {competitor_data['h1']}
        CONTENT SUMMARY:
        {competitor_data['content_preview']} (and full structure implied)
        
        CLIENT (Our Page - Needs Optimization):
        URL: {client_data['url']}
        TITLE: {client_data['title']}
        H1: {client_data['h1']}
        CURRENT CONTENT:
        {client_data['content_preview']}
        
        ================
        YOUR TASK
        ================
        Create the "Superior Version" of the Client's page.
        
        1. METADATA: Write a Title/Description that beats the Competitor's CTR.
        2. H1: Optimize the H1 for the keyword.
        3. CONTENT: Write the FULL body text (300-600 words). 
           - Use the Competitor's successful topics/structure as a baseline.
           - Improve upon them (more specific, better flow).
           - Use the Client's voice.
           - NO placeholders. Write the ACTUAL text.
        
        """

        print(f"   🚀 Sending prompt to GPT-4o-mini (or available model)...")
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini", # Cost effective, high quality
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )
            
            content = response.choices[0].message.content
            print("   ✅ Generation Complete!")
            return content

        except Exception as e:
            print(f"   ❌ LLM Call Failed: {e}")
            return self._get_placeholder_output(client_data, competitor_data, keyword)

    def _get_placeholder_output(self, client_data, competitor_data, keyword):
        """Fallback if no API key is present."""
        return f"""---
# SIMULATION (REAL LLM CALL FAILED - SEE LOGS)
target_keyword: {keyword}
client_url: {client_data['url']}
competitor_url: {competitor_data['url']}
---

# {client_data['h1']} (Placeholder)

*Please set OPENAI_API_KEY to generate the real superior text.*
"""


def main():
    parser = argparse.ArgumentParser(description="Real Content Optimizer")
    parser.add_argument("client_url", help="URL of the client page to optimize")
    parser.add_argument("keyword", help="Target keyword (Main Entity) for competitor search")
    
    args = parser.parse_args()
    
    optimizer = RealContentOptimizer()
    
    # 1. Scrape Client
    client_data = optimizer.scrape_page(args.client_url, is_client=True)
    if not client_data:
        return

    # 2. Find & Scrape Competitor
    comp_url = optimizer.search_competitor(args.keyword)
    if comp_url:
        competitor_data = optimizer.scrape_page(comp_url, is_client=False)
    else:
        print("   ⚠️ Skipping competitor analysis (not found). using placeholder.")
        competitor_data = {"url": "N/A", "title": "N/A", "h1": "N/A", "description": "N/A"}

    # 3. Optimize
    if competitor_data:
        result = optimizer.generate_superior_version(client_data, competitor_data, args.keyword)
        
        # Save output
        filename = f"OPTIMIZED_{args.keyword.replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"\n✅ Optimization Complete. Saved to {filename}")

if __name__ == "__main__":
    main()
