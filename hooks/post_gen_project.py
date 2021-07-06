import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{ cookiecutter.open_source_license }}" == "Not open source":
    remove(os.path.join(os.getcwd(), "{{cookiecutter.project_slug}}", "LICENSE"))


print("Done!! Now, you can develop Django project!!")
