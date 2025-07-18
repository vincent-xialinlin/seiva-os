# cli/seiva_run.py

import sys
from core.kernel import run_seiva_kernel

def main():
    print("🌐 SEIVA OS 启动中... [Structured Explicit-Language Intelligence via Architecture]")
    lang = "auto"
    if len(sys.argv) > 1:
        if sys.argv[1] == "--lang":
            lang = sys.argv[2]
    run_seiva_kernel(lang)

if __name__ == "__main__":
    main()
