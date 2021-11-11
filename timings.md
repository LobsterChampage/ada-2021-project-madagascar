# Timings

This is to give some indication on how much time is used on loading the data.

The times will vary on many factors. Most operations are single threaded, but can then be parallized on different sets.

It seems like a key factor for speed is just core clock speed on the CPU.

It seems chunksizes doesn't matter unless they are big which might be due to memory bottlenecks with the computer that tested.

Some speeds may vary a lot depending on whether the laptop than ran the test was plugged in or ran on battery. Some tests were done in parallell which also decreased speeds so the numbers are not comparable, this is just for reference/indication.

## Crossvalidation of chunksize

##### 2020

| Chunksize | Chunks | Time   | Size  |
| --------- | ------ | ------ | ----- |
| 1000000   | 6      | 796.1s | 786MB |
| 1000000   | 6      | 710.7s | 786MB |
| 1000000   | 6      | 683.6s | 786MB |
| 400000    | 14     | 603.2s | 786MB |
| 200000    | 27     | 626.7s | 786MB |
| 100000    | 53     | 602.9s | 786MB |

## Crossvalidaton of calling for elon quotes on different chunksizes

##### 2020

| Chunksize | Time   | Quotes |
| --------- | ------ | ------ |
| 1000000   | 404.8s | 1822   |
| 400000    | 384.1s | 1822   |
| 200000    | 164s   | 1822   |
| 100000    | 340.6s | 1822   |

## Chunking timings

| Year | Chunksize | Chunks | Time   | Size   |
| ---- | --------- | ------ | ------ | ------ |
| 2015 | 200000    | 105    | ~2500s | 3.09GB |
| 2016 | 200000    | 70     | ~2100s | 2.15GB |
| 2017 | 200000    | 134    | ~4900s | 4.81GB |
| 2018 | 200000    | 137    | ~4000s | 4.44GB |
| 2019 | 200000    | 109    | ~3200s | 3.29GB |

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

## Cutoff table

lg

| cutoff | pre_quotes | time   | org_quotes |
| ------ | ---------- | ------ | ---------- |
| 0.95   | 1741       | 15.1s  | 339        |
| 0.9    | 8292       | 59.3s  | 1550       |
| 0.85   | 15450      | 104.2s | 2853       |
| 0.8    | 21577      | 144.2s | 4001       |
| 0.7    | 30880      | 206.0s | 5834       |
| 0      | 43601      | 293.7s | 8739       |

md

| cutoff | pre_quotes | time   | org_quotes |
| ------ | ---------- | ------ | ---------- |
| 0.95   | 1741       | 15.6s  | 367        |
| 0.85   | 15450      | 105.7s | 3176       |
| 0.7    | 30880      | 204.3s | 6538       |
| 0      | 43601      | 294.7s | 9757       |

sm

| cutoff | pre_quotes | time   | org_quotes |
| ------ | ---------- | ------ | ---------- |
| 0.85   | 15450      | 95.3s  | 2425       |
| 0.7    | 30880      | 188.8s | 4973       |
| 0      | 43601      | 271.8s | 7376       |
