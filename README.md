# Regex-Generator

[![Build Status](https://travis-ci.com/maojui/Regex-Generator.svg?branch=master)](https://travis-ci.com/maojui/Regex-Generator)
[![](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/maojui/Regex-Generator/blob/master/LICENSE)

## Slide

https://docs.google.com/presentation/d/1iapTfVhuES_MD0Q3F4gFzuFOfiitQasKx4Ff0uKSirQ/edit?usp=sharing

## Paper

[Regular Expression Generator by using genetic alogirthm](https://github.com/maojui/Regex-Generator/blob/master/Regular%20Expression%20Generator%20by%20using%20Genetic%20Algorithm.pdf)

## Usage : 

```bash
git clone https://github.com/maojui/Regex-Generator
cd Regex-Generator
pip install -r requirements
python server.py
```

The service will run on : http://localhost:8080 

![](https://i.imgur.com/0DzOMem.png)

## Example :

Above argument 12 means using testset12, which is a set of random ip address. 

Our process will try to find out a regex to match all input data.

```
Target :
         9.136.40.77
         230.206.226.141
         178.53.157.92
         251.165.48.74
         81.89.99.152
         ...
         122.167.211.226
         53.40.30.228
         7.92.9.53
         84.40.110.26
         38.17.220.185
```

### Result : 

```
3796  \d{1,3}\.\d{2,3}\.\d{1,3}\.\d{1,3}
3639  [1-2]?[0-9]?[0-9]\.[1-2]?[0-9][0-9]\.[1-2]?[0-9]?[0-9]\.[1-9][0-9]?[1-9]?
```



## Others Generator

- [Txt2Re](http://www.txt2re.com/index.php3) - Generate Regular expressions based on a string
- [Regex Generator++](http://regex.inginf.units.it) - Automatic Generation of Text Extraction Patterns from Examples
- [regexgen](https://github.com/devongovett/regexgen) - Generates regular expressions that match a set of strings.
- [RegexGenerator](https://github.com/MaLeLabTs/RegexGenerator) - A tool for generating regular expressions for text extraction (by @MaLeLabTs)
- [Gamon's numberic range generator](http://gamon.webfactional.com/regexnumericrangegenerator/) - Regex Numeric Range Generator, when you need to match an integer range.
- [rgxg](https://rgxg.github.io) - Command line tool to generate Regex
- [Strings to RegEx](https://www.wimpyprogrammer.com/strings-to-regex/) - JavaScript library and online tool to generate a regular expression that matches strings.
- [Regex Guide](https://regex.guide/playground) - Plain Text to Regex Generator.
