from io import StringIO
from pdfminer.high_level import extract_text_to_fp, extract_text

output_string = StringIO()
with open('data/example.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string, output_dir='out_images')

text = extract_text('data/example.pdf')
print(repr(text.strip()))
