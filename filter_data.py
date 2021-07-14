from data_filtering_db import DATA


def run():
    all_python_devs = [worker["name"]
                       for worker in DATA if worker["language"] == 'python']

    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults_name = list(map(lambda worker: worker['name'], adults))
    old_people = list(map(lambda worker: worker | {
                      "old": worker['age'] > 50}, DATA))

    print(all_python_devs)
    print(adults_name)

    for people in old_people:
        print(people)


if __name__ == '__main__':
    run()
