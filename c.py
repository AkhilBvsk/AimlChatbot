from tkinter import *
import fileinput
import aiml
bot=aiml.Kernel()
bot.learn("newfile.aiml")

WindowTitle = 'STUDENT ASSISTANT'

def ClickAction():
    #Write message to chat window
    EntryText = EntryBox.get("0.0",END)
    #LoadMyEntry(ChatLog, EntryText)
    ChatLog.config(state=NORMAL)
    log = open('name.txt', 'r')
    user=log.read()
    log.close()
    ChatLog.insert(END, "\n\n"+user+": "+EntryText)
    temp = bot.respond(EntryText)
    #Erace previous message in Entry Box
    if temp!="":
        ChatLog.insert(END, "\nTARS: "+temp)
        EntryBox.delete("0.0",END)
    else:
        ChatLog.insert(END, "Bot: Sorry unable to find, but you can add your answer in other textbox ")
        EntryBox1.config(state=NORMAL)
    ChatLog.config(state=DISABLED)
    #Scroll to the bottom of chat windows
    ChatLog.yview(END)
    
def ClickAction1():
    temp2 = EntryBox1.get("0.0",END)
    if temp2!="\n":
        EntryText = EntryBox.get("0.0",END)
        aimltext='<category> <pattern>'+EntryText.upper()+'</pattern> <template>'+temp2+'</template> </category></aiml>'
        for line in fileinput.FileInput("newfile.aiml",inplace=1):
            line = line.replace("</aiml>",aimltext.replace('\n', ''))
            print (line)
        EntryBox1.delete("0.0",END)
        EntryBox1.config(state=DISABLED)
        bot.learn("newfile.aiml")
    EntryBox.delete("0.0",END)
    
def PressAction(event):
    EntryBox.config(state=NORMAL)
    ClickAction()
def DisableEntry(event):
    EntryBox.config(state=DISABLED)
def DisableEntry1(event):
    EntryBox.config(state=DISABLED)
def PressAction1(event):
    EntryBox1.config(state=DISABLED)
    ClickAction1()
    
base = Tk()
base.title(WindowTitle)
base.geometry("500x600")
base.resizable(width=FALSE, height=FALSE)

ChatLog = Text(base, bd=0, bg="lightcyan", height="8", width="50", font="Arial")
ChatLog.insert(END,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ChatLog.insert(END, "                  STUDENT ASSISTANT            \n")
ChatLog.insert(END,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ChatLog.insert(END,"\n        Ask TARS about timetable and general things!")
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="arrow")
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=30, text="Send", width="10", height=5,
                    bd=0, bg="deepskyblue", activebackground="cyan",
                    command=ClickAction)

EntryBox = Text(base, bd=0,bg="grey84",width="35", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)


EntryBox1 = Text(base, bd=0,bg="grey84",width="29", height="5", font="Arial")
EntryBox1.bind("<Return>", DisableEntry1)
EntryBox1.bind("<KeyRelease-Return>", PressAction1)
EntryBox1.config(state=DISABLED)

SendButton1 = Button(base, font=30, text="Add\nAnswer", width="10", height=5,
                    bd=0, bg="deepskyblue", activebackground="cyan",
                    command=ClickAction1)


scrollbar.place(x=476,y=6, height=486)
ChatLog.place(x=6,y=6, height=486, width=470)
EntryBox.place(x=6, y=501, height=45, width=365)
SendButton.place(x=377, y=501, height=45)

EntryBox1.place(x=6, y=551, height=45, width=365)
SendButton1.place(x=377, y=551, height=45)



base.mainloop()
