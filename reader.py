import PyPDF2 as pdf
import re
from docx import Document


# opens pdf in a readable fashion -done
def open_PDF(input_text, input_page):
    # add assert statements for pdf file and page number
    pdfobject = open(input_text, "rb")
    pdfread = pdf.PdfFileReader(pdfobject)
    page = convert_to_pdf(input_page, pdfread)
    page = page.replace("\n", "")
    page = page.replace("- ", "")
    return page


# removes citations -done
def removing_cite(text):
    for c in text:
        if c == "(":
            text = text[: text.find("(")] + text[text.find(")") + 1 :]
    return text


# parse all sentences
def important_sentences(wholetext, doc, words):
    if len(wholetext) <= 1:  # if there is <=1 character, the analyzing is finished
        return doc

    first_sentence = wholetext[
        : wholetext.find(".") + 1
    ]  # take out a sentence to analyze
    rest_of_text = wholetext[
        wholetext.find(".") + 1 :
    ]  # get rid of the first sentence and keep the rest

    if (
        wholetext[wholetext.find(".") + 1] == '"'
    ):  # if the next character after period is a quote, change index
        first_sentence = wholetext[: wholetext.find(".") + 3]
        rest_of_text = wholetext[wholetext.find(".") + 2 :]

    for w in words:  # look through keywords that is in the text file
        if (
            w in first_sentence
        ):  # if one of the words are in the sentence, add it to document
            doc.add_paragraph(
                first_sentence, style="List Bullet"
            )  # add to document using bullet points
            first_sentence = (
                ""
            )  # after adding, reset the first sentence to prevent any dups
    important_sentences(rest_of_text, doc, words)  # recursion


def convert_to_pdf(pages, pdf):
    # pages = int
    text = ""
    for page in range(int(pages)):
        text += pdf.getPage(page).extractText()
    return text


print("Reader: done")

