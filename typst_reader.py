import json
import re
import subprocess
from pathlib import Path

from pelican.plugins import signals
from pelican.readers import BaseReader


class TypstReader(BaseReader):
    file_extensions = ("typ",)

    def __init__(self, settings):
        super().__init__(settings)
        self.typst = str(Path(__file__).with_name("typst"))
        self.root = str(Path(settings["PATH"]).resolve())

    def run_typst(self, *arguments):
        return subprocess.run(
            [self.typst, *arguments],
            capture_output=True,
            check=True,
            text=True,
        ).stdout

    def read(self, source_path):
        relative_path = Path(source_path).relative_to(self.root).as_posix()
        metadata = json.loads(
            self.run_typst(
                "eval",
                "--features=html",
                "--target=html",
                f"import {json.dumps(relative_path)}: metadata; metadata",
                "--root",
                self.root,
            )
        )
        document = self.run_typst(
            "compile",
            "--features=html",
            "--format=html",
            "--pretty",
            source_path,
            "-",
            "--root",
            self.root,
        )
        body = re.search(r"<body[^>]*>(.*)</body>", document, re.DOTALL)
        if body is None:
            raise ValueError("Typst did not produce an HTML body")

        metadata = {
            name: self.process_metadata(name, value) for name, value in metadata.items()
        }
        return body.group(1).strip(), metadata


def add_reader(readers):
    readers.reader_classes["typ"] = TypstReader


def register():
    signals.readers_init.connect(add_reader)
