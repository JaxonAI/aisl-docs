"""Strip the "Made with Zensical" credit from the footer of a built site.

Zensical renders the credit next to the copyright notice and offers no config
option to turn it off, so we remove it from the generated HTML after
`zensical build`.

Usage: python scripts/remove_zensical_footer.py [SITE_DIR]   (default: site)
"""

import re
import sys
from pathlib import Path

FOOTER_CREDIT = re.compile(
    r"\s*Made with\s*<a\s+href=\"https://zensical\.org/\"[^>]*>\s*Zensical\s*</a>",
)


def main() -> int:
    site_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    if not site_dir.is_dir():
        print(f"error: {site_dir} is not a directory", file=sys.stderr)
        return 1

    changed = 0
    for page in site_dir.rglob("*.html"):
        html = page.read_text(encoding="utf-8")
        stripped, count = FOOTER_CREDIT.subn("", html)
        if count:
            page.write_text(stripped, encoding="utf-8")
            changed += 1

    print(f"Removed Zensical footer credit from {changed} page(s) in {site_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
