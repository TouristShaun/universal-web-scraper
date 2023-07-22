import scraper
import sitemap
import image_analysis
import image_to_text
import text_analysis

def main():
    url = input("Enter website URL: ")
    sitemap_urls = sitemap.get_sitemap_urls(url)
    for page_url in sitemap_urls:
        page_content = scraper.scrape_page(page_url)
        screenshot = scraper.take_screenshot(page_url)
        blip2_analysis = image_analysis.analyze_image_with_blip2(screenshot)
        donut_text = image_to_text.convert_image_to_text_with_donut(screenshot)
        text_analysis = text_analysis.analyze_text(donut_text)
        print("Page URL: ", page_url)
        print("BLIP-2 Analysis: ", blip2_analysis)
        print("Donut Text: ", donut_text)
        print("Text Analysis: ", text_analysis)

if __name__ == "__main__":
    main()