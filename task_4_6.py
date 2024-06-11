# -*- coding: utf-8 -*-
"""
Завдання 4.6

Обробити рядок ospf_route та вивести інформацію на стандартний потік виведення у вигляді:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для цього використовувати шаблон template і підставити значення з рядка
ospf_route. Значення рядка ospf_route треба отримати за допомогою Python.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

ospf_route = ospf_route.strip().split(" ")
ospf_route.remove(ospf_route[2])

ospf_route[1] = ospf_route[1][1:6]
ospf_route[2] = ospf_route[2].replace(",", "")
ospf_route[3] = ospf_route[3].replace(",", "")

print(template.format(ospf_route[0], ospf_route[1], ospf_route[2], ospf_route[3], ospf_route[4]))