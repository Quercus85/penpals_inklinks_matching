import csv
from random import randrange as rng


def givers_check():
    print("givers_check START")
    for entry in entry_list:
        print("current entry value:", entry)
        if entry["isGiver"] == 'true':
            print(f"{entry['name']}({entry['handle']}) is a giver")
            givers_list.append(entry)

    if len(givers_list) >= 2:
        print("There are two or more givers. Removing from entry_list")
        for g in givers_list:
            if g in entry_list:
                entry_list.remove(g)
    else:
        print("Not enough givers. They will stay in entry_list ")
    print("givers_check STOP")


def pairing_names(*, in_list, not_givers_list):
    print("pairing_names START")
    print("in_list values: ", in_list)
    print(f"Is the entry list? [{not_givers_list}] ")
    if not_givers_list:
        print("cycling entry list...")
    else:
        print("cycling givers list...")
    current_index = 0
    while len(in_list) > 1:
        random_index = rng(0, len(in_list) - 1)
        if current_index >= len(in_list):
            current_index = 0
        if random_index == current_index:
            print("Both index are the same. Skipping...")
            current_index += 1
            continue
        else:
            print("-------------------")
            print(f"Pairing {in_list[current_index]['name']} with {in_list[random_index]['name']}")
            print("-------------------")
            final_output.append(
                f"{in_list[current_index]["name"]} ({in_list[current_index]["handle"]} , {in_list[current_index]["country"]}) "
                f"paired with {in_list[random_index]['name']} ({in_list[random_index]["handle"]} , "
                f"{in_list[random_index]["country"]})")
            # Removing paired entries
            in_list.pop(current_index)
            if random_index > current_index:
                random_index -= 1
            in_list.pop(random_index)
            if current_index >= len(in_list):
                current_index = 0
            else:
                current_index += 1
        if len(in_list) <= 1:
            if len(in_list) == 1:
                if not_givers_list:
                    print("Pushing the left entry in the unmatched list...", in_list[0]["name"])
                    unmatch = f"{in_list[0]["name"]} ({in_list[0]["handle"]} , {in_list[0]["country"]})"
                    unmatched_list.append(unmatch)
                else:
                    print("Pushing the unmatched giver in the entry list...", in_list[0]["name"])
                    entry_list.append(in_list[0])
            break
    print("pairing_names STOP")


if __name__ == '__main__':
    # reminder: only a csv extraction file is handled here
    # path_file = r"C:\Your\Path\Here\filename.csv"
    path_file = r"C:\Users\lucac\Desktop\discordhandles_202409180953.csv"
    final_output = []
    givers_list = []
    unmatched_list = []
    with open(path_file) as f:
        entry_list = [{key: value for key, value in row.items()}
                      for row in csv.DictReader(f, skipinitialspace=True)]
    print("parsed dictionary: ", entry_list)

    # givers get to be paired between them first. If there are two or more
    # they get erased by the entry list, otherwise nothing happens
    givers_check()
    # calling pairing functions. First givers, then everyone else
    pairing_names(in_list=givers_list, not_givers_list=False)
    pairing_names(in_list=entry_list, not_givers_list=True)

    print("Results: ", final_output)
    print("Unmatched entries: ", unmatched_list)
