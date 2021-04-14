def in_thematic_area(phd_title: str) -> bool:
    area_keywords = ["information retrieval", "information extraction", "search engine",
                     "information overload", "text retrieval", "digital libraries",
                     "information seeking", "retrieval method", "web search",
                     "retrieval systems", "ir system", "ir model"]

    return any(keyword in phd_title for keyword in area_keywords)


try:
    file = open("./input/dblp-2021-02-01.xml")
except FileNotFoundError as e:
    print(f"Error opening the file: {e}")
    exit(-1)
else:
    year_counts = dict()
    valid = False

    for line in file:
        if line.startswith("<title>"):
            phd_valid = in_thematic_area(line[7:len(line) - 9].lower())

        if line.startswith("<year>") and phd_valid:
            year = line[6:10]
            year_counts[year] = year_counts.get(year, 0) + 1
            valid = False

    year_counts = dict(sorted(year_counts.items()))

    for k, v in year_counts.items():
        print(f"Key: {k}\tValue: {v}")

    print(f"Total titles found: {sum(year_counts.values())}")







