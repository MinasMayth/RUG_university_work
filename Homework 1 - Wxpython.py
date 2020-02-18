# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:11:45 2020

@author: pc
"""

import wx

class MyFrame(wx.Frame): 
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        
        my_sizer = wx.BoxSizer(wx.VERTICAL)
       
        
        #First Name Text and Entry Box
        first_name = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(panel, -1, "First Name:") 
		
        first_name.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t1 = wx.TextCtrl(panel) 
		
        first_name.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        
        my_sizer.Add(first_name)
        
        #Last Name Text and Entry Box
        last_name = wx.BoxSizer(wx.HORIZONTAL) 
        l2 = wx.StaticText(panel, -1, "Last Name:") 
		
        last_name.Add(l2, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t2 = wx.TextCtrl(panel) 
		
        last_name.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        
        my_sizer.Add(last_name)
        
        #Math Grade Text and Entry Box
        math_grade = wx.BoxSizer(wx.HORIZONTAL) 
        l3 = wx.StaticText(panel, -1, "Math Grade:") 
		
        math_grade.Add(l3, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t3 = wx.TextCtrl(panel) 
		
        math_grade.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        
        my_sizer.Add(math_grade)
        
        #English Grade Text and Entry Box
        eng_grade = wx.BoxSizer(wx.HORIZONTAL) 
        l4 = wx.StaticText(panel, -1, "English Grade:") 
		
        eng_grade.Add(l4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t4 = wx.TextCtrl(panel) 
		
        eng_grade.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        
        my_sizer.Add(eng_grade)
        
        
        
        
        #Enter Button
        enter_btn = wx.Button(panel, label='Enter')
        enter_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(enter_btn, 0, wx.ALL | wx.CENTER, 5) 

        panel.SetSizer(my_sizer)
        self.Show()
        
    def on_press(self, event):
        
        #What happens when the enter button is pressed
        
        first_name = str(self.t1.GetValue())
        last_name = str(self.t2.GetValue())
        math_grade = float(self.t3.GetValue())
        eng_grade = float(self.t4.GetValue())
        
        #Average grade computation
        avg_grade = (math_grade + eng_grade)/2

        #Output
        print ("The student's name is " + first_name, last_name + ".")
        print ("Their Math grade is " + str(math_grade) + """, and their English grade is """ + str(eng_grade) + ".")
        print ("This results in an average of " + str(avg_grade) + ".")
    
#Main Script
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()