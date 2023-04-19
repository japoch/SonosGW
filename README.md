# Sonos Gateway

[![CI](https://github.com/japoch/ansible/actions/workflows/ci.yml/badge.svg)](https://github.com/japoch/ansible/actions/workflows/ci.yml)
[![Pylint](https://github.com/japoch/SonosGW/actions/workflows/pylint.yml/badge.svg)](https://github.com/japoch/SonosGW/actions/workflows/pylint.yml)

## Description

This is a gateway for [Sonos wireless speakers and home sound systems](https://www.sonos.com).

## Dependencies

### General
- Python 3
- Pip 22.0.4
- Flask 2.2

### Python and Python Packages

To find a full list (incl. needed Versions) of required packages you can have a look into **requirements.txt**.

Create venv
```bash
python3 -m venv venv
```

Install needed packages with pip.
```bash
pip install -r requirements.txt
```

## Build and Run

```bash
# development environment
flask run
# production environment
cd src && gunicorn webapp:app
```

## Linting

Run Super-Linter locally to test your branch of code.
```bash
docker pull github/super-linter:v5
docker run --rm -e RUN_LOCAL=true -e USE_FIND_ALGORITHM=true -v "$PWD/src":/tmp/lint github/super-linter:v5
```

## Links

[SONOS API Documents](https://musicpartners.sonos.com/?q=docs "API Documents & Tools")

[Stream What You Hear](https://www.streamwhatyouhear.com/ "Stream the sound from your PC to an UPnP/DLNA device")
