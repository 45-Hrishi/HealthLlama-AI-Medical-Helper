import multiprocessing
from functools import partial
from pypdf import PdfReader
from langchain.document_loaders import PyPDFLoader

pdf_path = "data/medbook.pdf"
num_workers = multiprocessing.cpu_count() 
print(f"No of workers : {num_workers}")

def extract_text_from_pages(pdf_path, start_page, end_page):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    # print(len(pages))
    extracted_text = ""
    for i in range(start_page, end_page):
        if i < len(pages):
            extracted_text += pages[i].page_content
    return extracted_text

def count_total_pages(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        total_pages = len(reader.pages)
    return total_pages

# Function to divide the workload
def get_extracted_text():
    # Load the PDF to count the total number of pages
    # loader = PyPDFLoader(pdf_path)
    total_pages = count_total_pages(pdf_path)
    print("Total Pages:", total_pages)
    # Determine chunk size for each worker
    chunk_size = total_pages // num_workers

    print("Chunk size : ",chunk_size)
    # Create a pool of workers
    with multiprocessing.Pool(processes=num_workers) as pool:
        # Divide the workload and assign it to workers
        jobs = []
        for i in range(num_workers):
            start_page = i * chunk_size
            end_page = (i + 1) * chunk_size if i < num_workers - 1 else total_pages
            jobs.append(pool.apply_async(extract_text_from_pages, (pdf_path, start_page, end_page)))

        # Collect the results from all workers
        results = [job.get() for job in jobs]
    # Combine the text from all workers
    return results

