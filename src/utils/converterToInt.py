def converterToInt(str_comission):
    int_comission = (
    int(
        str_comission.replace("R$", "")
            .replace(" ", "")
            .replace(",", "")
            .replace(".", "")
            )
        ) / 100
    return int_comission