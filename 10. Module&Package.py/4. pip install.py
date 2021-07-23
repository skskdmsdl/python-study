# pip로 패키지 설치하기
# 구글에서 pypi 검색 👉 https://pypi.org/ 후 필요한 패키지 사용
# beautifulsoup 검색 👉 상세에 pip install 부분 복사 후 터미널에서 설치
# 👉 사용해 보기 위해 Quick start에 있는 부분 복사해서 테스트 해보기
# pip list를 통해 현재 설치된 패키지 목록 확인 가능
# pip show beautifulsoup4를 통해 패키지 정보 확인 가능

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
