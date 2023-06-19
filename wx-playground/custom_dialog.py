import wx

class CustomDialog(wx.Dialog):
    def __init__(self, parent, message):
        super().__init__(parent, title="Custom Dialog")

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add the message text
        message_label = wx.StaticText(self, label=message)
        sizer.Add(message_label, 0, wx.ALL, 10)

        # Create the buttons
        button_labels = ["Yes, use cloud data", "No, Refresh locally", "No, Refresh and update in cloud"]
        self.button_ids = []
        for label in button_labels:
            button = wx.Button(self, label=label)
            button.Bind(wx.EVT_BUTTON, self.on_button_click)
            sizer.Add(button, 0, wx.ALL, 5)
            self.button_ids.append(button.GetId())

        self.SetSizerAndFit(sizer)

    def on_button_click(self, event):
        button_id = event.GetEventObject().GetId()
        self.result = button_id
        self.Close()
def showCustomDialog():
    frame = wx.Frame(None)
    dialog = CustomDialog(frame, "Do you want to use cloud data?")

    if dialog.ShowModal() == wx.ID_OK:
        result = dialog.result
        if result in dialog.button_ids:
            button_index = dialog.button_ids.index(result)
            label = button_labels[button_index]
            print("User selected:", label)

    dialog.Destroy()
def showMessageDialog():
    msg_dlg = wx.MessageDialog(None, "Do you want to use the local data?", "Confirm Load", wx.YES | wx.NO | wx.ICON_QUESTION)
    msg_dlg.ShowModal()

# Example usage
app = wx.App()
showCustomDialog()
# showMessageDialog()
app.MainLoop()
