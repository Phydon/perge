from pypdf import PdfWriter
import argparse


def merge(*files: str, outfile: str = "merged_pdf.pdf") -> None:
    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)

    merger.write(outfile)
    merger.close()


def main():
    parser = argparse.ArgumentParser(
        prog="Perge", description="PDF Tool", epilog="leann.phydon@gmail.com"
    )

    # groups conflict with each other
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--merge", "-m", action="store_true", help="Merge pdf`s")
    group.add_argument("--split", "-s", action="store_true", help="Split pdf`s")

    parser.add_argument(
        "--echo", "-e", action="store_true", help="Prints a message"
    )

    args = parser.parse_args()

    if args.merge:
        print("This is a PDF merger")
    elif args.split:
        print("This is a PDF splitter")
    elif args.echo:
        print("This echos")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
