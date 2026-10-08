#2
def clean_notice(text):
    return " ".join(text.split())
#3
def has_bug(text):
    if "bug" in text.casefold():
       return True
    return False
#4
def valid_nickname(text):
    if len(text)<4 or len(text)>12:
        return False
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    allowed= letters + "1234567890" + "_"
    if text[0] not in letters:
        return False
    for char in text[1:]:
        if char not in allowed:
            return False
    return True
#5
def preview(text, limit):
    cleaned = " ".join(text.split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit-3] + "..."
#6
def parse_event(line):
    parts = line.split(";")
    if len(parts) != 3:
        return None
    group=parts[0].strip().upper()
    status=parts[1].strip().upper()
    message=parts[2].strip()
    if group != "Т118" and group != "Т119":
        return None
    if status != "PASS" and status != "FAIL":
        return None
    if message == "":
        return None
    return [group, status, message]
#7
events = [
 "Т118;PASS;Вход работает",
 " т118 ; fail ; Ошибка входа ",
 "Т119;FAIL;Не открывается профиль",
 "Т118;FAIL;Ошибка входа",
 "Т118;FAIL;",
 "не запись"
]
def failures(lines, group):
    group = group.upper().strip()
    if group != "Т118" and group != "Т119":
        return []
    result = []
    for line in lines:
        event = parse_event(line)
        if event is None:
            continue
        if event[0] == group and event[1] == "FAIL":
            result.append(event[2])
    return result
print("№2")
print(clean_notice(" EKEB ждёт Т118! "))
print(clean_notice("Алматы\nАстана\tТараз"))
print(clean_notice(" "))
print("№3")
print(has_bug("BUG найден"))
print(has_bug("Найден bug"))
print(has_bug("DEBUG"))
print(has_bug("Всё работает"))
print(has_bug(""))
print("№4")
print(valid_nickname("Aruzhan_7"))
print(valid_nickname("A123"))
print(valid_nickname("Abcdefghijkl"))
print(valid_nickname("A12"))
print(valid_nickname("Abcdefghijklm"))
print(valid_nickname("7Aruzhan"))
print(valid_nickname("Айдана"))
print(valid_nickname(" user"))
print(valid_nickname(""))
print("№5")
print(preview("EKEB приглашает", 10) )
print(preview(" EKEB ", 4))
print(preview("Алматы", 3))
print(preview(" ", 3))
print(preview("ABC", 3))
print("№6")
print(parse_event(" т118 ; fail ; Ошибка входа "))
print(parse_event("Т119;PASS;Проверка завершена"))
print(parse_event("T118;PASS;ОК"))
print(parse_event("Т118;WAIT;ОК"))
print(parse_event("Т118;FAIL; "))
print(parse_event("Т118;FAIL"))
print(parse_event("Т118;FAIL;а;б"))
print("№7")
print(failures(events, " т118 "))
print(failures(events, "Т119"))
print(failures(events, "Т300"))
print(failures([], "T118"))