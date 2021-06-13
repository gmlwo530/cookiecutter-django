
# Cookiecutter-Django

Cookiecutter Django template


## Usage

First, you should have cookiecutter in your machine. If you don't have, install it.
- Installation: [https://cookiecutter.readthedocs.io/en/1.7.2/installation.html](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)

Then, Generate Django project.

```bash
$ cookiecutter https://github.com/gmlwo530/cookiecutter-django.git
```

  
## Run Django Project

Run in local

```bash
  $ docker-compose build
  $ docker-compose up
```

Run in production

```bash
  $ docker-compose -f docker-compose-deploy.yml build
  $ docker-compose -f docker-compose-deploy.yml up
```

  
## Roadmap

[ ] coverage
[ ] CI
[ ] CD
[ ] MySQL
[ ] No docker
[ ] Django Rest Framework
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Authors

- [@gmlwo530](https://github.com/gmlwo530)

  