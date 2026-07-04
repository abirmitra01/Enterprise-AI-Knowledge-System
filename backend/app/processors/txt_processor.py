def extract_txt_text(filepath):

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()