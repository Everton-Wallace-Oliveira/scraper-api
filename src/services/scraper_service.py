import requests
from bs4 import BeautifulSoup
from exceptions.custom_exceptions import NotFoundError

class ScraperService:
    def get_google_info(self, query):
        url = f"https://www.google.com/search?q={query}"      
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            telefone_element = soup.find('span', string='Telefone')
            endereco_element = soup.find('span', string='Endereço')
            website_div = soup.find('div', string='Website')
            linkedin_link = soup.find('a', href=lambda href: href and 'linkedin.com' in href)    
            results = {}
            
            if linkedin_link:
                linkedin = linkedin_link['href']
                linkedin = linkedin.replace("url?q=", "")
                linkedin = linkedin.split("&")
                results['Linkedin'] = linkedin[0]
            else:
                results['Linkedin'] = "Not Found"
            
            instagram_link = soup.find('a', href=lambda href: href and 'instagram.com' in href)
            if instagram_link:
                instagram = instagram_link['href']
                instagram = instagram.replace("url?q=", "")
                instagram = instagram.split("&")
                results['Instagram'] = instagram[0]
            else:
                results['Instagram'] = "Not Found"

                
            facebook_link = soup.find('a', href=lambda href: href and 'facebook.com' in href)
            if facebook_link:
                facebook = facebook_link['href']
                facebook = facebook.replace("url?q=", "")
                facebook = facebook.split("&")
                results['Facebook'] = facebook[0]
            else:
                results['Facebook'] = "Not Found"


            twitter_link = soup.find('a', href=lambda href: href and 'twitter.com' in href)
            if twitter_link:
                twitter = twitter_link['href']
                twitter = twitter.replace("url?q=", "")
                twitter = twitter.split("&")
                results['Twitter'] = twitter[0]
            else:
                results['Twitter'] = "Not Found"
                
            if website_div:
                website_link = website_div.find_next('a')
                if website_link:      
                    website = website_link.get('href')
                    website = website.replace("url?q=", "")
                    website = website.split("&")
                    results['Website'] = website[0]
                else:
                    results['Website'] = "Not Found"
            else:
                results['Website'] = "Not Found"

            if endereco_element:
                endereco = endereco_element.find_next_sibling('span').text.strip()
                results['Address'] = endereco

            else:
                results['Address'] = "Not Found"
            if telefone_element:
                telefone = telefone_element.find_next_sibling('span').text.strip()
                results['Telephone'] = telefone
            else:
                 results['Telephone'] = "Not Found"
            return results
        else:
             raise NotFoundError("Error accessing Google page.")
