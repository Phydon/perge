from pypdf import PdfWriter
import argparse


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

    parser.add_argument("files", action="extend", nargs="+", type=str)
    parser.add_argument("--outfile", "-o", action="store", nargs="?", type=str)

    # groups conflict with each other
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--merge", "-m", action="store_true", help="Merge pdf`s")
    group.add_argument("--split", "-s", action="store_true", help="Split pdf`s")

    parser.add_argument(
        "--echo", "-e", action="store_true", help="Prints a message"
    )
    parser.add_argument(
        "--version", "-V", action="version", version="%(prog)s 1.0.0"
    )

    args = parser.parse_args()

    if args.merge:
        if len(args.files) <= 1:
            raise Exception(
                f"2 or more pdf`s needed to merge them together: {len(args.files)} provided"
            )

        if args.outfile:
            merge(args.files, outfile=args.outfile)
        else:
            merge(args.files)
    elif args.split:
        print("This is a PDF splitter")
    elif args.echo:
        print("This echos")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
