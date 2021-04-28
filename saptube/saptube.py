import webbrowser
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
    </body>
</html>"""

while True:
    l=input("Enter youtube link:")
    x=l.partition("watch?v=")
    link=x[0]+"embed/"+x[2]+"?playlist="+x[2]+"&loop=1"
    file=open("saptube.html","w")
    file.write(text.format(link))
    file.close()
    webbrowser.open_new_tab("saptube.html")
