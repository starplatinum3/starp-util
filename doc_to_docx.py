from win32com import client as wc
 
word = wc.Dispatch("Word.Application")
doc_file_path='D:\\毕设\\毕业设计-starp-考试.doc'
doc = word.Documents.Open(doc_file_path)
docx_type=12
docx_out_path=rf"D:\毕业设计-starp-考试.docx"
doc.SaveAs(docx_out_path, 12) 
# 12为docx
doc.Close()
word.Quit()