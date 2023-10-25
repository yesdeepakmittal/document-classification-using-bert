FROM python

LABEL Creator: "Deepak Mittal"

WORKDIR /.

RUN apt-get update && apt-get install -y tesseract-ocr && apt-get clean

RUN pip install pytesseract


