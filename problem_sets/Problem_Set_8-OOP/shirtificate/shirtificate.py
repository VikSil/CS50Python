from fpdf import FPDF
from fpdf import Align


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica 150
        self.set_font("helvetica", size=40)
        # Printing title:
        self.cell(txt="CS50 Shirtificate", w=0, align="C")


def main():
    text = input("Name: ").lower().title() + " took CS50"
    print(text)

    makeshirt(text)


def makeshirt(text):
    pdf = PDF()
    pdf.add_page()

    pdf.image("shirtificate.png", Align.C, 50, w=180)

    pdf.set_font("helvetica", size=20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(100)
    pdf.cell(txt=text, w=0, align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
