from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_client_window(object):
    def __init__(self):
        self.actionsend = None
        self.send_button = None
        self.messanger_edit = None
        self.line = None
        self.horizontalLayout = None
        self.line_3 = None
        self.tb_smile_4 = None
        self.tb_smile_3 = None
        self.tb_smile_2 = None
        self.tb_smile_1 = None
        self.tb_u = None
        self.line_2 = None
        self.tb_i = None
        self.tb_b = None
        self.horizontalLayout_4 = None
        self.line_4 = None
        self.horizontalLayout_2 = None
        self.verticalLayout = None
        self.messanges_list = None
        self.dialogs_list = None
        self.horizontalLayout_3 = None
        self.messanger_window = None

    def setupUi(self, client_window):
        client_window.setObjectName("client_window")
        client_window.resize(648, 600)
        self.messanger_window = QtWidgets.QWidget(client_window)
        self.messanger_window.setMinimumSize(QtCore.QSize(648, 600))
        self.messanger_window.setObjectName("messanger_window")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.messanger_window)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dialogs_list = QtWidgets.QListWidget(self.messanger_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogs_list.sizePolicy().hasHeightForWidth())
        self.dialogs_list.setSizePolicy(sizePolicy)
        self.dialogs_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dialogs_list.setLineWidth(1)
        self.dialogs_list.setObjectName("dialogs_list")
        self.horizontalLayout_2.addWidget(self.dialogs_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.messanges_list = QtWidgets.QListWidget(self.messanger_window)
        self.messanges_list.setLineWidth(2)
        self.messanges_list.setObjectName("messanges_list")
        self.verticalLayout.addWidget(self.messanges_list)
        self.line_4 = QtWidgets.QFrame(self.messanger_window)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tb_b = QtWidgets.QToolButton(self.messanger_window)
        self.tb_b.setObjectName("tb_b")
        self.horizontalLayout_4.addWidget(self.tb_b)
        self.tb_i = QtWidgets.QToolButton(self.messanger_window)
        self.tb_i.setObjectName("tb_i")
        self.horizontalLayout_4.addWidget(self.tb_i)
        self.tb_u = QtWidgets.QToolButton(self.messanger_window)
        self.tb_u.setObjectName("tb_u")
        self.horizontalLayout_4.addWidget(self.tb_u)
        self.line_2 = QtWidgets.QFrame(self.messanger_window)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.tb_smile_1 = QtWidgets.QToolButton(self.messanger_window)
        self.tb_smile_1.setObjectName("tb_smile_1")
        self.horizontalLayout_4.addWidget(self.tb_smile_1)
        self.tb_smile_2 = QtWidgets.QToolButton(self.messanger_window)
        self.tb_smile_2.setObjectName("tb_smile_2")
        self.horizontalLayout_4.addWidget(self.tb_smile_2)
        self.tb_smile_3 = QtWidgets.QToolButton(self.messanger_window)
        self.tb_smile_3.setObjectName("tb_smile_3")
        self.horizontalLayout_4.addWidget(self.tb_smile_3)
        self.tb_smile_4 = QtWidgets.QToolButton(self.messanger_window)
        self.tb_smile_4.setObjectName("tb_smile_4")
        self.horizontalLayout_4.addWidget(self.tb_smile_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.messanger_window)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(self.messanger_window)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.messanger_edit = QtWidgets.QTextEdit(self.messanger_window)
        self.messanger_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.messanger_edit.setObjectName("messanger_edit")
        self.horizontalLayout.addWidget(self.messanger_edit)
        self.send_button = QtWidgets.QPushButton(self.messanger_window)
        self.send_button.setMinimumSize(QtCore.QSize(50, 0))
        self.send_button.setMaximumSize(QtCore.QSize(16777215, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon)
        self.send_button.setObjectName("send_button")
        self.horizontalLayout.addWidget(self.send_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        client_window.setCentralWidget(self.messanger_window)
        self.actionsend = QtWidgets.QAction(client_window)
        self.actionsend.setIcon(icon)
        self.actionsend.setObjectName("actionsend")

        self.retranslateUi(client_window)
        QtCore.QMetaObject.connectSlotsByName(client_window)

    def retranslateUi(self, client_window):
        _translate = QtCore.QCoreApplication.translate
        client_window.setWindowTitle(_translate("client_window", "Messanger Client"))
        self.tb_b.setText(_translate("client_window", "..."))
        self.tb_i.setText(_translate("client_window", "..."))
        self.tb_u.setText(_translate("client_window", "..."))
        self.tb_smile_1.setText(_translate("client_window", "..."))
        self.tb_smile_2.setText(_translate("client_window", "..."))
        self.tb_smile_3.setText(_translate("client_window", "..."))
        self.tb_smile_4.setText(_translate("client_window", "..."))
        self.send_button.setText(_translate("client_window", "Отправить"))
        self.actionsend.setText(_translate("client_window", "send"))