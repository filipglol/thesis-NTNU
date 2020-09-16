import os 

"""
This script builds the latex file
"""

if __name__ == "__main__":
    os.system("biber thesis")
    os.system("pdflatex thesis.tex")
    os.system("biber thesis")
    os.system("pdflatex thesis.tex")
