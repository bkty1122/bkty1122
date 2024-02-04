Option Compare Database

Public Function Email_to_trainer()

    Dim rs As DAO.Recordset
    Dim content As String
    Set rs = CurrentDb.OpenRecordset("Retired log")
    If (DCount("*", "[Retired log]") = 0) Then
        MsgBox "No record found"
        Exit Function
    End If
    ' Create the html table, word style is arial, size 1
    content = "<html><body>Dear Trainer and Assistant Trainer,<br><br>Please be informed that DVCS has updated the Retired Horse documents, please read them carefully and find attached new version for your kind immediate action.<br><br><table border='1'><tr><br><br>"
    'add heading as per rs fields
    content = content & "<tr>"
    For i = 0 To rs.Fields.Count - 1
        content = content & "<th>" & rs.Fields(i).Name & "</th>"
    Next i
    content = content & "</tr>"
    ' add the data in the table
    Do While Not rs.EOF
        content = content & "<tr>"
        For i = 0 To rs.Fields.Count - 1
            content = content & "<td>" & rs.Fields(i).Value & "</td>"
        Next i
        content = content & "</tr>"
        rs.MoveNext
    Loop
    ' after the loop, close the table, and add the signature
    content = content & "</table><br><br>Action 1: Present part A Veterinary Transition Instructions to your stable vet for completion.  Please retain a copy in order to collect any drugs prescribed from Pharmacy.<br>Action 2: Fill in part B Trainer Report as usual.<br>Action 3: The completed forms (part A&B) should be displayed on the horse’s stable (including if transferred to temporary stables);<br>Action 4: Please return Veterinary Transition Instructions + Trainer Report to vet office by email to transitioninstructionsandtrainerreport@hq.bus.hkjc.org.hk or by fax 2966 6622 or by hand to STCC vet office 1/F.<br><br>As the horses had already been assessed, it would be much appreciated if you can submit the TNT reports as soon as possible.<br><br>Please contact us if you have any queries. Thanks for your kind assistance!<br><br><br>Regards,<br>VCS administration department<br><br>"
    ' Create a new email, content is the html table
    Dim objOutlook As Object
    Dim objMail As Object
    Set objOutlook = CreateObject("Outlook.Application")
    Set objMail = objOutlook.CreateItem(0)

    Dim email As DAO.Recordset
    Set email = CurrentDb.OpenRecordset("Select [Trainer Email] from [Retired log]", dbOpenSnapshot, dbReadOnly)
    Dim strEmailAddess As String

    With email
        Do While Not .EOF
            strEmailAddess = strEmailAddess & ![Trainer Email] & ";"
            .MoveNext
        Loop
    End With
    With objMail
        .To = Left$(strEmailAddess, Len(strEmailAddess) - 1)
        .CC = "sandra.sh.lam@hkjc.org.hk"
        .BCC = ""
        .Subject = Date & " Trainer and Transition Report"
        .HTMLBody = content
        ' Add attachment to the email, if the default path is not working, prompt user to select the file
        On Error GoTo ErrHandler
        .Attachments.Add "C:\Users\beckytykwok\Documents\Access\Automation-Tools-By-Becky\Retired-Horses-Workflow\Transition Instructions & Trainer Report.pdf"
        GoTo NoError
ErrHandler:
        ' If the default path is not working, prompt user to select the file
        Const msoFileDialogFilePicker As Long = 3
        Dim FldrPicker As FileDialog
        Dim strFile As String
        Set FldrPicker = Application.FileDialog(msoFileDialogFilePicker)
        With FldrPicker
            .Title = "Select a File"
            .AllowMultiSelect = False
            .Filters.Clear
            .Filters.Add "PDF", "*.pdf"
            If .Show <> -1 Then GoTo NoError
                strFile = .SelectedItems(1)
                .Attachments.Add strFile
            End If
        End With
        .Display
NoError:
        .Display
    End With
End Function
