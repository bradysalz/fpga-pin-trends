# FPGA Pin Trends

I was doing some hardware designs with FPGAs the other day at work, and on the face of it, it's pretty ridiculous how many pins are just power and ground. I get why - signal integrity, power integrity, all the good stuff, but when did this start becoming a thing? Someone at work said the general rule is four IO pins to one GND pin, but is that really teh case? This repo is a side project of mine to make some neat data visualizations to find out what these trend line really are.

This repo is probably going to be 90% code dedicated to data cleanup, and 10% ~~machine learning~~ plotting.

## Getting Started

## Data Overview

This entire repo revolves around pin-outs of a huge number of components, none of which were designed by me. I've included this data in the repo under `data/` in order to make everything simpler. It's organized as:
```
data
├───manufacturer_A
│   ├───product_family_a
|   |   ├───overview.toml
│   │   ├───part_12.csv
│   │   └───part_34.csv
│   ├───product_family_b
|   |   ├───overview.toml
│   │   ├───part_56.csv
│   │   └───part_78.csv
│   └───product_family_c
└───manufacturer_X
```

The `overview.toml` file contains the generational parameters of the product family. For now, it's only a few items:

1. `node`: the CMOS process node the family was fabricated on [assumes nanometer CMOS]
2. `year`: the year the device family came out
3. `parser`: which parser to use for this product family

All of the pin out data comes from downloading (a huge number) of files from these two sites:

* [Intel Altera Pin-Outs](https://www.intel.com/content/www/us/en/programmable/support/literature/lit-dp.html)
* [Xilinx Package Files Portal](https://www.xilinx.com/support/package-pinout-files.html)


## License

There's no `LICENSE` file here - the data is not mine, but I've included the relevant licenses when made available. For anything code I write, that's always going to be [WTFPL](http://www.wtfpl.net/about/). For the images that get produced, I'll probably do some Wikipedia style CC BY-SA. Will update this when I get to that stage!

## Citations

TODO... if ever :shrug:
