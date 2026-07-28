import re
import subprocess

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

MATH = re.compile(r"\$\$(.+?)\$\$|(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL)
TYPST = ["./typst", "compile", "--features", "html", "--format", "html", "-", "-"]

class TypstMathPreprocessor(Preprocessor):
    def run(self, lines):
        def replace_math(match):
            display, inline = match.groups()
            expression = (display or inline).strip()
            equation = f"$ {expression} $" if display is not None else f"${expression}$"
            html = subprocess.check_output(TYPST, input=equation, text=True)
            return self.md.htmlStash.store(
                re.search(r"<math.*?</math>", html, re.DOTALL).group()
            )

        return MATH.sub(replace_math, "\n".join(lines)).split("\n")

class TypstMathExtension(Extension):
    def extendMarkdown(self, markdown):
        markdown.preprocessors.register(TypstMathPreprocessor(markdown), "typst_preprocessor", 30)

def makeExtension(**kwargs):
    return TypstMathExtension(**kwargs)
