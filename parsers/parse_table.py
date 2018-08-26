from parsers.xilinx_ultrascale_plus import parse_kintex_ultrascale_plus
from parsers.xilinx_ultrascale import parse_kintex_ultrascale

PARSE_TABLE = {
    'parse_kintex_ultrascale': parse_kintex_ultrascale,
    'parse_kintex_ultrascale_plus': parse_kintex_ultrascale_plus,
}
