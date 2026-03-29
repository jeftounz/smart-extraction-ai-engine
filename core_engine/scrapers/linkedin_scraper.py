from .base_scraper import BaseScraper
from selenium_stealth import stealth
import time

class LinkedInScraper(BaseScraper):
    def __init__(self, keywords, location):
        super().__init__(headless=False)
        self.base_url = f"https://www.linkedin.com/jobs/search?keywords={keywords}&location={location}"

    def run(self):
        self.start_driver()
        
        stealth(self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        try:
            print(f"🚀 Navegando a: {self.base_url}")
            self.driver.get(self.base_url)
            time.sleep(5) 

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(3)

            job_cards = self.driver.find_elements("css selector", ".base-card")
            print(f"✅ Se encontraron {len(job_cards)} vacantes potenciales.")

            extracted_data = []
            for card in job_cards[:5]: 
                title = card.find_element("css selector", ".base-search-card__title").get_attribute("textContent").strip()
                company = card.find_element("css selector", ".base-search-card__subtitle").get_attribute("textContent").strip()
                link = card.find_element("css selector", ".base-card__full-link").get_attribute("href")
                
                extracted_data.append({
                    "title": title,
                    "company": company,
                    "link": link
                })

            return extracted_data

        except Exception as e:
            print(f"❌ Error en la extracción: {e}")
        finally:
            self.close_driver()

if __name__ == "__main__":
    scraper = LinkedInScraper("Flutter Developer", "Spain")
    data = scraper.run()
    print("\n--- DATOS EXTRAÍDOS ---")
    print(data)