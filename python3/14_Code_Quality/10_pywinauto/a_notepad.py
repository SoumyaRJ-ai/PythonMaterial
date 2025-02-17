#!/usr/bin/python
"""
Purpose: Automate windows UI tasks
    pip install -U pywinauto --user
"""

from pywinauto.application import Application

# Run a target application
app = Application().start("notepad.exe")

# Select a menu item
app.UntitledNotepad.menu_select("Help->About Notepad")

# Click on a button
app.AboutNotepad.OK.click()

# Type a text string
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)

# Select a menu item
app.UntitledNotepad.menu_select("File->Save As")

# Save file
app.SaveAs.edit1.set_edit_text("Test_File.txt")
app.SaveAs.Save.click()
