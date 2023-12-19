import os
import PyPDF2


def read_pdf(pdf_list, txt_list, pdf_path, txt_path):
    if pdf_list:
        try:
            for pdf_file_name, txt_file_name in zip(pdf_list, txt_list):

                pdf_file_path = os.path.join(pdf_path, pdf_file_name)
                txt_file_path = os.path.join(txt_path, txt_file_name)

                with open(pdf_file_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    page_num = len(pdf_reader.pages)

                    with open(txt_file_path, 'w') as txt_file:
                        for num in range(page_num):
                            page = pdf_reader.pages[num]
                            text = page.extract_text()
                            txt_file.write(text)

        except Exception as e:
            print(e)
    else:
        print("Por favor adicione um ou mais arquivos PDF's na pasta 'pdf'💡")


def main():
    root_path = os.getcwd()

    pdf_path = f'{root_path}/pdf'
    pdf_list = [file for file in os.listdir(pdf_path) if file.endswith('.pdf')]

    txt_path = f'{root_path}/txt'
    txt_list = [f'{os.path.splitext(file)[0]}.txt' for file in pdf_list]

    read_pdf(pdf_list, txt_list, pdf_path, txt_path)


if __name__ == "__main__":
    main()
