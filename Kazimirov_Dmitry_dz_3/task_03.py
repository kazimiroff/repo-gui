#3
def thesaurus(*names):
    list_name = [*names]
    dictionary = {}
    for name in list_name:
        name.capitalize()
        lett = name[0]
        dict_1 = {lett : name}
        dictionary.update(dict_1)



    return dictionary

print(thesaurus("Андрей", "Антон", "Борис", "Виктор"))

#не получилось добить до конца, создаётся только по одному имени к букве,
# имена на одну букву не отрабатываются корректно