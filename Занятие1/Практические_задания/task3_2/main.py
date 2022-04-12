BYTES_ONE_CHAR = 1

pages = 100  # ввести количество страниц
lines = 50  # ввести количество строк
chars = 25  # ввести количество символов в строке

total_chars = pages * lines * chars  # общее количество символов в книге
total_bytes = total_chars * BYTES_ONE_CHAR  # размер одной книги в байтах

disk_size = 1.44 * 1024 * 1024 # размер дискеты в байтах

print(disk_size // total_bytes)  # найти количество книг, которое поместится на дискете
