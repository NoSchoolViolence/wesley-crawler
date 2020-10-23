CHROME_PATH='/usr/local/bin/chromedriver'
# DRIVER_NAME_CHROME='./chromedriver'
DRIVER_NAME_CHROME='chromedriver'

MOZILLA_PATH='/usr/local/bin/geckodriver'
DRIVER_NAME_MOZILLA='./geckodriver'

DRIVER_NAME=DRIVER_NAME_CHROME
PATH =CHROME_PATH

SEARCH_TOPIC='school+violence'
SEARCH_TOPIC_LIST={'school+violence','school+shooter','student+violence','teacher+violence+school'}
BASE_WEB='https://www.google.com'
MAX_PAGE=1
MAX_ITEM=20

NUMBER_OF_RESULTS_PER_PAGE=5
PAUSE_BTW_REQUEST=0.5

#1 = save as csv, 0=do not save
SAVE_AS_CSV=1