trips = ['ермітаж', 'київський зоопарк', 'лувр', 'зоологічний музей']
searching = input ('Запит:')
searching = searching.lower ()
# Допиши програму
if searching in trips:
    print("Є таке")
else:
    print("такого нема")