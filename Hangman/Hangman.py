#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import wx
import gui
import random

class MainWindow(gui.MainWindow):
    def __init__(self, parent=None):
        gui.MainWindow.__init__(self, parent)
        self.Center()

        self.Words = ("black", "blue", "white", "red", "green", "yellow", "purple", "pink", "gray", "orange")

        self.StartNewGame()
                
    def StartNewGame(self):
        self.Word = random.choice(self.Words).upper()
        self.HiddenWord = self._GetHiddenWord()
        
        self.Lives = 6
        self.m_word.SetValue(self.HiddenWord)
        self.m_gauge_lives.SetRange(self.Lives)
        self.m_gauge_lives.SetValue(self.Lives)

        self._EnableButtons()
        self.m_word.SetForegroundColour('BLACK')
        
    def LetterButtonClicked( self, event ):
        button = event.GetEventObject()
        letter = button.Label
        
        button.Disable()

        if letter in self.Word:
            self._ShowChars(letter)
            
            if self.HiddenWord == self.Word:
                self.m_word.SetForegroundColour('GREEN')
                self._DisableButtons()
        else:
            self.Lives -= 1
            self.m_gauge_lives.SetValue(self.Lives)
            
            if self.Lives == 0:
                self.m_word.SetValue(self.Word)
                self.m_word.SetForegroundColour('RED')
                self.m_word.Refresh()
                self._DisableButtons()
    
    def NewGameButtonClicked( self, event ):
        self.StartNewGame()

    def LoadButtonClicked( self, event ):
        dialog = wx.FileDialog(self, "Open new words file", wildcard = "Hangman files (*.hgm)|*.hgm", style= wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        self.Words = []
        with open(dialog.GetFilename()) as f:
            for line in f.readlines():
                self.Words.append(line.strip())
        
        self.StartNewGame()

    def _ShowChars(self, char):
        newWord = ""

        for i in range(0, len(self.Word)):
            if self.Word[i] == char:
                newWord = newWord + self.Word[i]
            else:
                newWord = newWord + self.HiddenWord[i]

        self.HiddenWord = newWord
        self.m_word.SetValue(self.HiddenWord)

    def _GetHiddenWord(self):
        hidden = ""

        for i in range(0, len(self.Word)):
            if self.Word[i] == " ":
                hidden += " "
            else:
                hidden += "*"

        return hidden

    def _DisableButtons(self):
        self.m_btn_Key0.Disable()
        self.m_btn_Key1.Disable()
        self.m_btn_Key2.Disable()
        self.m_btn_Key3.Disable()
        self.m_btn_Key4.Disable()
        self.m_btn_Key5.Disable()
        self.m_btn_Key6.Disable()
        self.m_btn_Key7.Disable()
        self.m_btn_Key8.Disable()
        self.m_btn_Key9.Disable()
        self.m_btn_Key10.Disable()
        self.m_btn_Key11.Disable()
        self.m_btn_Key12.Disable()
        self.m_btn_Key13.Disable()
        self.m_btn_Key14.Disable()
        self.m_btn_Key15.Disable()
        self.m_btn_Key16.Disable()
        self.m_btn_Key17.Disable()
        self.m_btn_Key18.Disable()
        self.m_btn_Key19.Disable()
        self.m_btn_Key20.Disable()
        self.m_btn_Key21.Disable()
        self.m_btn_Key22.Disable()
        self.m_btn_Key23.Disable()
        self.m_btn_Key24.Disable()
        self.m_btn_Key25.Disable()

    def _EnableButtons(self):
        self.m_btn_Key0.Enable()
        self.m_btn_Key1.Enable()
        self.m_btn_Key2.Enable()
        self.m_btn_Key3.Enable()
        self.m_btn_Key4.Enable()
        self.m_btn_Key5.Enable()
        self.m_btn_Key6.Enable()
        self.m_btn_Key7.Enable()
        self.m_btn_Key8.Enable()
        self.m_btn_Key9.Enable()
        self.m_btn_Key10.Enable()
        self.m_btn_Key11.Enable()
        self.m_btn_Key12.Enable()
        self.m_btn_Key13.Enable()
        self.m_btn_Key14.Enable()
        self.m_btn_Key15.Enable()
        self.m_btn_Key16.Enable()
        self.m_btn_Key17.Enable()
        self.m_btn_Key18.Enable()
        self.m_btn_Key19.Enable()
        self.m_btn_Key20.Enable()
        self.m_btn_Key21.Enable()
        self.m_btn_Key22.Enable()
        self.m_btn_Key23.Enable()
        self.m_btn_Key24.Enable()
        self.m_btn_Key25.Enable()

class App(wx.App):
    def OnInit(self):
        self.frame = MainWindow()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App(0)
    app.MainLoop()
 
if __name__ == '__main__':
    main()