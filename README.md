# steampie
[![License](https://img.shields.io/github/license/offish/steampie.svg)](https://github.com/offish/steampie/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/offish/steampie.svg)](https://github.com/offish/steampie/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/steampie.svg)](https://github.com/offish/steampie/issues)
[![Size](https://img.shields.io/github/repo-size/offish/steampie.svg)](https://github.com/offish/steampie)
[![Discord](https://img.shields.io/discord/467040686982692865?color=7289da&label=Discord&logo=discord)](https://discord.gg/t8nHSvA)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

`steampie` is a Python library for interacting with Steam, and is a modified fork of [bukson](https://github.com/bukson)'s [steampy](https://github.com/bukson/steampy).

## Donate
* BTC: `bc1qntlxs7v76j0zpgkwm62f6z0spsvyezhcmsp0z2` (offish)
* [Steam Trade Offer](https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR) (offish)
* BTC (bukson): `3PRzESHsTVkCFK7osjwFGQLZjSf7qXP1Ta` (bukson)
* [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=XC8BMJ8QRD9ZY) (bukson)

## Installation
```bash
pip install steampie
```

### Update
```bash
pip install --upgrade steampie
```

## Differences from `steampy`
<!-- * Added functionality for adding/removing friends -->
* Removed market functionality due to Steam having strict ToS regarding market automation
* Uses [ruff](https://github.com/astral-sh/ruff) for formatting and linting
* Uses [pytest](https://pytest.org/) for unit tests

<!-- ## Usage


## Examples


## Developing -->


### Tests
```bash
# steampie/
pytest
```

### Building documentation
```bash
# steampie/
cd docs/
make clean
make html
```

## License
MIT License

Copyright (c) 2016 [Michał Bukowski](mailto:gigibukson@gmail.com) <br>
Copyright (c) 2024 offish ([confern](https://steamcommunity.com/id/confern))

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
