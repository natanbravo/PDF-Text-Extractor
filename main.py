import PyPDF2


def read_pdf(pdf_path, txt_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page_num = len(pdf_reader.pages)

            with open(txt_path, 'w') as txt_file:

                for num in range(page_num):
                    page = pdf_reader.pages[num]
                    text = page.extract_text()
                    txt_file.write(text)

    except Exception as e:
        print(e)


def main():
    pdf_path = './content.pdf'
    txt_path = './content.txt'
    read_pdf(pdf_path, txt_path)


if __name__:
    main()
