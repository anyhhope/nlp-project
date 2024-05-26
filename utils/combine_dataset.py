import os
import tarfile
import lzma

def extract_xz_files(directory, output_file, max_chars=1_000_000_000):
    total_chars = 0
    with open(output_file, 'w', encoding='utf-8') as outfile:
 
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.xz'):
                    file_path = os.path.join(root, file)
                    print(f"Распаковка файла {file_path}")
                    
                    with lzma.open(file_path, 'rb') as f:
                        with tarfile.open(fileobj=f) as tar:
                            for member in tar.getmembers():
                                if member.isfile():
                                    member_file = tar.extractfile(member)
                                    if member_file:
                                        content = member_file.read().decode('utf-8')
                                        content_length = len(content)

                                        if total_chars + content_length > max_chars:
                                            remaining_chars = max_chars - total_chars
                                            outfile.write(content[:remaining_chars])
                                            print(f"Достигнуто ограничение в {max_chars} символов.")
                                            return
                                        else:
                                            outfile.write(content + '\n')
                                            total_chars += content_length

if __name__ == "__main__":
    directory = 'openwebtext' 
    output_file = 'combined_text_mlrd.txt'
    max_chars = 1_000_000_000
    extract_xz_files(directory, output_file, max_chars)
    print("Процесс завершен. Все файлы объединены в", output_file)