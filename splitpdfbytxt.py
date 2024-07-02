import PyPDF2
import os

def split_pdf_by_pages():
    # หาชื่อไฟล์ PDF และ TXT ในไดเร็กทอรีปัจจุบัน
    current_directory = os.getcwd()
    pdf_files = [file for file in os.listdir(current_directory) if file.endswith('.pdf')]
    txt_files = [file for file in os.listdir(current_directory) if file.endswith('.txt')]

    if not pdf_files or not txt_files:
        print("ไม่พบไฟล์ PDF หรือ TXT ในไดเร็กทอรีปัจจุบัน")
        return

    pdf_file = pdf_files[0]  # เลือกไฟล์ PDF แรกที่พบ
    txt_file = txt_files[0]  # เลือกไฟล์ TXT แรกที่พบ

    # กำหนดชื่อโฟลเดอร์ output เป็นชื่อเดียวกับไฟล์ PDF
    output_folder = os.path.join(current_directory, os.path.splitext(pdf_file)[0])
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) == 2:
                    name, page_number = parts
                    try:
                        page_number = int(page_number) - 1  # แปลงหน้าให้เป็น index (เริ่มจาก 0)
                        
                        pdf_writer = PyPDF2.PdfWriter()
                        pdf_writer.add_page(pdf_reader.pages[page_number])
                        
                        output_file = os.path.join(output_folder, f"{name}.pdf")
                        with open(output_file, 'wb') as output_pdf:
                            pdf_writer.write(output_pdf)
                        
                        print(f"สร้างไฟล์: {output_file}")
                    except (ValueError, IndexError) as e:
                        print(f"ข้อผิดพลาดในการประมวลผลบรรทัด: {line}, ข้อผิดพลาด: {e}")
                else:
                    print(f"รูปแบบข้อมูลไม่ถูกต้องในบรรทัด: {line}")

# เรียกใช้งานฟังก์ชัน
split_pdf_by_pages()
