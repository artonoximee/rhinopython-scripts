import rhinoscriptsyntax as rs

def MaterialColorToObject():
    ids = rs.GetObjects("Select objects",preselect=True)
    if not ids:return
    
    for id in ids:
        color = rs.CreateColor(255, 0, 0)
        rs.ObjectColor(id,color)
        rs.ObjectPrintColor(id,color)
        
        
if __name__ == '__main__':MaterialColorToObject()