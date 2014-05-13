#! /usr/bin/env bash

error_message="error: pass the directory created by the web_brother.sh tools that contains list and files"

if [ "${WEBBROTHER_WORKSPACE}" != '' ]
then
	WORKSPACE="${WEBBROTHER_WORKSPACE}"
else
	WORKSPACE="$(cd "$(dirname $0)"; pwd)/../material/"
fi

! [ -d "${WORKSPACE}" ] && echo "${error_message}" && exit 1

archives_list="${WORKSPACE}/lists/printers_archives_with_licenses.txt"

! [ -f "${archives_list}" ] && echo "${error_message}" && exit 1

cat "${WORKSPACE}/lists/printers_files_with_metadata.txt" | cut -c 1-32 | sort | uniq | while read file_sum
do
	grep "^${file_sum}" "${WORKSPACE}/lists/printers_files_with_metadata.txt" | sort -k 3 | tee "${WORKSPACE}/lists/printers_unique_files_with_metadata.txt"
done

#EOF