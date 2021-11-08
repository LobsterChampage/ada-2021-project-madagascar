# Timings

This is to give some indication on how long the handling of data part takes.

The times will vary on many factors. Most operations are single threaded, but can then be parallized on different sets.

It seems like a key factor for speed is just core clock speed.

It seems chunksizes doesn't matter. Some speeds may vary a lot depending on wether the laptop than ran the test was plugged in or ran on battery.

Some tests were done in parallell which also decreased speeds.

## Crossvalidation of chunksize

##### 2020

| Chunksize | Chunks | Time   | Size  |
| --------- | ------ | ------ | ----- |
| 1000000   | 6      | 796.1s | 786MB |
| 400000    | 14     | 603.2s | 786MB |
| 200000    | 27     | 626.7s | 786MB |
| 100000    | 53     | 602.9s | 786MB |

## Chunking timings

| Year | Chunksize | Chunks | Time   | Size   |
| ---- | --------- | ------ | ------ | ------ |
| 2015 | 200000    | ?      | ~2500s | ?GB    |
| 2016 | 200000    | ?      | ~2100s | ?GB    |
| 2017 | 200000    | 134    | ~4900s | 4.81GB |
| 2018 | 200000    | ?      | ~4000s | ?GB    |
| 2019 | 200000    | ?      | ~3200s | ?GB    |

## Crossvalidaton of calling for elon quotes on different chunksizes

##### 2020

| Chunksize | Time   | Quotes |
| --------- | ------ | ------ |
| 1000000   | 404.8s | 1822   |
| 400000    | 384.1s | 1822   |
| 200000    | 164s   | 1822   |
| 100000    | 340.6s | 1822   |

## Calling for elon quotes timings

| Year | Chunksize | Time    | Quotes       |
| ---- | --------- | ------- | ------------ |
| 2017 | 200000    | 1354.9s | didn't check |
| 2016 | 200000    | 748.9s  | didn't check |
| 2016 | 200000    | 496.2s  | 4568         |
| 2019 | 200000    | 885.8s  | 8533         |
| 2015 | 200000    | 884.6s  | 5282         |
| 2018 | 200000    | 1318.3s | 14183        |
| 2017 | 200000    | 1385.1s | 9213         |

## Calling organizations on elon_quotes with spacy 'lg'

##### 2020

| Time  | Quotes |
| ----- | ------ |
| 19.6s | 485    |
| 15.2s | 485    |
| 15.1s | 485    |

##### 2016

| Time  | Quotes |
| ----- | ------ |
| 38.2s | 916    |

##### 2015-2020

| Time   | Quotes |
| ------ | ------ |
| 368.2s | 10257  |
