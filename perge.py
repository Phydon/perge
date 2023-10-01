from pypdf import PdfWriter

import argparse
import shutil


def copy_pdf(src: list[str]) -> None:
    for file in src:
        dst = "copy_of_" + file
        shutil.copy2(file, dst)


def merge(files: list[str], outfile: str = "merged_pdf.pdf") -> None:
    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)

    merger.write(outfile)
    merger.close()


def main():
    parser = argparse.ArgumentParser(
        prog="Perge", description="PDF Tool", epilog="leann.phydon@gmail.com"
    )

    parser.add_argument(
        "files",
        action="extend",
        nargs="+",
        type=str,
        help="the pdf files to work with",
    )
    parser.add_argument(
        "--outfile",
        "-o",
        action="store",
        nargs="?",
        type=str,
        help="provide a custom name for the output file",
    )
    parser.add_argument(
        "--copy",
        "-c",
        action="store_true",
        help="make a copy of the provided files before working with them",
    )

    # groups conflict with each other
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--merge", "-m", action="store_true", help="merge pdf`s")
    group.add_argument("--split", "-s", action="store_true", help="split pdf`s")

    parser.add_argument(
        "--version", "-V", action="version", version="%(prog)s 1.0.0"
    )

    args = parser.parse_args()

    if args.merge:
        if len(args.files) <= 1:
            raise Exception(
                f"2 or more pdf`s needed to merge them together: {len(args.files)} provided"
            )

        if args.copy:
            copy_pdf(args.files)

        if args.outfile:
            merge(args.files, outfile=args.outfile)
        else:
            merge(args.files)
    elif args.split:
        if args.copy:
            copy_pdf(args.files)

        print("This is a PDF splitter")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
