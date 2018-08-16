#!/usr/bin/env python3
from collections import namedtuple
import sqlite3
import gzip
import json
import csv
import sys

JAPANESE_DATABASE = "Japanese4.db"
Word = namedtuple('Word', ['Entry', 'Furigana', 'Summary'])

def get_entry_ids(filename):
    entry_ids = []
    with gzip.open(filename, 'rb') as f:
        cards = json.loads(f.read().decode("utf-8"))
        for l in cards['lists']:
            for e in l['entries']:
                entry_ids.append(e['ref'])
    return entry_ids

def get_words(entry_ids):
    conn = sqlite3.connect(JAPANESE_DATABASE)
    c = conn.cursor()
    words = []
    for entry_id in entry_ids:
        q = c.execute('SELECT Entry, Furigana, Summary from entries WHERE _id = ?', [entry_id])
        result = q.fetchone()
        if result is None:
            continue
        words.append(Word(*result))
    return words

def write_csv(words, filename):
    with open(filename, 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for word in words:
            writer.writerow([word.Entry, word.Furigana, word.Summary])
    print("Wrote {} words to {}".format(len(words), filename))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <wordlist.jpl> <output.csv>".format(sys.argv[0]))
        exit(-1)

    entry_ids = get_entry_ids(sys.argv[1])
    words = get_words(entry_ids)
    write_csv(words, sys.argv[2])
