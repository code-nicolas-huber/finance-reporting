# Finance-Reporting

[![code-nicolas-huber - finance-reporting](https://img.shields.io/static/v1?label=code-nicolas-huber&message=finance-reporting&color=blue&logo=github)](https://github.com/code-nicolas-huber/finance-reporting "Go to GitHub repo")
[![stars - finance-reporting](https://img.shields.io/github/stars/code-nicolas-huber/finance-reporting?style=social)](https://github.com/code-nicolas-huber/finance-reporting)
[![forks - finance-reporting](https://img.shields.io/github/forks/code-nicolas-huber/finance-reporting?style=social)](https://github.com/code-nicolas-huber/finance-reporting)
[![GitHub tag](https://img.shields.io/github/tag/code-nicolas-huber/finance-reporting?include_prereleases=&sort=semver&color=blue)](https://github.com/code-nicolas-huber/finance-reporting/releases/)
[![issues - finance-reporting](https://img.shields.io/github/issues/code-nicolas-huber/finance-reporting)](https://github.com/code-nicolas-huber/finance-reporting/issues)
[![License](https://img.shields.io/badge/License-INDIVIDUAL-blue)](#license)

## Abstract

The finance-reporting tool is part of the [nicolas-huber](https://github.com/code-nicolas-huber/code-nicolas-huber) software suite and extends the functionality of `finance.nicolas-huber` by enabling financial data analysis using a CLI.

---

## License

The source code of this application is licensed under the license linked [here](LICENSE.md).

---

## Technical documentation

The following documentation is intended for developers. Please visit [finance.nicolas-huber](https://finance.nicolas-huber.ch/pages/data/data-tools) for a detailed user-oriented documentation. Please note that this page requires a user account on the `finance.nicolas-huber` platform. You might also find an answer to your question on the public [support page](https://finance.nicolas-huber.ch/pages/system/support). Keep in mind that the `finance.nicolas-huber` site is only available in German language.

_Please note: Proper linting and formatting are both missing in this project. Make sure to use tools like pylint and Black if you put further efforts into this project. :-) This tool serves educational purposes and thus won't be updated to professional guidelines and standards._

### Introduction

`finance-reporting` is a powerful tool designed to extend the functionality of the `finance.nicolas-huber` platform. It provides a command-line interface for financial data analysis, allowing individuals to process and interpret financial data more efficiently.

This tool is part of the [nicolas-huber](https://github.com/code-nicolas-huber/code-nicolas-huber) software suite and is developed exclusively by Nicolas Huber. It is designed to extend `finance.nicolas-huber` but can also be extended for other applications.

The `FINANCE.py` file is the main entry point of the application. It contains the core functionalities and the command-line interface for the tool. For more detailed information about the usage and architecture of the tool, please refer to the respective sections in this documentation.

### Getting started

#### Prerequisites

In order to run this project, make sure to install Python `3.12` on your machine.

#### Installation

Clone this repository, enter the project directory and run `pip3 install -r requirements.txt`, which will install the project dependencies.

#### Basic Usage

After installing the application you can execute the file `FINANCE.py`, which is the main entry point of the application. The system dialogue is written in German Language but can be adapted if needed. 

The system reads CSV tables containing transaction data and currently requires a table header of the following format:

```csv
ID;User;Konto;Kategorie;Datum;Buchungstext;Transaktionsnummer;Betrag;Währung;Status
```

You can generate reportings in Markdown, HTML and PDF format.

### Architecture

The application is structured as follows:

```txt
finance-reporting
|-- assets/
| -- src/ |
| ------- || classes/ |
| -------- ||     | constants/ |
| --- ||functions/
|-- FINANCE.py
|-- LICENSE.md
|-- README.md
|-- requirements.txt
```

### Contributing

At this time, the `finance-reporting` project is not open for community contributions. The development is currently handled exclusively by Nicolas Huber. Your interest is appreciated and this section will be updated if the policy changes in the future. 

### Changelog

#### [1.0.0] - 11/10/2023

- Initial release of the project

---

## Support

If you find this tool useful and would like to support the ongoing development and maintenance, you might want to consider "buying me a coffee". Any support is greatly appreciated and will go directly into creating more useful software. You can support me on [Buy me a coffee](https://www.buymeacoffee.com/nicolashuber) or reach me at [nicolas-huber.ch](https://nicolas-huber.ch). Thank you for your generosity and support!

[![Buy me a coffee](assets/black-button.png)](https://www.buymeacoffee.com/nicolashuber)

---

## Disclaimer

The author is not responsible for any damage caused by the use of the software.

---

_© 2023, [Nicolas Huber](https://nicolas-huber.ch). All rights reserved._