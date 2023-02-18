import statistics

grades = [85, 93, 45, 89, 85]

print(f'Середнє значення, раховане ручним методом: {sum(grades)/len(grades)}')

print(f'Середнє значення, раховане за допомогою модуля statistics:{statistics.mean(grades)}')

print(f'Медіана, рахована за допомогою модуля statistics:{statistics.median(grades)}')

print(f'Мода, рахована за допомогою модуля statistics:{statistics.mode(grades)}')