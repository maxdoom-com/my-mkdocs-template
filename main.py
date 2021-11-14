# hint: you can get a lot of macro informations in your docs using:
#   {{ macros_info() }}


def define_env(env):

    # ==================================================================
    @env.macro
    def lorem():
        return """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

    # ==================================================================
    @env.macro
    def csv2table(filename, dialect="excel"):
        """
        convert a csv file living relative to the current document
        to a html table
        """

        import csv

        abs_filename = "/".join(env.page.file.abs_src_path.split("/")[0:-1] + [filename])
        
        header = None
        lines = []

        with open(abs_filename, newline="") as csv_file:
            my_reader = csv.reader(csv_file, dialect=dialect)
            for row in my_reader:
                if not header:
                    header = row
                else:
                    lines.append(row)

        header_html = "".join(f"<th>{s}</th>" for s in header)
        lines_html = ""
        for line in lines:
            lines_html += "<tr>" + "".join(f"<td>{s.strip()}</td>" for s in line) + "</tr>"

        return f"<table><thead><tr>{header_html}</tr></thead><tbody>{lines_html}</tbody></table>"

    # ==================================================================
