import webbrowser
from pytube import YouTube
import googlesearch as gs

text="""<!DOCTYPE html>
    <head>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
        <h1>SAPTUBE &#127909;</h1>
        <div class="container">
            <iframe id="yt-player" src="{}" frameborder="5"></iframe>
	</div>            
	<span class="author">Made by <a href="">MASTERMIND</a>.</span>
	<details>
          <summary>More about the video(click here)</summary>
          {}
        </details>
    </body>
</html>"""

while True:
    l=input("Enter youtube link or any query:")
    url=None
    if len(l)==0:
        print("You need to provide a youtube video link or any query")
        continue
    elif l.startswith("https://www.youtube.com/watch?v="):
        url=l
    else:
        s=gs.search("https://www.youtube.com/results?search_query="+l.replace(" ","+"),"com","en",num=10,stop=10,pause=2.0)
        for i in s:
            if i.startswith("https://www.youtube.com/watch?v="):
                url=i
                break
    if url==None:
        print("Some error occured")
        continue

    yt=YouTube(str(url))
    yt_desc=f"""<ul>
                  <li>Title:{yt.title}</li>
                  <li>Description:{yt.description}</li>
                  <li>Author: {yt.author}</li>
                  <li>Duration: {str(yt.length)} seconds</li>
                  <li>Publish date: {str(yt.publish_date)}</li>
                  <li>Rating: {str(yt.rating)}</li>
                  <li>Views: {str(yt.views)}</li>
                </ul>"""

    
    x=url.partition("watch?v=")
    link=x[0]+"embed/"+x[2]+"?playlist="+x[2]+"&loop=1"
    file=open("saptube.html","w")
    file.write(text.format(link,yt_desc))
    file.close()
    webbrowser.open_new_tab("saptube.html")
