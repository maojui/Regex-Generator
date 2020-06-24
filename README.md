# Regex-Generator

[![Build Status](https://travis-ci.com/maojui/Regex-Generator.svg?branch=master)](https://travis-ci.com/maojui/Regex-Generator)

## Slide

https://docs.google.com/presentation/d/1iapTfVhuES_MD0Q3F4gFzuFOfiitQasKx4Ff0uKSirQ/edit?usp=sharing


## Usage : 

```bash
git clone https://github.com/maojui/Regex-Generator
cd Regex-Generator
pip install -r requirements
python server.py
```

The service will run on : http://localhost:8080 

![](https://i.imgur.com/Sej2cJO.png)

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