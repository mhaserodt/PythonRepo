#A quick tool for work to convert a bunch of PDFs to CSVs
import tabula
import os

cwd = os.getcwd()

tabula.io.convert_into_by_batch(cwd, pages='all', output_format='csv', java_options=None, stream=True)
