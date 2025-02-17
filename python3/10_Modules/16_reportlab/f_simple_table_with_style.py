#!/usr/bin/python3

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def simple_table_with_style():
    doc = SimpleDocTemplate("f_simple_table_with_style.pdf", pagesize=letter)
    flowables = []

    data = [
        ["col_{}".format(x) for x in range(1, 6)],
        [str(x) for x in range(1, 6)],
        ["a", "b", "c", "d", "e"],
    ]

    tblstyle = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.red),
            ("TEXTCOLOR", (0, 1), (-1, 1), colors.blue),
        ]
    )

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    flowables.append(tbl)

    doc.build(flowables)


if __name__ == "__main__":
    simple_table_with_style()
