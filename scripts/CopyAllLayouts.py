import rhinoscriptsyntax as rs

obj = rs.GetObject("Select object on layout to copy to all")

rs.SelectObject(obj)
rs.Command('_CopyToClipboard')

rs.EnableRedraw(False)

for view_name in rs.ViewNames(return_names = True, view_type=1):
	rs.CurrentView(view_name)
	rs.Command('_Paste')
    
rs.EnableRedraw(True)