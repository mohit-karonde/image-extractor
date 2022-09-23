import pafy

url = "https://www.youtube.com/watch?v=eACohWVwTOc"
video = pafy.new(url)

streams = video.streams
for i in streams:
    print(i)

# get best resolution of a specific format
# set format out of(mp4, webm, flv or 3gp)
best = video.getbest(preftype="3gp")

best.download()
