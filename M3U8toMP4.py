import os
default_folder = r'/storage/emulated/0/UCDownloads/video'
default_output = r'/storage/emulated/0/UCDownloads/Output'
folder_path = input("Enter the folder path which contains m3u8 file : ")
output_path = input("Enter the output folder path : ")
print("Processing...")
if not output_path: output_path = default_output
if not folder_path: folder_path = default_folder
m3u8_files = sorted([i for i in os.listdir(folder_path) if i.endswith('.m3u8')])
m3u8_folder = sorted([i for i in os.listdir(folder_path) if i.endswith('.m3u8_contents')])

count = 0

if len(m3u8_files) != len(m3u8_folder):
    print("Some files are Missing, check and try again")
for folder in m3u8_folder:
    #print(folder)
    with open(os.path.join(folder_path,m3u8_files[count]),'r') as m3u8:
        files = m3u8.read()
    files = files.split('file:')[1:]
    files = [x.split('\n')[0].split('/')[-1] for x in files]
    count +=1
    with open(os.path.join(output_path,folder.split(".m3u8_contents")[0])+".mp4",'wb') as output_file:
        for i in files:
            with open(os.path.join(folder_path,folder,str(i)),'rb') as read_file:
                #print(read_file.read())
                output_file.write(read_file.read())  
    print(f"Episode: {folder.split('Episode ')[1][:2]} Converted")
print(f"All Done Total {count} files converted :)")