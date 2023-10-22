import sys
import struct

def extract_files(packed_file, output_directory):
    with open(packed_file, 'rb') as pak_file:
        # Leitura do deslocamento da lista a partir do final do arquivo
        pak_file.seek(-struct.calcsize('Q'), 2)
        list_offset = struct.unpack('Q', pak_file.read(struct.calcsize('Q')))[0]

        # Lê a lista de arquivos a partir do deslocamento
        pak_file.seek(list_offset)
        list_data = pak_file.read()
        list_entries = list_data.decode('utf-8').split('\n')

        for entry in list_entries:
            if entry:
                
                entrys=entry.split(',')
                if len(entrys)>1:
                    file_name=entrys[0]
                    start_offset=entrys[1]
                    start_offset = int(start_offset)

                    # Lê o conteúdo do arquivo do pacote
                    pak_file.seek(start_offset)
                    file_data = pak_file.read()

                    # Escreve o arquivo descompactado
                    with open(f"{output_directory}/{file_name}", 'wb') as output_file:
                        output_file.write(file_data)

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")
    if len(sys.argv) != 3:
        print("Uso: python extract_files.py <packed_file> <output_directory>")
    else:
        packed_file = sys.argv[1]  # Arquivo empacotado (out.pak)
        output_directory = sys.argv[2]  # Diretório de saída para os arquivos descompactados
        extract_files(packed_file, output_directory)

