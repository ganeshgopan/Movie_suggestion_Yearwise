import requests
import bs4

def movie_suggestion_year(url):
	mov=[]
	resp = requests.get(url)
	soup = bs4.BeautifulSoup(resp.content, features="html.parser")
	sugg = soup.find_all("a", attrs = {"class" : "unstyled articleLink"})
	for i in sugg:
		#print(i.get_text())
		mov.append(i.get_text())
	return mov

def select_year(yr):
	x="https://www.rottentomatoes.com/top/bestofrt/?year="
	y= str(yr)
	z= x+y
	year="("+y+")"

	print(f"TOP 100 MOVIES OF THE YEAR {year} ")
	movies=movie_suggestion_year(z)
	for i in movies:
		if i.split(" ")[-1]== year :
			print(i)

def main():
	yr=int(input())
	if len(str(yr))==4:
		select_year(yr)
	else:
		print("WRONG INPUT")


if __name__ =="__main__":
	main()
