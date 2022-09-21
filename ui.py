import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from TranslationAPI import *
import threading

class ui():
    def __init__(self, control):
        self.root = control
        self.root.config()
        self.root.title('臉孔畫風突變器')
        self.root.geometry('800x600')
        global canvas
        canvas = tk.Canvas( self.root,
                            width = 800,
                            height = 600,
                            highlightthickness = 0,
                            borderwidth = 0)
        canvas.place(x = 0, y = 0)              
        window(self.root)        
                
class window():
    def __init__(self, control):
        self.control = control
        self.interface = tk.Frame(self.control)
        self.interface.place(x = 0, y = 0)
        self.startPage()

    def startPage(self):
        global image, imageFile, im1, im2, im1_1, im1_2
        global btn1, btn2, label1, label2, type1, type2
        global bgid
        
        image = Image.open('background_2.jpg')
        image = image.resize((800, 600))
        imageFile = ImageTk.PhotoImage(image)
        
        bgid = canvas.create_image(0, 0, image = imageFile, anchor = 'nw')
        
        self.createLabel(1, '臉孔畫風突變器', '#5555FF', 30, 250, 25, 550, 125)
        self.createLabel(2, '請選擇模式:', 'orange', 23, 50, 140, 250, 210)
        
        btn1 = tk.Button(text = '動畫轉真人',
                         bg = '#5500FF', fg = 'white',
                         font = '微軟正黑體 15 bold',
                         command = self.change_to_Page2_1)
        btn1.place(x = 150, y = 250)
        
        btn2 = tk.Button(text = '真人轉動畫',
                         bg = '#5500FF', fg = 'white',
                         font = '微軟正黑體 15 bold',
                         command = self.change_to_Page2_2)
        btn2.place(x = 150, y = 450)

        im1_1 = Image.open('anime_to_real.jpg')
        im1_1 = im1_1.resize((300, 150))
        im1_1 = ImageTk.PhotoImage(im1_1)
        type1 = tk.Label(image = im1_1,
                         fg = 'blue',
                         text = '',
                         highlightthickness = 1,
                         borderwidth = 1,
                         padx = 0,
                         pady = 0,
                         compound = 'center',
                         font = '微軟正黑體 15 bold')
        type1.place(x = 400, y = 200)

        im1_2 = Image.open('real_to_anime.jpg')
        im1_2 = im1_2.resize((300, 150))
        im1_2 = ImageTk.PhotoImage(im1_2)
        type2 = tk.Label(image = im1_2,
                         fg = 'blue',
                         text = '',
                         highlightthickness = 1,
                         borderwidth = 1,
                         padx = 0,
                         pady = 0,
                         compound = 'center',
                         font = '微軟正黑體 15 bold')
        type2.place(x = 400, y = 400)
        
        
                         
    def change_to_Page2_1(self):
        self.destroyPage1()
        self.Page2()
        self.Page2_1()

    def change_to_Page2_2(self):
        self.destroyPage1()
        self.Page2()
        self.Page2_2()

    def Page2(self):
        global image, combobox, uploadBtn, savefileBtn
        global im3, im4, im5, imRequire
        global labelImgIn, labelImgOut, btnOK, labelRequire, btnRestart
        global filePath
        global okPressed

        filePath, okPressed = '', 0
        uploadBtn = tk.Button(text = '上傳圖片',
                              font = '微軟正黑體 15 bold',
                              command = self.fileOpen)
        uploadBtn.place(x = 120, y = 500)
        
        savefileBtn = tk.Button(text = '另存新檔',
                                font = '微軟正黑體 15 bold',
                                state = tk.DISABLED,
                                command = self.fileSave)
        savefileBtn.place(x = 550, y = 500)

        region = (100, 200, 380, 480)
        cropped = image.crop(region)
        im4 = ImageTk.PhotoImage(cropped)
        labelImgIn = tk.Label(image = im4,
                             fg = 'blue',
                             text = '上傳圖片顯示區',
                             highlightthickness = 1,
                             borderwidth = 1,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = '微軟正黑體 15 bold')
        labelImgIn.place(x = 100, y = 200)

        region = (450, 200, 730, 480)
        cropped = image.crop(region)
        im5 = ImageTk.PhotoImage(cropped)
        labelImgOut = tk.Label(image = im5,
                             fg = 'blue',
                             text = '結果顯示區',
                             highlightthickness = 1,
                             borderwidth = 1,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = '微軟正黑體 15 bold')
        labelImgOut.place(x = 450, y = 200)

        btnOK = tk.Button(text = 'OK',
                          font = '微軟正黑體 15 bold',bg = '#9F88FF',
                          state = tk.DISABLED,
                          command = self.Transform)
        btnOK.place(x = 250, y = 500)

        region = (250, 135, 540, 190)
        cropped = image.crop(region)
        imRequire = ImageTk.PhotoImage(cropped)
        labelRequire = tk.Label(image = imRequire,
                             fg = 'red',
                             text = '',
                             highlightthickness = 0,
                             borderwidth = 0,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = '微軟正黑體 15 bold')
        labelRequire.place(x = 250, y = 135)

        btnRestart = tk.Button(text = 'Restart',
                               font = '微軟正黑體 15 bold',bg = '#9F88FF',
                               command = self.restart)
        btnRestart.place(x = 650, y = 20)

    def Page2_1(self):
        global decision, remind, image, im_re
        decision = 1
        region = (20, 100, 200, 200)
        cropped = image.crop(region)
        im_re = ImageTk.PhotoImage(cropped)
        remind = tk.Label(image = im_re,
                             fg = 'blue',
                             text = '請上傳動畫圖片:',
                             highlightthickness = 0,
                             borderwidth = 0,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = '微軟正黑體 15 bold')
        remind.place(x = 20, y = 100)

    def Page2_2(self):
        global decision, image, im3, combobox, remind, im_re, label2_1
        decision = 2

        region = (20, 100, 200, 200)
        cropped = image.crop(region)
        im_re = ImageTk.PhotoImage(cropped)
        remind = tk.Label(image = im_re,
                             fg = 'blue',
                             text = '請上傳真人圖片:',
                             highlightthickness = 0,
                             borderwidth = 0,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = '微軟正黑體 15 bold')
        remind.place(x = 20, y = 100)
        
        region = (20, 20, 180, 70)
        cropped = image.crop(region)
        im3 = ImageTk.PhotoImage(cropped)
        label2_1 = tk.Label(image = im3,
                             fg = 'blue',
                             text = '請選擇畫風:',
                             highlightthickness = 0,
                             borderwidth = 0,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = '微軟正黑體 20 bold')
        label2_1.place(x = 20, y = 20)

        combobox = ttk.Combobox(values = ['現代動畫畫風', 'gyate', 'JOJO', '90年代動畫畫風'],
                                font = '微軟正黑體 15 normal',
                                state = 'readonly')
        combobox.place(x = 200, y = 30)
        combobox.current(0)

    def createLabel(self, num, text1, color, textSize, x1, y1, x2, y2):
        global image, im1, im2, label1, label2
        region = (x1, y1, x2, y2)
        cropped = image.crop(region)
        temp = '微軟正黑體 ' + str(textSize) + ' bold'
        if num == 1:
            im1 = ImageTk.PhotoImage(cropped)
            label1 = tk.Label(image = im1,
                             fg = color,
                             text = text1,
                             highlightthickness = 0,
                             borderwidth = 0,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = temp)
            label1.place(x = x1, y = y1)
        else:
            im2 = ImageTk.PhotoImage(cropped)
            label2 = tk.Label(image = im2,
                             fg = color,
                             text = text1,
                             highlightthickness = 0,
                             borderwidth = 0,
                             padx = 0,
                             pady = 0,
                             compound = 'center',
                             font = temp)
            label2.place(x = x1, y = y1)

    def destroyPage1(self):
        global btn1, btn2, label1, label2, bgid, type1, type2
        global imageFile, image, im1, im2, canvas
        image = Image.open('background_1.jpg')
        image = image.resize((800, 600))
        imageFile = ImageTk.PhotoImage(image)
        bgid = canvas.create_image(0, 0, image = imageFile, anchor = 'nw')
        btn1.destroy()
        btn2.destroy()
        label1.destroy()
        label2.destroy()
        type1.destroy()
        type2.destroy()
        

    def fileOpen(self):
        global filePath, inputImage, labelImgIn, combobox, btnOK
        filePathTmp = filedialog.askopenfilename(
                        title = u'選擇上傳檔案',
                        filetypes = (('圖片', ['*.jpeg', '*.jpg', '*.png']),
                                     ('all files', '*.*')))

        if filePathTmp != '':
            filePath = filePathTmp

        if filePath != '':
            inputImage = Image.open(filePath)
            inputImage = inputImage.resize((280, 280))
            inputImage = ImageTk.PhotoImage(inputImage)
            labelImgIn.config(image = inputImage, text = '')
            btnOK.config(state = tk.NORMAL)


    def fileSave(self):
        global saveName, okPressed, labelRequire
        savePath = filedialog.asksaveasfilename(
                            title = u'另存新檔',
                            defaultextension = '.png',
                            filetypes = (('圖片', ['*.jpeg', '*.jpg', '*.png']),
                                         ('all files', '*.*')))
        if savePath != '':
            tempImg = Image.open(saveName)
            tempImg.save(savePath)


    def Transform(self):
        global decision, filePath, combobox, saveName, outputImage, savefileBtn
        global labelRequire
        global okPressed
        saveName = 'test.png'

        if filePath != '':
            t = threading.Thread(target = self.APIrunning)
            t.start()
            labelRequire.config(text = '')
            okPressed = 1


    def restart(self):
        self.destroyPage2()
        self.startPage()

    def destroyPage2(self):
        global remind, uploadBtn, savefileBtn
        global labelImgIn, labelImgOut, btnOK, labelRequire
        global btnRestart, okPressed
        remind.destroy()
        uploadBtn.destroy()
        savefileBtn.destroy()
        labelImgIn.destroy()
        labelImgOut.destroy()
        btnOK.destroy()
        labelRequire.destroy()
        btnRestart.destroy()
        okPressed = 0

        if decision == 2:
            global label2_1, combobox
            label2_1.destroy()
            combobox.destroy()
        
    def APIrunning(self):
        global saveName, outputImage, labelImgOut, decision, combobox
        global labelRequire, labelImgOut, im5, savefileBtn
        labelImgOut.config(image = im5, text = '結果顯示區')
        labelRequire.config(text = '請稍候...')
        savefileBtn.config(state = tk.DISABLED)
        if decision == 1:
            filename = anime2real(filePath, savePath = saveName)
        else:
            if combobox.current() == 0:
                filename = real2anime(filePath, savePath = saveName)
            elif combobox.current() == 1:
                filename = real2gyate(filePath, savePath = saveName)
            elif combobox.current() == 2:
                filename = real2jojo(filePath, savePath = saveName)
            elif combobox.current() == 3:
                filename = real2titan(filePath, savePath = saveName)
        outputImage = Image.open(saveName)
        outputImage = outputImage.resize((280, 280))
        outputImage = ImageTk.PhotoImage(outputImage)
        labelImgOut.config(image = outputImage, text = '')
        labelRequire.config(text = '')
        savefileBtn.config(state = tk.NORMAL)
        

if __name__ == '__main__':
    root = tk.Tk()
    ui(root)
    root.mainloop()