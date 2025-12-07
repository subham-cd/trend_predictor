import requests
import xml.etree.ElementTree as ET

def get_trending_topics(category="General"):
    print(f"Connecting to Google News ({category})...")
    
    # Base URL settings
    base_params = "ceid=IN:en&hl=en-IN&gl=IN"
    
    # Category Map: Kis interest ke liye kaunsa URL use karein
    urls = {
        "General": f"https://news.google.com/rss?{base_params}",
        "Tech": f"https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?{base_params}",
        "Business": f"https://news.google.com/rss/headlines/section/topic/BUSINESS?{base_params}",
        "Sports": f"https://news.google.com/rss/headlines/section/topic/SPORTS?{base_params}",
        "Entertainment": f"https://news.google.com/rss/headlines/section/topic/ENTERTAINMENT?{base_params}",
        "Science": f"https://news.google.com/rss/headlines/section/topic/SCIENCE?{base_params}",
        "Health": f"https://news.google.com/rss/headlines/section/topic/HEALTH?{base_params}"
    }
    
    # Sahi URL select karo
    url = urls.get(category, urls["General"])
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            trends = []
            for item in root.findall('.//item'):
                title = item.find('title').text
                clean_title = title.split(' - ')[0]
                trends.append(clean_title)
            return trends[:5]
        else:
            return ["Error fetching news", "Check Internet"]
    except Exception as e:
        print(f"Error: {e}")
        return ["Error fetching news", "Check Internet"]