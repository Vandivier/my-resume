import os
from jinja2 import Template
from dotenv import load_dotenv
import subprocess

# Load environment variables
load_dotenv()

# Prepare your data from environment variables
data = {"EMAIL": os.getenv("EMAIL"), "PHONE": os.getenv("PHONE")}

# Read the HTML template
template_path = "resume.html"
with open(template_path, "r") as file:
    template = Template(file.read())

# Render the HTML with the interpolated data
rendered_html_path = "interpolated.html"
with open(rendered_html_path, "w") as file:
    file.write(template.render(data))

# Path for the output PDF
pdf_output_path = "resume.pdf"

# Call wkhtmltopdf to convert the interpolated HTML to PDF
subprocess.run(["wkhtmltopdf", rendered_html_path, pdf_output_path])

print("PDF generated successfully!")
