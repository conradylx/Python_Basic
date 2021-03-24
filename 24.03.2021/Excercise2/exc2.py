# Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.

import os

statinfo = os.stat('text.txt')
print(statinfo.st_size)