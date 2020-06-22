import pandas as pd


# Series una dimensión 
series_test = pd.Series([100, 200, 300])
series_test2 = pd.Series({1999:28, 2000:65, 2001: 39})

print(series_test)
print(series_test2)

# DataFrames, nos da la abstracción de una Tabla
frame_test = pd.DataFrame({1999: [74, 38, 39],
                            2000: [34, 32, 32],
                            2001: [23, 39, 23]})

print(frame_test)

frame_test2 = pd.DataFrame([[74, 38, 39],
                           [34, 32, 32],
                           [23, 39, 23]],
                            columns = [1999, 2000, 2001])

print(frame_test2)


# Read DataSet
el_universal = pd.read_csv('/Users/gonzaloferrando/Documents/Platzi/Cursos/Python/Ejemplos/web_scrapper_curso_eng/eluniversal_2020_06_12_articles.csv')

print(type(el_universal))
print(el_universal)