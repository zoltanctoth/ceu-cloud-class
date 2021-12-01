## SUBJECT DATE
DATE_PARAM="2021-10-02"

date <- as.Date(DATE_PARAM, "%Y-%m-%d")

# install.packages('httr', 'jsonlite', 'lubridate')
library(httr)
library(aws.s3)
library(jsonlite)
library(lubridate)

# See https://wikimedia.org/api/rest_v1/#/Edited%20pages%20data/get_metrics_edited_pages_top_by_edits__project___editor_type___page_type___year___month___day_
url <- paste(
  "https://wikimedia.org/api/rest_v1/metrics/edited-pages/top-by-edits/en.wikipedia/user/content/",
  format(date, "%Y/%m/%d"), sep='')

wiki.server.response = GET(url)
wiki.response.status = status_code(wiki.server.response)
print(paste('Wikipedia API Response: ', wiki.response.status, sep=''))

wiki.response.body = content(wiki.server.response, 'text')

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
# Save `wiki.response.body` to the local filesystem into the folder defined 
# in variable `RAW_LOCATION_BASE` under the name `raw-edits-YYYY-MM-DD.txt`,
# i.e: `data/raw-edits/raw-edits-2021-10-01.txt`.




########
# LAB  #
########
#
# Upload the file you created to S3.
#
# * Upload the file you created to your bucket (you can reuse your bucket from 
#   the previous classes or create a new bucket. Both solutions work.) 
# * Place the file on S3 into your bucket under the folder called `datalake/raw/`.
# * Don't change the file's name when you are uploading to S3, keep it at `raw-edits-YYYY-MM-DD.txt`
# * Once you uploaded the file, verify that it's there (list the bucket in R, in the CLI or on the Web)


# BUCKET="{your bucket name}"
#
# {{ FILL IN AWS SETUP STEPS (you might need to copy your accessKey.csv to the working directory) }}
#

## Upload the file
# put_object(file = "{{ ADD LOCAL FILE PATH }}",
#            object = "{{ ADD FOLDER AND FILE NAME HERE in a form of FOLDER/FILE_NAME }}",
#            bucket = BUCKET,
#            verbose = TRUE)




## Parse the response and write the parsed string to "Bronze"

# We are extracting the top edits from the server's response
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
