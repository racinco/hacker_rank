if __name__ == '__main__':
    main_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        main_list.append([name, score])

    # create a set of all scores
    all_scores = set([list[1] for list in main_list])
    second_lowest = sorted(all_scores)[1]
    get_all_second_lowest = [list for list in main_list if list[1] == second_lowest]

    sort_by_name = sorted(get_all_second_lowest, key = lambda list: list[0])

    for name in sort_by_name:
        print(name[0])

        



