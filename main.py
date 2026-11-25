import os

LINE = "I resign. After 512 attempts, I have learned the server isn't down. It just isn't that into us."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as entry_file:
        entry_file.write(LINE)


if __name__ == "__main__":
    main()
