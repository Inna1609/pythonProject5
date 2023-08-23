#2 завдання. скористайтесь pytest. напишіть функцію, яка додає в csv один рядок.
# Напишіть функцію, яка видаляє з csv один рядок. напишіть два тести, які перевіряють відповідно чи додався рядок і чи він видалився.
# в якості перевірного csv можете скористатись доданим до завдання файлом або будь-яким іншим.

import csv
import pytest

def add_row(file_path, row):
  with open(file_path, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(row)

def delete_row(file_path, row_number):
  with open(file_path, 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

  rows.remove(rows[row_number])

  with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)


def test_add_row(capsys):
  with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['first row', 'second row', 'third row'])

  add_row('test.csv', ['fourth row', 'fifth row', 'six row'])

  with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

  assert rows == [['first row', 'second row', 'third row'], ['fourth row', 'fifth row', 'six row']]

  captured = capsys.readouterr()
  assert captured.out == ''


def test_delete_row(capsys):
  with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['first row', 'second row', 'third row'])
    writer.writerow(['fourth row', 'fifth row', 'six row'])

  delete_row('test.csv', 1)


  with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

  assert rows == [['first row', 'second row', 'third row']]

  captured = capsys.readouterr()
  assert captured.out == ''