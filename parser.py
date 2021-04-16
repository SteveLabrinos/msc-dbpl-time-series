import pandas as pd


def in_thematic_area(phd_title: str) -> bool:
    area_keywords = ["information retrieval", "information extraction", "search engine",
                     "information overload", "text retrieval", "digital libraries",
                     "information seeking", "retrieval method", "web search",
                     "retrieval systems", "ir system", "ir model"]

    area_keywords = ["database", "information"]

    return any(keyword in phd_title for keyword in area_keywords)


def parse_xml(file_path: str) -> list:
    try:
        file = open(file_path)
    except FileNotFoundError as e:
        print(f"Error opening the file: {e}")
        exit(-1)
    else:
        year_counts = dict()
        phd_valid = False

        for line in file:
            if line.startswith("<title>"):
                phd_valid = in_thematic_area(line[7:len(line) - 9].lower())

            if line.startswith("<year>") and phd_valid:
                year = line[6:10] + "-12-31"
                year_counts[year] = year_counts.get(year, 0) + 1
                phd_valid = False

        year_counts = sorted(year_counts.items())

        print(f"Total titles found in file: {str(sum([year[1] for year in year_counts]))}")

        return year_counts


test = pd.DataFrame(parse_xml("./input/sample.xml"), columns=["date", "publications"])
#
# test.date = pd.to_datetime(test.date)
# test.set_index("date", inplace=True)
# test = test.asfreq('a')
print(test)







