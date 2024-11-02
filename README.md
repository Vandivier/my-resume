# my-resume

My version-controlled markdown resume with pdf export style control.

I care about the style control so that I can better comply with resume best practices such as restricting the resume to a single page.

It's a good idea to ensure your output resume is ATS compliant by testing it with the Indeed Resume Scan tool:
https://www.indeed.com/career-services/resume-help/instant-report/?collectorID=rescan

## Recommended Workflow

Please don't write out the HTML by hand. That's too much work.

Instead:

1. Export your LinkedIn resume built with the [LinkedIn Resume Builder](https://www.linkedin.com/help/linkedin/answer/a551182).
2. Use GPT-4 to convert the LinkedIn-built PDF into `resume.html`. See the `GPT-4 Prompt` section for more tips about the specific prompt to use.
3. Replace this repository's `resume.html` with your own.
4. Ensure you have `wkhtmltopdf` installed locally.
   1. On mac, this is `brew install wkhtmltopdf`. Don't worry if you see a deprecation notice on that install.
5. Run `poetry install` in this repo. If you need poetry, try `pipx install poetry`.
6. Run `poetry run python create-pdf-resume.py`
   1. Please ensure `python` refers to Python v3.11+
   2. You can try it with a lower version, but you may need to update the pyproject.toml file, and reinstall, and it also might not work.
7. Optional: Remove `resume.pdf` from `.gitignore`.
   1. Benefit: This publishes the final form of your resume to GitHub
   2. Cost/Risk: If your resume has sensitive or personal data on it, that data will be published to the open web.

## Known Limitations

You cannot make the HTML body background pink.

Basically, styling on the HTML body tag may fail to transpile into PDF.

## GPT-4 Prompt

The recommended approach has four steps:

1. Attach your linkedin-resume.pdf to GPT-4
2. Paste the existing resume.html from this repository into the prompt window
3. Write a new line, a triple-dash seperator (`---`), and another new line
4. Write `Consider the attached resume PDF. Please create a resume HTML form of the content based on the HTML template provided above.`

You may need to tinker with the output. You can also try prompting from scratch.

#### Prompting from Scratch

In this approach, you do not paste any existing HTML. You should still attach your LinkedIn-generated PDF resume. Then you can use a prompt like the below, which was used to generate the resume.html found in this repository:

```
Consider the attached LinkedIn resume PDF.
Let's create an HTML representation of this resume.
Do not skip or summarize any content except for items I specifically ask you to omit from the HTML.
Doing that would harm the quality of my resume, and we want to generate a high-quality resume.
Do not use an HTML footer tag.
The resume should have three sections: The top matter which includes my name, title, contact details, and summary paragraph is the first section.
My name and title should be treated as the heading of the top matter section.
`Experience` is the second section
`Education` is the third section
Add a thin horizontal divider across the page between each section change.

Specify my phone number as the literal `Phone: {{ PHONE }}`,
so that I can store it in a dotenv file and interpolate it later.
Do similarly with email.
This way I can save my HTML file on GitHub without exposing my sensitive data.
Include my GitHub and LinkedIn URLs in the ordinary way.

For work experience entries,
use a subheading with the format `{{ POSITION }} at {{ EMPLOYER_NAME }}`,
but do not literally include the braces. That's just to show you where to put each bit.
For contract experience, append `- Contract` to the position name`.

For education dates, use years without specifying the month.
Follow the format:
`<section>
   <h3>{{ CREDENTIAL NAME }}</h3>
   <p>{{ INSTITUTION }}</p>
   <p>{{ START DATE }} - {{ END DATE}}</p>
</section>`,
but do not literally include the braces. That's just to show you where to put each bit.

Remove my high school education entry.
Retain the Summary section.
Ignore the Skill and Achievement sections.
Do not include images in the HTML resume.

Keep the font size equal for p tags and for h3 or smaller headings,
with a 12px font size.
Use at most 0.5rem for any margin or padding needed.
Paragraphs should not have padding nor horizontal margin.
Remove the left indentation from all lists.
```
