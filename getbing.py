import json, requests

print("Collecting JSON...")
url = "https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
url_text = requests.get(url=url).text

print("Collecting Image...")
response = json.loads(url_text)["images"][0]["url"]
img_url = "https://bing.com" + response
img = requests.get(img_url)

print("Writing...")
with open("./bing.jpg", "wb") as i:
	i.write(img.content)

print("Done!")