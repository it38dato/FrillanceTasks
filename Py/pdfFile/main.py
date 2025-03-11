#Работаем с ПДФ файлами. Выведем только первые 5 страниц
# Разработка Парсинг ПДФ файлов.
import fitz # Фитз входит в состав библиотеки PyMuPDF
spisok=list(range(5)) # Список с номерами первых 5 страниц
docu=fitz.open("pdf_file.pdf")
docu.select(spisok) # Удаляются все, кроме 5 страниц
docu.save("pdf_file2.pdf", garbage=3)
docu.close()
"""
import  fitz
stroka_1="ABCD"; stroka_2="EFGH"; stroka_3="IJKL"
new_docu=fitz.open()
new_docu.insertPage(text=stroka_1, fontsize=11)
new_docu.insertPage(text=stroka_2, fontsize=20)
new_docu.insertPage(text=None, fontsize=20)
new_docu.insertPage(text=stroka_3, fontsize=20)
new_docu.save("NewFile.pdf", garbage=3)
new_docu_2=fitz.open("NewFile.pdf")
spisok2=list(range(new_docu_2.pageCount))
for page_number in spisok2:
    if not new_docu.getPageText(page_number):
        spisok2.remove(page_number)
new_docu_2.select(spisok2)
new_docu_2.save("NewFileResult.pdf", garbage=3)
new_docu.close()
new_docu_2.close()
"""