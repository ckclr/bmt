from pathlib import Path

# from tkinter import messagebox
from utils import mark_yaml

import sys
import win32com.client
import yaml


def open_file_in_devenv(filename, line):
    dte = win32com.client.GetActiveObject("VisualStudio.DTE")
    dte.MainWindow.Activate
    dte.ItemOperations.OpenFile(filename)
    dte.ActiveDocument.Selection.MoveToLineAndOffset(line, 1)


def main():
    prj_dir = Path(sys.argv[1]).parent
    mark_id = int(sys.argv[2])
    cfg_pth = prj_dir / "config.yaml"
    with open(cfg_pth, mode="r", encoding="utf-8") as cfg_file:
        prj_cfg = yaml.load(cfg_file, Loader=yaml.Loader)
    hexsha = prj_cfg["SHA"]
    # messagebox.showinfo("hello-bmt", f"{prj_dir}\n{hexsha}\n{mark_id}")
    with open(prj_dir / hexsha / mark_yaml, mode="r", encoding="utf-8") as table_file:
        mark_table = yaml.load(table_file, Loader=yaml.Loader)
        mark_pos = mark_table[mark_id].split(",")
        open_file_in_devenv(mark_pos[0], mark_pos[1])


if __name__ == "__main__":
    main()
