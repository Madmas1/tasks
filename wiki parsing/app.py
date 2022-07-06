import requests
import lxml
from bs4 import BeautifulSoup


url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
req = requests.get(url).text

names = []


# Цикл парсинга
while True:
    soup = BeautifulSoup(req, "lxml")
    # Тормозим цикл если страница с животными началась с английской буквы
    if soup.find("div", class_="mw-category mw-category-columns").find("div", class_="mw-category-group").find(
            "h3").text == "A":
        break
    # Парсинг и запись имен животных
    data = soup.find(id="mw-content-text").find("div", class_="mw-category-generated").find("div", id="mw-pages"). \
        find("div", class_="mw-content-ltr").find("div", class_="mw-category mw-category-columns").find_all("a")
    for elem in data:
        names.append(elem.text)
    # Поиск линков для перехода на следующую страницу и формирования адреса для последующего реквеста
    links = soup.find('div', id='mw-pages').find_all('a')
    for elem in links:
        if elem.text == "Следующая страница":
            url = "https://ru.wikipedia.org/" + elem.get('href')
            req = requests.get(url).text
    # Для отслеживания какая буква сейчас парсится
    print(soup.find("div", class_="mw-category mw-category-columns").find("div", class_="mw-category-group").find(
        "h3").text)

# Можно было бы посчитать количество более оптимальными способами, но я посчитал что так будет нагляднее.
for i in range(ord("А"), ord("Я") + 1):
    count = 0
    for name in names:
        if name[0] == chr(i):
            count += 1
    print(f"{chr(i)}:{count}")


if __name__ == '__main__':
    pass


