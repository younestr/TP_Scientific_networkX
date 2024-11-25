from nbconvert import HTMLExporter
import nbformat

# Load the notebook
with open("notebook.ipynb", "r", encoding="utf-8") as f:
    notebook_content = nbformat.read(f, as_version=4)

# Initialize the HTML exporter
html_exporter = HTMLExporter()

# Convert notebook to HTML
(body, resources) = html_exporter.from_notebook_node(notebook_content)

# Write HTML output to a file
with open("TP_Scientific_Network.html", "w", encoding="utf-8") as f:
    f.write(body)
