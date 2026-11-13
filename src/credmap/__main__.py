"""`python -m credmap` runs passkey and says so once."""

import sys

from passkey.cli import main

sys.stderr.write("credmap is now passkey; `credmap` still runs for this release\n")
raise SystemExit(main())
