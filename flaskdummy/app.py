import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import openai
import numpy as np
# import pywhatkit as kit
import textwrap
from fpdf import FPDF
import webbrowser

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx'}

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)
    pdf.output(filename, 'F')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            # return redirect(url_for('uploaded_file', filename=filename))
            reader = PdfReader(f"uploads/{filename}")
            page = reader.pages[0]
            openai.api_key = "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"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="Extract questions from the given text. Write answers in about 200 words in a numbered manner. Also display the question before each answer" + page.extract_text(),
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            text = response["choices"][0]["text"]
            # print(response)

            print(text)
            with open('readme.txt', 'w') as f:
                f.writelines(text)
            input_filename = 'readme.txt'
            output_filename = 'output.pdf'
            file = open(input_filename)
            text = file.read()
            file.close()
            text_to_pdf(text, output_filename)
            webbrowser.open_new(r'output.pdf')
            # kit.text_to_handwriting(text, save_to="handwriting.png")
            # img = cv2.imread("handwriting.png")
            # cv2.imshow("Text to Handwriting", img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # image = np.zeros((500, 500, 3), np.uint8)
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(image, text, (50, 250), font, 1, (255, 255, 255), 2)
            # cv2.imwrite("handwriting.png", image)

    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
