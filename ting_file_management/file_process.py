from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)

    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    instance.enqueue(info)
    sys.stdout.write(str(info))

    return info


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    file = instance.dequeue()
    return sys.stdout.write(
        f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        return sys.stderr.write("Posição inválida\n")

    file = instance.search(position)

    return sys.stdout.write(str(file))
