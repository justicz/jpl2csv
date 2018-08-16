# jpl2csv

This is a Python program to convert the proprietary flashcard list format used in version 4 of the [Japanese app for iOS/Android](https://www.japaneseapp.com/) into a CSV.

The `.jpl` format that the app exports is a gzipped json object containing a list of database ids for the entries. To decode this list you'll need a copy of `Japanese4.db`, which I can't post here on GitHub. You can get this file off of an Android phone from `/data/data/com.renzo.japanese/databases/Japanese4.db` after installing the app.
