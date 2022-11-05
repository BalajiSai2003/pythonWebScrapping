from bs4 import BeautifulSoup
with open('pythonWebScrapping.html','r') as htmlfile:
    contents=htmlfile.read()
    soup =BeautifulSoup(contents,"lxml")
    print(soup.prettify())
    courses_html_tags=soup.find_all("h5")
    for courses in courses_html_tags:
        print(courses.text)
    course_cards=soup.find_all("div",class_="card")
    for course in course_cards:
        course_Name=course.h5.text
        course_price=course.a.text.split()[-1]
        print(f'{course_Name} costs {course_price}')
