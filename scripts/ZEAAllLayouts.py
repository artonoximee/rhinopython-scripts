import rhinoscriptsyntax as rs

for view_name in rs.ViewNames(return_names = True, view_type=1):
	rs.CurrentView(view_name)
	rs.Command('_Zoom _All _Extents')
