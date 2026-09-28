def sum_numbers_in_text(text):
    clean_text = ""
    sum = 0
    for word in text:
        if word.isdigit():
            clean_text += word
        else:
            clean_text += " "
    for num in clean_text.split():
        sum += int(num)
    return sum

print(sum_numbers_in_text("I ran 14 km and then 3 km"))

scores = {'Alice':85, 'Bob':90, 'Charlie':78}
for key,value in scores.items():
    print(f'{key} is {value}')
