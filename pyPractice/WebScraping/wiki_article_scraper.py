import requests
from bs4 import BeautifulSoup

def get_wikipedia_article(topic):
	url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"

	headers = {
		'User-Agent': 'Chrome/91.0.4472.124'
	}

	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		return response.text
	else:
		return f"Error: Unable to retrieve article. Status code: {response.status_code}"
	
def get_article_title(soup):
	return soup.find('h1', {'id': 'firstHeading'}).get_text()

def get_article_summary(soup):
	paragraphs = soup.find_all('p')
	for paragraph in paragraphs:
		if paragraph.text.strip():
			return paragraph.text.strip()
	return "No summary available."

def get_headings(soup):
	headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
	return headings

def get_related_links(soup):
	links = []
	for link in soup.find_all('a', href=True):
		if link['href'].startswith('/wiki/') and not link['href'].startswith('/wiki/Special:'):
			links.append(f"https://en.wikipedia.org{link['href']}")
	return list(set(links))  

def main():
	topic = input("Enter a Wikipedia topic: ")
	article_html = get_wikipedia_article(topic)
	if article_html.startswith("Error"):
		print(article_html)
		return

	soup = BeautifulSoup(article_html, 'html.parser')
	title = get_article_title(soup)
	summary = get_article_summary(soup)
	headings = get_headings(soup)
	related_links = get_related_links(soup)

	print(f"\nTitle: {title}\n")
	print(f"Summary: {summary}\n")
	print("Headings:")
	for heading in headings:
		print(f"- {heading}")
	print("\nRelated Links:")
	for link in related_links[:10]:  
		print(f"- {link}")

if __name__ == "__main__":	
	main()