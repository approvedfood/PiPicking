from tkinter import *
import paho.mqtt.client as mqtt
import datetime

class GuiSetup:


    def __init__(self,master):
        topframe = Frame(master)
        topframe.grid(row=0)
        midframe = Frame(master)
        midframe.grid(row=1)
        bottomframe = Frame(master)
        bottomframe.grid(row=2)

        # label
        self.lbl_userid = Label(topframe, text="Enter User ID")
        self.lbl_userid.grid(row = 0)
        # Entry box
        v = StringVar()
        self.entry_userid = Entry(topframe,textvariable=v)
        self.entry_userid.grid(row = 0, column=1)


        def subscribeClient(self):
            channel = v.get()
            print(channel)
            # self.f = str(self.lbl_connectionstatus['text'])

            client.unsubscribe(str(t.get()))
            print("Connected with result code " + str(channel))
            # Subscribing in on_connect() means that if we lose the connection and
            # reconnect then subscriptions will be renewed.
            client.subscribe("approvedfood/picking/" + str(channel))
            t.set(str("approvedfood/picking/" + str(channel)))
            cleanlabels()

        #Button
        self.btn_userid = Button(topframe, text = "Go")
        self.btn_userid.bind("<Button-1>", subscribeClient)
        self.btn_userid.grid(row = 0, column=2)
        # Connection lbl
        self.lbl_connection = Label(topframe, text="Connection Status")
        self.lbl_connection.grid(row=1, column=0)
        # Connection status
        t = StringVar()
        self.lbl_connectionstatus = Label(topframe, text="Not Connected",textvariable = t)
        self.lbl_connectionstatus.grid(row=1, column=1)

        #Row 0
        prod0frame = Frame(midframe)
        prod0frame.grid(row=0, column=0)
        self.lblprod0 = Label(prod0frame, text="Location 1")
        self.lblprod0.grid(row=0, column=0)
        self.lblprod0status = Label(prod0frame, text="Status", bg="grey")
        self.lblprod0status.grid(row=0, column=1)

        #Row 1
        prod1frame = Frame(midframe)
        prod1frame.grid(row=1, column=0)
        self.lblprod1 = Label(prod1frame, text="Location 2")
        self.lblprod1.grid(row=1, column=0)
        self.lblprod1status = Label(prod1frame, text="Status", bg="grey")
        self.lblprod1status.grid(row=1, column=1)

        #Row 2
        prod2frame = Frame(midframe)
        prod2frame.grid(row=2, column=0)
        self.lblprod2 = Label(prod2frame, text="Location 3")
        self.lblprod2.grid(row=2, column=0)
        self.lblprod2status = Label(prod2frame, text="Status", bg="grey")
        self.lblprod2status.grid(row=2, column=1)

        # Row 3
        prod3frame = Frame(midframe)
        prod3frame.grid(row=3, column=0)
        self.lblprod3 = Label(prod3frame, text="Location 4")
        self.lblprod3.grid(row=3, column=0)
        self.lblprod3status = Label(prod3frame, text="Status", bg="grey")
        self.lblprod3status.grid(row=3, column=1)

        # Row 4
        prod4frame = Frame(midframe)
        prod4frame.grid(row=4, column=0)
        self.lblprod4 = Label(prod4frame, text="Location 5")
        self.lblprod4.grid(row=4, column=0)
        self.lblprod4status = Label(prod4frame, text="Status", bg="grey")
        self.lblprod4status.grid(row=4, column=1)

        # Row 5
        prod5frame = Frame(midframe)
        prod5frame.grid(row=5, column=0)
        self.lblprod5 = Label(prod5frame, text="Location 6")
        self.lblprod5.grid(row=5, column=0)
        self.lblprod5status = Label(prod5frame, text="Status", bg="grey")
        self.lblprod5status.grid(row=5, column=1)

        # Row 6
        prod6frame = Frame(midframe)
        prod6frame.grid(row=6, column=0)
        self.lblprod6 = Label(prod6frame, text="Location 7")
        self.lblprod6.grid(row=6, column=0)
        self.lblprod6status = Label(prod6frame, text="Status", bg="grey")
        self.lblprod6status.grid(row=6, column=1)

        # Row 7
        prod7frame = Frame(midframe)
        prod7frame.grid(row=7, column=0)
        self.lblprod7 = Label(prod7frame, text="Location 8")
        self.lblprod7.grid(row=7, column=0)
        self.lblprod7status = Label(prod7frame, text="Status", bg="grey")
        self.lblprod7status.grid(row=7, column=1)

        # last updated status
        self.lbllastupdated = Label(bottomframe, text="Last Updated")
        self.lbllastupdated.grid(row = 0)
        updatetime = StringVar()
        self.lblUpdateTime = Label(bottomframe, textvariable = updatetime)
        self.lblUpdateTime.grid(row=0, column=1)
        updatetime.set(datetime.datetime.now().time())

        def cleanlabels():
            self.lblprod0status['bg'] = "grey"
            self.lblprod1status['bg'] = "grey"
            self.lblprod2status['bg'] = "grey"
            self.lblprod3status['bg'] = "grey"
            self.lblprod4status['bg'] = "grey"
            self.lblprod5status['bg'] = "grey"
            self.lblprod6status['bg'] = "grey"
            self.lblprod7status['bg'] = "grey"


        # The callback for when the client receives a CONNACK response from the server.

        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))
            # Subscribing in on_connect() means that if we lose the connection and
            # reconnect then subscriptions will be renewed.
            client.subscribe("approvedfood/picking/")
            t.set("approvedfood/picking/")
            # self.lbl_connectionstatus['text'] = "approvedfood/picking/"

    # The callback for when a PUBLISH message is received from the server.
        def on_message(client, userdata, msg):
            print(str(msg.payload))
            self.lblUpdateTime=str(datetime.datetime.now().time())
            self.lblprod0status['bg'] = "grey"
            self.lblprod1status['bg'] = "grey"
            self.lblprod2status['bg'] = "grey"
            self.lblprod3status['bg'] = "grey"
            self.lblprod4status['bg'] = "grey"
            self.lblprod5status['bg'] = "grey"
            self.lblprod6status['bg'] = "grey"
            self.lblprod7status['bg'] = "grey"

            if str(msg.payload) == "b'A'":
                self.lblprod0status['bg'] = "green"
            elif str(msg.payload) == "b'B'":
                self.lblprod1status['bg'] = "green"
            elif str(msg.payload) == "b'C'":
                self.lblprod2status['bg'] = "green"
            elif str(msg.payload) == "b'D'":
                self.lblprod3status['bg'] = "green"
            elif str(msg.payload) == "b'E'":
                self.lblprod4status['bg'] = "green"
            elif str(msg.payload) == "b'F'":
                self.lblprod5status['bg'] = "green"
            elif str(msg.payload) == "b'G'":
                self.lblprod6status['bg'] = "green"
            elif str(msg.payload) == "b'H'":
                self.lblprod7status['bg'] = "green"



        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("test.mosquitto.org", 1883, 60)
        client.loop_start()
        # def connect_to_service(self, cservice):
             # client.subscribe("dancluderay" + "/" + str(cservice))


root = Tk()
root.title="Pi Pick"

screen = GuiSetup(root)


print("Setup")


root.mainloop()

print("Finished full setup")
