import os
import os.path
import time

version = "1.1"

header = (
    "<!DOCTYPE html>"
    "<html>"
    "<head>"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    "<title>Index of {}</title>"
    "<style>"
    ":root {{"
    "  --color-bg: white;"
    "  --color-text: #404040;"
    "  --color-table-bg: white;"
    "  --color-table-bg--head: #efefef;"
    "  --color-table-bg--even: whitesmoke;"
    "  --color-table-text: #222222;"
    "  --color-link-text: #3498db;"
    "  --color-link-text--visited: #8e44ad;"
    "  --color-search-text: #8e44ad;"
    "  --color-search-bg: white;"
    "  --color-search-border: rgba(0, 0, 0, .15);"
    "  --color-search-border--focus: #8e44ad;"
    "}}"
    "@media (prefers-color-scheme: dark) {{"
    "  :root {{"
    "    --color-bg: #222222;"
    "    --color-text: #bbb;"
    "    --color-table-bg: #222222;"
    "    --color-table-bg--head: #181818;"
    "    --color-table-bg--even: #333;"
    "    --color-table-text: #ccc;"
    "    --color-link-text: #3096d5;"
    "    --color-link-text--visited: #9e4ebf;"
    "    --color-search-text: #9e4ebf;"
    "    --color-search-bg: #181818;"
    "    --color-search-border: rgba(255, 255, 255, .15);"
    "    --color-search-border--focus: #9e4ebf;"
    "  }}"
    "body {{"
    "  margin: 0;"
    "  font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", Helvetica, Arial, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";"
    "  font-weight: 300;"
    "  color: var(--color-text);"
    "  background-color: var(--color-bg);"
    "}}"
    "table {{"
    "  width: 100%;"
    "  background: var(--color-table-bg);"
    "  border: 0;"
    "  table-layout: auto;"
    "}}"
    "table thead {{"
    "  background: var(--color-table-bg--head);"
    "}}"
    "table tr th, table tr td {{"
    "  padding: 0.5625rem 0.625rem;"
    "  font-size: 0.875rem;"
    "  color: var(--color-table-text);"
    "  text-align: left;"
    "  line-height: 1.125rem;"
    "}}"
    "table thead tr th {{"
    "  padding: 0.5rem 0.625rem 0.625rem;"
    "  font-weight: bold;"
    "}}"
    "table tr.even {{"
    "  background: var(--color-table-bg--even);"
    "}}"
    "a {{"
    "  text-decoration: none;"
    "  color: var(--color-link-text);"
    "}}"
    "a:hover {{"
    "  text-decoration: underline;"
    "}}"
    "a:visited {{"
    "  color: var(--color-link-text--visited);"
    "}}"
    ".img-wrap {{"
    "  vertical-align: middle;"
    "  display: inline-block;"
    "  margin-right: 8px;"
    "  width: 16px;"
    "  height: 16px;"
    "}}"
    ".img-wrap img {{"
    "  display: block;"
    "  width: 100%;"
    "  height: 100%;"
    "  max-width: none;"
    "  object-fit: contain;"
    "}}"
    ".img-wrap + a {{"
    "  display: inline-block;"
    "  vertical-align: middle;"
    "}}"
    ".hidden {{"
    "  display: none;"
    "}}"
    "#page-header {{"
    "  display: flex;"
    "  align-items: center;"
    "  margin-left: 0.625rem;"
    "  margin-right: 0.625rem;"
    "}}"
    "#search {{"
    "  display: block;"
    "  padding: 0.5rem 0.75rem;"
    "  font-size: 1rem;"
    "  line-height: 1.25;"
    "  color: var(--color-search-text);"
    "  background-color: var(--color-search-bg);"
    "  background-image: none;"
    "  background-clip: padding-box;"
    "  border: 1px solid var(--color-search-border);"
    "  border-radius: 0.25rem;"
    "  margin-left: 1rem;"
    "  -webkit-appearance: textfield;"
    "}}"
    "#search:focus {{"
    "  border-color: var(--color-search-border--focus);"
    "  outline: 0;"
    "}}"
    "@media (max-width: 600px) {{"
    "  .indexcollastmod, .indexcoldesc, .indexcolsize {{"
    "    display: none;"
    "  }}"
    "  h1 {{"
    "    font-size: 1.5em;"
    "  }}"
    "  #page-header {{"
    "    flex-direction: column;"
    "    align-items: flex-start;"
    "    justify-content: flex-start;"
    "    margin-bottom: 1em"
    "  }}"
    "  #search {{"
    "    margin-left: 0;"
    "  }}"
    "}}"
    "@media (max-width: 400px) {{"
    "  h1 {{"
    "    font-size: 1.375em;"
    "  }}"
    "}}"
    "</style>"
    "</head>"
    "<body>"
    "<div id=\"page-header\">"
    "<h1>Index of {}</h1>"
    "<input type=\"text\" id=\"search\" placeholder=\"Search\">"
    "</div>"
    "<table>"
    "<thead>"
    "<tr>"
    "<th>Name</th>"
    "<th>Last Modified</th>"
    "<th>Size</th>"
    "</tr>"
    "</thead>"
    "<tbody>"
)

footer = (
    "</tbody>"
    "</table>"
    "<hr>"
    "</body>"
    "</html>".format(version)
)

icon_mapping = {
    ".txt": "text-icon.png",
    ".pdf": "pdf-icon.png",
    ".doc": "doc-icon.png",
    ".docx": "doc-icon.png",
    ".xls": "xls-icon.png",
    ".xlsx": "xls-icon.png",
    ".ppt": "ppt-icon.png",
    ".pptx": "ppt-icon.png",
    ".png": "image-icon.png",
    ".jpg": "image-icon.png",
    ".jpeg": "image-icon.png",
    ".gif": "image-icon.png",
    ".zip": "archive-icon.png",
    ".rar": "archive-icon.png",
}

def getlink(path, file, isDir):

    file_extension = os.path.splitext(file)[1].lower()
    icon = icon_mapping.get(file_extension, "file-icon.png")

    fileLen = len(file)
    filesz = os.path.getsize(path + "/" + file)
    mtime = os.path.getmtime(path + "/" + file)
    mtime = time.strftime('%d-%b-%Y %H:%M', time.localtime(mtime))

    if not isDir:
        return "<tr><td><img class=\"img-wrap\" src=\"{}\"><a href=\"{}\">{}</a></td><td>{}</td><td>{}</td></tr>".format(
            icon, file, file, mtime, filesz
        )
    else:
        return "<tr><td><img class=\"img-wrap\" src=\"{}\"><a href=\"{}\">{}/</a></td><td>{}</td><td>-</td></tr>".format(
            icon, file, file, mtime
        )


def listfiles(path):

    displaypath = path

    if path == ".":
        displaypath = "/"
    elif displaypath.startswith("./"):
        displaypath = displaypath[1:]

    idx = open(path + "/index.html", "w")

    # Write the header
    idx.write(header.format(displaypath, displaypath))

    # Write back link
    idx.write("<tr><td colspan=\"3\"><a href=\"..\">..</a></td></tr>")

    # Write directories first
    for file in sorted(os.listdir(path)):
        if os.path.isdir(path + "/" + file):
            idx.write(getlink(path, file, True))
            listfiles(path + "/" + file)

    # ... then write files
    for file in sorted(os.listdir(path)):
        if not os.path.isdir(path + "/" + file):
            if file.endswith("index.html"):
                continue
            idx.write(getlink(path, file, False))

    idx.write(footer)
    idx.close()


def main():
    listfiles(".")


if __name__ == "__main__":
    main()
