import requests
import xml.todlist as ET

def get_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    sitemap = ET.fromstring(response.text)
    urls = [url.get('loc').text for url in sitemap.findall('url')]
    return urls
