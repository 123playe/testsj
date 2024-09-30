# Таблица соответствий символов
encrypt_table = {
    'a': 'yayz', 'b': 'poiu', 'c': 'hgfw', 'd': 'wlal', 'e': 'viqi',
    'f': 'psjvy', 'g': '+276h', 'h': 'usu88', 'i': 'r09yy', 'j': 'qjaq',
    'k': 'shhh', 'l': 'shHwy', 'm': 'aiaii', 'n': 'Yy5@5', 'o': 'YqY884',
    'p': '/#)Hh', 'q': 'QvGw71', 'r': '18hJsj', 's': 'SjjU7', 't': '×hHS:',
    'u': 'IsixBh', 'v': 'Kabdj', 'w': 's32JN26', 'x': '8#7hjn', 'y': 'JY6-&fa',
    'z': 'jcg',
     'а': 'shPwj87', 'б': 'ehj-DH', 'в': 'IapMm', 'г': 'y367h@&', 'д': 'sMml9%',
      'е': 'mļöđѣ', 'ж': 'hYĳ1a@', 'з': 'mĆş65', 'и': 'ys6S0', 'й': '6whhŧ',
       'к': 'sjn!6', 'л': 'ņsÿ9xx', 'м': 'haB61_', 'н': 'êu66þ', 'о': 'PeTsg',
        'п': 'HsbY:66', 'р': 'Hhdũ6', 'с': '1jĥFŝ', 'т': 'ak971', 'у': 'Hsuĥ54',
        'ф': 'su0ŀġ', 'х': 'aĳh', 'ц': 'Gaþ53', 'ч': 'gatĝm', 'ш': 'yaVX6',
         'щ': 'Yaj45P', 'ъ': 'Bato41', 'ы': 'Ja+ß', 'ь': 'MslG+', 'э': 'YaťMķ',
          'ю': ',tBmm43', 'я': 'Ggba642',
          'http': 'http',
}

# Функция для шифрования строки
def encrypt_string(original_string):
    encrypted_string = ''
    
    for char in original_string:
        encrypted_char = encrypt_table.get(char, char)
        encrypted_string += encrypted_char
        
    return encrypted_string

# Оригинальная строка
original_string = "Кто дешифрует тот лох"

# Шифруем строку
encrypted_string = encrypt_string(original_string)
print("Зашифрованная строка:", encrypted_string)
encrypted_string = encrypt_string(original_string)
print("Обычная строка:", original_string)