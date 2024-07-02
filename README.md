# Split PDF by Page Numbers

This Python script splits a PDF file based on page numbers specified in a TXT file. It uses PyPDF2 library to extract and create new PDF files for each specified page range.

### Requirements

- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)

### Installation

1. Clone or download this repository.
2. Install PyPDF2 library using pip:

```
pip install PyPDF2
```

### Usage

1. Place your PDF file and TXT file in the same directory as `splitpdfbytxt.py`.
2. Modify the TXT file to specify filename and page ranges in the format: `filename,pagenumber`.
3. Run the script using command prompt or terminal:

```
py splitpdfbytxt.py
```

4. The script will create separate PDF files based on the specifications in the TXT file.

``` name.txt
file1,1
file2,2
file3,3
```
---

สคริปต์ Python นี้ใช้สำหรับแยกไฟล์ PDF ตามหมายเลขหน้าที่ระบุในไฟล์ข้อความ (TXT) โดยใช้งานไลบรารี PyPDF2 เพื่อสร้างไฟล์ PDF ใหม่สำหรับแต่ละช่วงหน้าที่ระบุ.

### ความต้องการ

- Python 3.x
- ไลบรารี PyPDF2 (`pip install PyPDF2`)

### วิธีการติดตั้ง

1. คลอนหรือดาวน์โหลด repository นี้.
2. ติดตั้งไลบรารี PyPDF2 โดยใช้คำสั่ง pip:
   
```
pip install PyPDF2
```

### การใช้งาน

1. วางไฟล์ PDF และไฟล์ TXT ในโฟลเดอร์เดียวกันกับ `splitpdfbytxt.py`.
2. แก้ไขไฟล์ TXT เพื่อระบุชื่อไฟล์และช่วงหน้าที่ต้องการในรูปแบบ: `ชื่อไฟล์,หมายเลขหน้า`.
3. รันสคริปต์ผ่าน command prompt หรือ terminal:

```
py splitpdfbytxt.py
```

4. สคริปต์จะสร้างไฟล์ PDF แยกตามที่ระบุในไฟล์ TXT.
   
``` name.txt
file1,1
file2,2
file3,3
```
