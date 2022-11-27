## SUBJECT DATE
DATE_PARAM="2022-10-28"

date <- as.Date(DATE_PARAM, "%Y-%m-%d")

install.packages('httr')
install.packages('jsonlite', 'lubridate')
install.packages('testit')

library(httr)
library(aws.s3)
library(jsonlite)
library(lubridate)
library(testit)

# See https://wikimedia.org/api/rest_v1/#/Edited%20pages%20data/get_metrics_edited_pages_top_by_edits__project___editor_type___page_type___year___month___day_
url <- paste(
  "https://wikimedia.org/api/rest_v1/metrics/edited-pages/top-by-edits/en.wikipedia/user/content/",
  format(date, "%Y/%m/%d"), sep='')

print(paste('Requesting REST API URL: ', url, sep=''))
wiki.server.response = GET(url)

wiki.response.status = status_code(wiki.server.response)
wiki.response.body = content(wiki.server.response, 'text')

print(paste('Wikipedia REST API Response body: ', wiki.response.body, sep=''))
print(paste('Wikipedia REST API Response Code: ', wiki.response.status, sep=''))

if (wiki.response.status != 200){
  print(paste("Recieved non-OK status code from Wiki Server: ",
              wiki.response.status,
              '. Response body: ',
              wiki.response.body, sep=''
  ))
}

# Save Raw Response and upload to S3
RAW_LOCATION_BASE='data/raw-edits'
dir.create(file.path(RAW_LOCATION_BASE), showWarnings = TRUE, recursive = TRUE)

########
# LAB  #
########
#
# Save the contents of `wiki.response.body` to file called `raw-edits-YYYY-MM-DD.txt` into the folder
#in variable `RAW_LOCATION_BASE` defined 
# i.e: `data/raw-edits/raw-edits-2021-10-01.txt`.

## END OF LAB

########
# LAB  #
########
#
# Upload the file you created to S3.
#
# * Upload the file you created to your bucket (you can reuse your bucket from 
#   the previous classes or create a new bucket. Both solutions work.) 
# * Place the file on S3 into your bucket under a folder called `datalake/raw/`.
# * Don't change the file's name when you are uploading to S3, keep it at `raw-edits-YYYY-MM-DD.txt`
# * Once you uploaded the file, verify that it's there (list the bucket in R on the AWS Website)


# BUCKET="{your bucket name}"
#
# {{ FILL IN AWS SETUP STEPS (you might need to copy your accessKey.csv to the working directory) }}
#

## Upload the file
# put_object(file = "{{ ADD LOCAL FILE PATH }}",
#            object = "{{ ADD FOLDER AND FILE NAME HERE in a form of FOLDER/FILE_NAME }}",
#            bucket = BUCKET,
#            verbose = TRUE)


## END OF LAB

## Parse the wikipedia response and write the parsed string to "Bronze"

# First, we are extracting the top edits from the server's response

wiki.response.parsed = content(wiki.server.response, 'parsed')
top.edits = wiki.response.parsed$items[[1]]$results[[1]]$top

# Convert the server's response to JSON lines
current.time = Sys.time() 
json.lines = ""
for (page in top.edits){
  record = list(
    title = page$page_title[[1]],
    edits = page$edits,
    date = format(date, "%Y-%m-%d"),
    retrieved_at = current.time
  )
  
  json.lines = paste(json.lines,
                     toJSON(record,
                            auto_unbox=TRUE),
                     "\n",
                     sep='')
}

# Save the Top Edits JSON lines as a file and upload it to S3

JSON_LOCATION_BASE='data/edits'
dir.create(file.path(JSON_LOCATION_BASE), showWarnings = TRUE)

json.lines.filename = paste("edits-", format(date, "%Y-%m-%d"), '.json',
                            sep='')
json.lines.fullpath = paste(JSON_LOCATION_BASE, '/', 
                            json.lines.filename, sep='')

write(json.lines, file = json.lines.fullpath)

put_object(file = json.lines.fullpath,
           object = paste('datalake/edits/', 
                          json.lines.filename,
                          sep = ""),
           bucket = BUCKET,
           verbose = TRUE)
