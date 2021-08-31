path = r"/home/jay/PycharmProjects/pythonProject/excercise 7/reci.pdf"
import pdftotext
with open(path, "rb") as f:
    pdf = pdftotext.PDF(f)
pdftotext_text = "\n\n".join(pdf)

print(pdftotext_text)