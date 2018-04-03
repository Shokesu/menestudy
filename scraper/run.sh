#!/usr/bin/env bash
rm -f data.json
scrapy crawl main -o data.json