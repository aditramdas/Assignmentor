# Assignmentor
Assignmentor is a tool born to help the students from the hectic task of doing all the boring assignments. To use our tool, all you have to do is upload your assignment pdf(containing all the questions) and just hit the solve button. Wait a few seconds and see the magic unfold. You will be presented with a pdf containing the answers of the above questions(in a questions answer format) which you will be able to download.

# Team Members
1) Arjun A I    ->  https://github.com/Arjun-A-I
2) Adith Ramdas ->  https://github.com/aditramdas
3) Aslam Naseer ->  https://github.com/Aslam-Naseer

# Team Id - 

# Link To Video - [Assignmentor](https://www.youtube.com/watch?v=mdo_DFsofEw)

# How the tool works
We first take in the pdf uploaded by the user and extract text from it. After extracting, we process the text and input the text to OpenAI after parsing the text into questions. The answers given by the OpenAI engine is stored into a text value. The text value is converted to handwriting and exported as a pdf,  which is then shown to the user for download.
[Demo](https://www.youtube.com/watch?v=mdo_DFsofEw)

# Libraries Used
Latest versions of the libraries were used.
* Flask
* PyPDF2 
* textwrap
* FPDF
* PIL
* webbrowser

# How to configure and Run
Clone this repo into your local machine. Open the flaskdummy folder, and open the app.py file. Install the dependencies using pip. Place your OpenAI api key in the placeholder field. Change the font of the output according to your wish, by downloading the required font from the net, and replacing the font name. Now run the python file.
