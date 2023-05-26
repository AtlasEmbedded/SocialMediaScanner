import requests
from bs4 import BeautifulSoup

def search_username(username):
    platforms = {
        'GitHub': f"https://github.com/{username}",
        'Twitter': f"https://twitter.com/{username}",
        'Instagram': f"https://www.instagram.com/{username}",
        'LinkedIn': f"https://www.linkedin.com/in/{username}",
        'Facebook': f"https://www.facebook.com/{username}",
        'Youtube': f"https://www.youtube.com/{username}",
        
    }

    for platform, url in platforms.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        if response.status_code == 200:
            if platform == 'Twitter':
                # Check for Twitter's account suspension message
                if soup.find('div', class_='NoResults-title'):
                    print(f"[{platform}] Username '{username}' not found")
                else:
                    print(f"[{platform}] Username '{username}' found")
            elif platform == 'Instagram':
                # Check for Instagram's account private message
                if soup.find('h2', class_='rkEop'):
                    print(f"[{platform}] Username '{username}' not found")
                else:
                    print(f"[{platform}] Username '{username}' found")
            else:
                # Check for other platforms if username exists in page content
                if username.lower() in soup.get_text().lower():
                    print(f"[{platform}] Username '{username}' found")
                else:
                    print(f"[{platform}] Username '{username}' not found")
        else:
            print(f"[{platform}] Failed to connect to {url}")

# Example usage
username = input("Enter a username to search: ")
search_username(username)