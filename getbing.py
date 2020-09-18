import requests

print("Collecting JSON...")
url_text = requests.get(url="https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1").json()

print("Collecting Image...")
response = url_text["images"][0]["url"]
img_url = f"https://cn.bing.com{response}"
print(img_url)
img = requests.get(img_url)

print("Writing...")
with open("./bing.jpg", "wb") as i:
	i.write(img.content)

print("Done!")
