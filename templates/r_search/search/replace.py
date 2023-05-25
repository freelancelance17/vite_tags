import fileinput
import os

assets_list = os.listdir('./dist/assets/')

# get the file names from the assets directory
js = assets_list[0] if assets_list[0].endswith(".js") else assets_list[1]
css = assets_list[1] if assets_list[1].endswith(".css") else assets_list[0]

js = f'<script type="module" crossorigin src="/assets/{js}"></script>'
css = f'<link rel="stylesheet" href="/assets/{css}">'

with fileinput.FileInput("./dist/index.html", inplace=True, backup=".bak") as file:
    for line in file:
        print(line.replace(js, ''), end="")

with fileinput.FileInput("./dist/index.html", inplace=True, backup=".bak") as file:
    for line in file:
        print(line.replace(css, ""), end="")

