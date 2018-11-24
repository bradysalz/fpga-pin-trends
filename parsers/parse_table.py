from parsers.parse_xilinx_spartan import parse_xilinx_spartan
from parsers.parse_xilinx_spartan_six import parse_xilinx_spartan_six
from parsers.parse_xilinx_virtex_five import parse_xilinx_virtex_five
from parsers.parse_xilinx_virtex_four import parse_xilinx_virtex_four
from parsers.parse_xilinx_virtex_six import parse_xilinx_virtex_six
from parsers.xilinx_ultrascale_plus import parse_kintex_ultrascale_plus
from parsers.xilinx_ultrascale import parse_kintex_ultrascale

PARSE_TABLE = {
    'parse_kintex_ultrascale': parse_kintex_ultrascale,
    'parse_kintex_ultrascale_plus': parse_kintex_ultrascale_plus,
    'parse_xilinx_spartan': parse_xilinx_spartan,
    'parse_xilinx_spartan_six': parse_xilinx_spartan_six,
    'parse_xilinx_virtex_five': parse_xilinx_virtex_five,
    'parse_xilinx_virtex_four': parse_xilinx_virtex_four,
    'parse_xilinx_virtex_six': parse_xilinx_virtex_six
}
