# FPGA Pin Trends

I was doing some hardware designs with FPGAs the other day at work, and on the face of it, it's pretty ridiculous how many pins are just power and ground. I get why - signal integrity, power integrity, all the good stuff, but when did this start becoming a thing? Someone at work said the general rule is four IO pins to one GND pin, but is that really the case? This repo is a side project of mine to make some neat data visualizations to find out what these trend line really are.

This repo is probably going to be 90% code dedicated to data cleanup, and 10% ~~machine learning~~ plotting.

![VCC Pins and GND Pins](/img/vcc_vs_gnd.png)

## Getting Started

This requires Python 3.6+. Install all required libraries with:

```
pip install -r requirements.txt
```

If you wish to re-generate the database, you can do that with:

```
python -m db.build_db
```

Otherwise, just play around with `plot.py`. See `./plot.py --help` for more info.

## Data

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

### Data Overview

The `overview.toml` file contains the generational parameters of the product family. The base set of information is:

1. `node`: the CMOS process node the family was fabricated on [assumes nanometer CMOS]
2. `year`: the year the device family came out
3. `parser`: the parser function to use for this product family
4. `manufacturer`: the OEM who made this component
5. `family`: the OEM's designated product family (if applicable)

All of the pin out data comes from downloading (a huge number) of files from these two sites:

* [Intel Altera Pin-Outs](https://www.intel.com/content/www/us/en/programmable/support/literature/lit-dp.html)
* [Xilinx Package Files Portal](https://www.xilinx.com/support/package-pinout-files.html)

I've shortened "Intel Altera" to simply "Altera" everywhere else, for simplicity. See **Licenses** below on using them.

### Images

All the images I thought were neat are tracked in the repo under the `img/` folder.

## Status

Repo is in a usable but not necessarily complete state. Some quick notes for myself on what to work on next:

- [x] Xilinx parsing
- [x] Cyclone parsing
- [ ] Finish Altera parsing
- [ ] Add some tests
- [ ] Clean up/refactor parsers
- [ ] Make more plots using other factors (`manufacturer`, `family`?)

## License

The whole `data/` folder belongs to the original manufacturer(s). Most files contain the legal information associated with that file (e.g. [`data/xilinx/ultrascale_qualified/xqku5pffrb676pkg.csv`](data/xilinx/ultrascale_qualified/xqku5pffrb676pkg.csv)).

All code is MIT licensed. See [`LICENSE.txt`](LICENSE.txt).

All images are licensed under the [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/). See [`img/CC-BY-SA-40.txt`](img/CC-BY-SA-40.txt).

### Citations

If you use this data elsewhere, I would love to know! You can cite the repo as:

```
@Misc{,
  author =    {Braedon Salz},
  title =     {FPGA Pin Trends},
  year =      {2018--},
  url = "https://github.com/bradysalz/fpga-pin-trends/",
  note = {[Online; accessed <today>]}
}
```
