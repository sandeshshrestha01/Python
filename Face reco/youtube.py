from  pytube import YouTube

YouTube('https://youtu.be/k8htEz293vo?si=7c1HyRyEvsKAbNBf').streams.first().download()