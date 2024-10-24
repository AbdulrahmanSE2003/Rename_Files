import os
folderPath = "D:\\Abdulrahman\\Projects\\Front_End\\firstFullProject\\images\\Gallery"  #Put Your Path Here...
for index, fileName in enumerate(os.listdir(folderPath)):
    oldFilePath = os.path.join(folderPath, fileName)

    newFileName = f"image_{index + 1}{os.path.splitext(fileName)[1]}" #Put The New File Name

    newFilePath = os.path.join(folderPath,newFileName)

    os.rename(oldFilePath , newFilePath)
    
    print(f"Renamed: {fileName} --> {newFileName} \n") #Just For Testing
