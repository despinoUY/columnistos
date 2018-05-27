#!/bin/sh
export TESTING='True'
export LOG_FOLDER='./logs/'

cd diarios
scrapy crawl elpais
scrapy crawl ladiaria
#scrapy crawl elobservador
#scrapy crawl larepublica
