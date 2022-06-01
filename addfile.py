import argparse
import csv
import shutil
import sys
import os

# la funzione directories_check l'avevo già inserita all'interno del fileorganizer, ho 
# deciso di inserirla anche qui nel caso in cui addfile venga usato prima
def directories_check(path):
	subfolders = ["audio", "docs", "images"]
	for folder in subfolders:
		os.makedirs(os.path.join(path, folder), exist_ok=True)

# definisco una funzione per controllare che sia stato inserito solo un nome dopo quello
# dello script e che il nome sia dotato di un'estensione
def argument_check():
    parser = argparse.ArgumentParser(description = "Move the specified file into the appropriate folder")
    parser.add_argument("filename", help = "the name of the file you want to move (with the extension)")
    args = parser.parse_args()
    filename = args.filename
    name, extension = os.path.splitext(filename)
    # volevo fare in modo che ogni errore fosse segnalato correttamente, quindi ho aggiunto un if
    # statement per avvisare l'utente nel caso in cui scriva il nome del file senza estensione
    if not extension:
        print("The filename needs to be written with the extension")
        sys.exit()

# la funzione è identica a file_handling di fileorganizer, l'unica differenza è l'aggiunta
# di una funzione print al termine di ogni spostamento in modo che ci sia conferma visiva
# per l'utente che il file è stato trasferito con successo all'interno della sua cartella
def file_handling(path, file, files_list):
    images_ext = [".png", ".jpg", ".jpeg"]
    audio_ext = [".mp3"]
    docs_ext = [".txt", ".odt"]
    with open(os.path.join(path,"recap.csv"), "a", newline ='') as csv_file:
        writer = csv.writer(csv_file)
        if not "recap.csv" in files_list:
            writer.writerow(["Filename","Type","Size(B)"])
        fileName, fileExtension = os.path.splitext(file)
        fileSize = os.path.getsize(os.path.join(path,file))
        if fileExtension in images_ext:
            writer.writerow([fileName, "image", fileSize])
            img_path = os.path.join(path,"images")
            shutil.move(os.path.join(path,file), img_path)
            print(f""""{file}" successfully moved to "{img_path}" """)
        elif fileExtension in audio_ext:
            writer.writerow([fileName, "audio", fileSize])
            audio_path = os.path.join(path,"audio")
            shutil.move(os.path.join(path,file), audio_path)
            print(f""""{file}" successfully moved to "{audio_path}" """)
        elif fileExtension in docs_ext:
            writer.writerow([fileName, "docs", fileSize])
            docs_path = os.path.join(path,"docs")
            shutil.move(os.path.join(path,file), docs_path)
            print(f""""{file}" successfully moved to "{docs_path}" """)

# ho creato la funzione main perché essendo un eseguibile ho utilizzato l'if statement successivo
# per assicurarmi che il programma sia eseguito solo se chiamato tramite shell e non nel caso in cui
# dovesse essere importato come modulo
def main():
    argument_check()
    path = r"./files"
    files_list = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name))]
    directories_check(path)
    file = sys.argv[1]
    # controllo se il file è presente all'interno della cartella ed in caso opposto stampo un
    # messaggio opportuno
    if file in files_list:
        file_handling(path, file, files_list)
    else:
        print(f"""File "{file}" not found inside path "{path}" """)
        
main()
