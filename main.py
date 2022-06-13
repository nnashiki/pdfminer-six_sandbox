from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('data/example.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string, output_dir='out_images')
print(output_string.getvalue())
