#!/usr/bin/env python

import os

from jinja2 import Environment, FileSystemLoader
import pdfkit

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

def render_template(filename):
	return env.get_template(filename).render(
		test_field1 = 'Sample Text1',
		test_field2 = 'Sample Text2'
	)

def generate_pdf_css(template_filename, css_filename, output_filename):
	pdfkit.from_string(render_template(template_filename), output_filename, css=css_filename)

def generate_pdf(template_filename, output_filename):
	pdfkit.from_string(render_template(template_filename), output_filename)

if __name__ == "__main__":
	generate_pdf_css('template.j2', 'styles.css', 'out.pdf')