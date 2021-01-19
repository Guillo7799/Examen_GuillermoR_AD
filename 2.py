import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
if __name__ == '__main__':
    db_client = MongoClient('localhost:27017')
    cursos = db_client.Examen_AD_GuillermoR
    scraping = cursos.posts

    response = requests.get("https://www.educaedu.com.ec/cursos/quito--pichincha")
    soup = BeautifulSoup(response.content, "lxml")
    post_courses = soup.find_all("a", class_="course-title-link")
    cursos = []
    for post_title in post_courses:
        cursos.append({
            'link'  :  post_title['href'],
            'title' : post_title['title']
        })
    for post in cursos:
       if db_client.Examen_AD_GuillermoR.scraping.find_one({'link': post['link']}) is None:

            print("Found a new listing at the following url: ", post['link'])
            db_client.Examen_AD_GuillermoR.scraping.insert_one(post)