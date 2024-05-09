# my-resume

My version-controlled markdown resume with pdf export style control.

I care about the style control so that I can better comply with resume best practices such as restricting the resume to a single page.

## Recommended Workflow

Please don't write out the HTML by hand. That's too much work.

Instead:

1. Export your LinkedIn resume built with the [LinkedIn Resume Builder](https://www.linkedin.com/help/linkedin/answer/a551182).
2. Use GPT-4 to convert the LinkedIn-built PDF into `resume.html`.
   1. It is recommended prompt GPT-4 to build this HTML file without images.
   2. Optionally, let GPT-4 know that you want sensitive data interpolated from a dotenv file like `<p>Phone: {{ PHONE }}</p>`.
3. Replace this repository's `resume.html` with your own.
4. Ensure you have `wkhtmltopdf` installed locally.
   1. On mac, this is `brew install wkhtmltopdf`. Don't worry if you see a deprecation notice on that install.
5. Run `poetry install` in this repo.
6. Run `poetry run python create-pdf-resume.py`
   1. Please ensure `python` refers to Python v3.11+
   2. You can try it with a lower version, but you may need to update the pyproject.toml file, and reinstall, and it also might not work.
7. Optional: Remove `resume.pdf` from `.gitignore`.
   1. Benefit: This publishes the final form of your resume to GitHub
   2. Cost/Risk: If your resume has sensitive or personal data on it, that data will be published to the open web.

## Known Limitations

You cannot make the HTML body background pink.

Basically, styling on the HTML body tag may fail to transpile into PDF.
