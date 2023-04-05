def exists_word(word, instance):
    l_word = word.lower()
    info = []

    for file in range(len(instance)):
        data = instance.search(file)
        word_qty = []
        for index, row in enumerate(data["linhas_do_arquivo"]):
            if l_word in row.lower():
                word_qty.append({"linha": index + 1})

        if word_qty:
            info.append({
                        "palavra": word,
                        "arquivo": data["nome_do_arquivo"],
                        "ocorrencias": word_qty
                        })

    return info


def search_by_word(word, instance):
    l_word = word.lower()
    info = []

    for file in range(len(instance)):
        data = instance.search(file)
        word_qty = []
        for index, row in enumerate(data["linhas_do_arquivo"]):
            if l_word in row.lower():
                word_qty.append({"linha": index + 1, "conteudo": row})

        if word_qty:
            info.append({
                        "palavra": word,
                        "arquivo": data["nome_do_arquivo"],
                        "ocorrencias": word_qty
                        })

    return info
