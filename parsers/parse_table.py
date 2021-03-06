from parsers.altera.arria_ten import parse_altera_arria_ten
from parsers.altera.arria_gx import parse_altera_arria_gx
from parsers.altera.arria_ii_gx import parse_altera_arria_ii_gx
from parsers.altera.arria_v import parse_altera_arria_v
from parsers.altera.cyclone import parse_altera_cyclone
from parsers.altera.cyclone_ii import parse_altera_cyclone_ii
from parsers.altera.cyclone_iii import parse_altera_cyclone_iii
from parsers.altera.cyclone_ten import parse_altera_cyclone_ten
from parsers.xilinx.spartan import parse_xilinx_spartan
from parsers.xilinx.spartan_six import parse_xilinx_spartan_six
from parsers.xilinx.virtex_five import parse_xilinx_virtex_five
from parsers.xilinx.virtex_four import parse_xilinx_virtex_four
from parsers.xilinx.virtex_six import parse_xilinx_virtex_six
from parsers.xilinx.ultrascale_plus import parse_kintex_ultrascale_plus
from parsers.xilinx.ultrascale import parse_kintex_ultrascale


def null(*args):
    return []


PARSE_TABLE = {
    'parse_altera_arria_ten': parse_altera_arria_ten,
    'parse_altera_arria_gx': parse_altera_arria_gx,
    'parse_altera_arria_ii_gx': parse_altera_arria_ii_gx,
    'parse_altera_arria_v': parse_altera_arria_v,
    'parse_altera_cyclone': parse_altera_cyclone,
    'parse_altera_cyclone_ii': parse_altera_cyclone_ii,
    'parse_altera_cyclone_iii': parse_altera_cyclone_iii,
    'parse_altera_cyclone_ten': parse_altera_cyclone_ten,
    'parse_kintex_ultrascale': parse_kintex_ultrascale,
    'parse_kintex_ultrascale_plus': parse_kintex_ultrascale_plus,
    'parse_xilinx_spartan': parse_xilinx_spartan,
    'parse_xilinx_spartan_six': parse_xilinx_spartan_six,
    'parse_xilinx_virtex_five': parse_xilinx_virtex_five,
    'parse_xilinx_virtex_four': parse_xilinx_virtex_four,
    'parse_xilinx_virtex_six': parse_xilinx_virtex_six,
    'null': null
}
