# https://doc.qt.io/qtforpython-5/PySide2/QtCore/QObject.html#PySide2.QtCore.PySide2.QtCore.QObject.findChildren

widgets = mprun.findChildren(QToolBar, options=Qt.FindChildOption.FindChildrenRecursively)
for toolbar in widgets:
  toolbar.wheelEvent = lambda *event: None   # this disables mouse scrolling on toolbars
