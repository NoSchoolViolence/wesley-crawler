#APPLICATION MODE {for now}
APP_MODE_SEARCH=1
APP_MODE_CRAWL_ALL=2
APP_MODE_CRAWL_WE_CONTENT=2
APP_MODE_CRAWL_FILES=3
APP_MODE_CLEAN_CONTENT=4
APP_MODE_CSF=4
APP_MODE=APP_MODE_CSF
# DEFINE Cloud File Store Vendor
APP_CSF_ACTIVE=1
APP_CSF_VENDOR_BOX=1
APP_CSF_VENDOR_AWSS3=2
APP_CSF_VENDOR_GDRIVE=3
APP_CSF_VENDOR=APP_CSF_VENDOR_BOX

#Dummy search keyword..
SEARCH_TOPIC='school+violence'
# {query1, query2,.....,queryN}
SEARCH_TOPIC_LIST={'school+violence','school+shooter','student+violence','teacher+violence+school'}
BASE_WEB='https://www.google.com'


# MAX_PAGE=1 fetch result only from 1st page.
MAX_PAGE=1
# MAX_ITEM = Fetch at most MAX_ITEM for each query search.
MAX_ITEM=20

#Fetch NUMBER_OF_RESULTS_PER_PAGE result from each page.
NUMBER_OF_RESULTS_PER_PAGE=5
#0.5 second.
PAUSE_BTW_REQUEST=0.5
# 10 seconds
TIMEOUT_TO_GET_WEB_CONTENT=10

#1 = save as csv, 0=do not save
SAVE_AS_CSV=1
SAVE_AS_JSON=1
REMOVE_TMP_DIR=1
