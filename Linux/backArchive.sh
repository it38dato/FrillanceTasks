#!/bin/bash
#Бэкап архив всех файлов.
BACKUPFILE=backup
archive=${1:-$BACKUPFILE}
find . -mtime -1 -type f -print0 | xargs -0 tar rvf "$archive.tar"
echo "Каталог $PWD заархивирован в файл \"$archive.tar\"."
exit 0