def in_thematic_area(phd_title: str) -> bool:
    area_keywords = ["information retrieval", "information extraction", "search engine",
                     "information overload", "text retrieval", "digital libraries",
                     "information seeking", "retrieval method", "web search",
                     "retrieval systems", "ir system", "ir model"]

    return any(keyword in phd_title for keyword in area_keywords)


def parse_xml(file_path: str) -> list:
    try:
        r_file_handler = open(file_path, "r")
    except FileNotFoundError as e:
        print(f"Error opening the r_file_handler: {e}")
        exit(-1)
    else:
        year_counts = dict()
        phd_valid = False
        title_tag = "<title>", "</title>"
        year_tag = "<year>", "</year>"

        for line in r_file_handler:
            if any(tag in line for tag in title_tag):
                phd_valid = in_thematic_area(line.lower())
            elif phd_valid and any(tag in line for tag in year_tag):
                year = line[6:10] + "-12-31"
                year_counts[year] = year_counts.get(year, 0) + 1
                phd_valid = False

        year_counts = sorted(year_counts.items())

        w_file_handler = open("output.txt", "w")
        publications_cnt = 0
        for publications in year_counts:
            w_file_handler.write(f"{publications[0]}\t{publications[1]}\n")
            publications_cnt += publications[1]
        print(f"Total titles found in r_file_handler: {str(publications_cnt)}")

        r_file_handler.close()
        w_file_handler.close()

        return year_counts


parse_xml("./input/dblp-2021-02-01.xml")
