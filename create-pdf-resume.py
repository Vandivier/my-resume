import os
from jinja2 import Template
from dotenv import load_dotenv
import subprocess
import glob

# Load environment variables
load_dotenv()

# Prepare your data from environment variables
data = {"EMAIL": os.getenv("EMAIL"), "PHONE": os.getenv("PHONE")}

# Get all resume HTML files in the current directory
template_files = glob.glob("resume*.html")

for template_path in template_files:
    with open(template_path, "r") as file:
        template = Template(file.read())

    # Create a corresponding HTML and PDF file name
    base_name = os.path.splitext(template_path)[0]
    rendered_html_path = f"{base_name}_interpolated.html"
    pdf_output_path = f"{base_name}.pdf"

    # Render the HTML with the interpolated data
    with open(rendered_html_path, "w") as file:
        file.write(template.render(data))

    # Call wkhtmltopdf to convert the interpolated HTML to PDF
    subprocess.run(["wkhtmltopdf", rendered_html_path, pdf_output_path])

print("PDFs generated successfully!")
