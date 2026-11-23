"""One-Line Laugh Sprint entry: writes the one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os

LINE = "The washing machine finished an hour ago; now it's holding my clothes hostage until I confess I forgot them."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
