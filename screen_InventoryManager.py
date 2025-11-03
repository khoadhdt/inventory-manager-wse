# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen_InventoryManager.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import lib_icon_InventoryManagement_rc
import lib_icon_InventoryManagement_rc

class Ui_InventoryManager(object):
    def setupUi(self, InventoryManager):
        if not InventoryManager.objectName():
            InventoryManager.setObjectName(u"InventoryManager")
        InventoryManager.resize(1846, 2063)
        icon = QIcon()
        icon.addFile(u":/icon/images/icon/Inventory Management.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        InventoryManager.setWindowIcon(icon)
        self.images_zoom_label = QLabel(InventoryManager)
        self.images_zoom_label.setObjectName(u"images_zoom_label")
        self.images_zoom_label.setGeometry(QRect(50, 400, 150, 150))
        self.images_zoom_label.setStyleSheet(u"QLabel {\n"
"    background-color: rgba(255, 255, 255, 0.9); /* N\u1ec1n tr\u1eafng m\u1edd, gi\u1eef nguy\u00ean */\n"
"    border: 3px solid #3B82F6; /* Vi\u1ec1n m\u00e0u xanh d\u01b0\u01a1ng nh\u1eb9 */\n"
"    border-radius: 20px; /* G\u00f3c bo tr\u00f2n m\u1ec1m m\u1ea1i */\n"
"    padding: 10px; /* T\u0103ng padding nh\u1eb9 \u0111\u1ec3 tho\u1ea3i m\u00e1i h\u01a1n */\n"
"    opacity: 0; /* \u1ea8n m\u1eb7c \u0111\u1ecbnh */\n"
"}")
        self.images_zoom_label.setFrameShape(QFrame.StyledPanel)
        self.images_zoom_label.setPixmap(QPixmap(u":/icon/images/icon/no_image.png"))
        self.images_zoom_label.setScaledContents(True)
        self.images_zoom_label.setWordWrap(False)
        self.MyWidget = QWidget(InventoryManager)
        self.MyWidget.setObjectName(u"MyWidget")
        self.MyWidget.setGeometry(QRect(9, 9, 1835, 2034))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MyWidget.sizePolicy().hasHeightForWidth())
        self.MyWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_22 = QVBoxLayout(self.MyWidget)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.widget_header = QWidget(self.MyWidget)
        self.widget_header.setObjectName(u"widget_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_header.sizePolicy().hasHeightForWidth())
        self.widget_header.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_open_invoice_button = QPushButton(self.widget_header)
        self.input_open_invoice_button.setObjectName(u"input_open_invoice_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_open_invoice_button.sizePolicy().hasHeightForWidth())
        self.input_open_invoice_button.setSizePolicy(sizePolicy2)
        self.input_open_invoice_button.setMaximumSize(QSize(50, 40))
        self.input_open_invoice_button.setSizeIncrement(QSize(0, 40))
        font = QFont()
        self.input_open_invoice_button.setFont(font)
        self.input_open_invoice_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_open_invoice_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    image: url(:/icon/images/icon/open_126062.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    image: url(:/icon/images/icon/person.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;\n"
"    image: none;\n"
"}\n"
"")
        self.input_open_invoice_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.input_open_invoice_button)

        self.input_check_id_info_checkBox = QCheckBox(self.widget_header)
        self.input_check_id_info_checkBox.setObjectName(u"input_check_id_info_checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.input_check_id_info_checkBox.sizePolicy().hasHeightForWidth())
        self.input_check_id_info_checkBox.setSizePolicy(sizePolicy3)
        self.input_check_id_info_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/load_off.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/load_on.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_check_id_info_checkBox.setChecked(False)

        self.horizontalLayout_2.addWidget(self.input_check_id_info_checkBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.input_logo_label = QLabel(self.widget_header)
        self.input_logo_label.setObjectName(u"input_logo_label")
        sizePolicy3.setHeightForWidth(self.input_logo_label.sizePolicy().hasHeightForWidth())
        self.input_logo_label.setSizePolicy(sizePolicy3)
        self.input_logo_label.setMinimumSize(QSize(70, 42))
        self.input_logo_label.setMaximumSize(QSize(70, 42))
        font1 = QFont()
        font1.setBold(True)
        self.input_logo_label.setFont(font1)
        self.input_logo_label.setStyleSheet(u"")
        self.input_logo_label.setPixmap(QPixmap(u":/icon/images/icon/logo.png"))
        self.input_logo_label.setScaledContents(True)
        self.input_logo_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.input_logo_label)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.title_label = QLabel(self.widget_header)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.title_label.setFont(font2)
        self.title_label.setFrameShape(QFrame.NoFrame)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title_label)

        self.horizontalSpacer_11 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.widget_user = QWidget(self.widget_header)
        self.widget_user.setObjectName(u"widget_user")
        self.gridLayout = QGridLayout(self.widget_user)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_image_user = QWidget(self.widget_user)
        self.horizontalWidget_image_user.setObjectName(u"horizontalWidget_image_user")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget_image_user)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_user_label = QLabel(self.horizontalWidget_image_user)
        self.image_user_label.setObjectName(u"image_user_label")
        sizePolicy3.setHeightForWidth(self.image_user_label.sizePolicy().hasHeightForWidth())
        self.image_user_label.setSizePolicy(sizePolicy3)
        self.image_user_label.setMinimumSize(QSize(32, 40))
        self.image_user_label.setMaximumSize(QSize(32, 32))
        self.image_user_label.setFont(font1)
        self.image_user_label.setStyleSheet(u"QLabel {\n"
"    border: 3px solid #dcdcdc; /* Vi\u1ec1n nh\u1eb9 nh\u00e0ng */\n"
"    border-radius: 3px; /* Bo tr\u00f2n th\u00e0nh h\u00ecnh tr\u00f2n */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    border: 4px solid #3B82F6; /* Vi\u1ec1n xanh khi \u0111\u01b0\u1ee3c focus */\n"
"}\n"
"")
        self.image_user_label.setPixmap(QPixmap(u":/icon/images/icon/User.png"))
        self.image_user_label.setScaledContents(True)
        self.image_user_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.image_user_label)


        self.gridLayout.addWidget(self.horizontalWidget_image_user, 0, 0, 1, 1)

        self.team_user_label = QLabel(self.widget_user)
        self.team_user_label.setObjectName(u"team_user_label")
        sizePolicy1.setHeightForWidth(self.team_user_label.sizePolicy().hasHeightForWidth())
        self.team_user_label.setSizePolicy(sizePolicy1)
        self.team_user_label.setFont(font2)
        self.team_user_label.setFrameShape(QFrame.NoFrame)
        self.team_user_label.setAlignment(Qt.AlignCenter)
        self.team_user_label.setMargin(7)

        self.gridLayout.addWidget(self.team_user_label, 0, 3, 1, 1)

        self.name_user_label = QLabel(self.widget_user)
        self.name_user_label.setObjectName(u"name_user_label")
        sizePolicy1.setHeightForWidth(self.name_user_label.sizePolicy().hasHeightForWidth())
        self.name_user_label.setSizePolicy(sizePolicy1)
        self.name_user_label.setFont(font2)
        self.name_user_label.setFrameShape(QFrame.NoFrame)
        self.name_user_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.name_user_label, 0, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_user)

        self.horizontalSpacer_26 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_26)


        self.verticalLayout_22.addWidget(self.widget_header)

        self.tabWidget_main = QTabWidget(self.MyWidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        sizePolicy.setHeightForWidth(self.tabWidget_main.sizePolicy().hasHeightForWidth())
        self.tabWidget_main.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.tabWidget_main.setFont(font3)
        self.tabWidget_main.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_main.setAutoFillBackground(False)
        self.tabWidget_main.setTabPosition(QTabWidget.South)
        self.tabWidget_main.setTabShape(QTabWidget.Rounded)
        self.tabWidget_main.setIconSize(QSize(32, 32))
        self.tabWidget_main.setElideMode(Qt.ElideLeft)
        self.tabWidget_main.setTabsClosable(False)
        self.tabWidget_main.setTabBarAutoHide(False)
        self.tabLogin = QWidget()
        self.tabLogin.setObjectName(u"tabLogin")
        self.verticalLayout_21 = QVBoxLayout(self.tabLogin)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.horizontalWidget_Login_3 = QWidget(self.tabLogin)
        self.horizontalWidget_Login_3.setObjectName(u"horizontalWidget_Login_3")
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalWidget_Login_3)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_24)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_28 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_28)

        self.widget_7 = QWidget(self.horizontalWidget_Login_3)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy4)
        self.widget_7.setMinimumSize(QSize(400, 0))
        self.widget_7.setMaximumSize(QSize(600, 500))
        self.widget_7.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0, 0.6); /* M\u00e0u n\u1ec1n \u0111en m\u1edd */\n"
"    border-radius: 15px; /* Bo g\u00f3c m\u1ec1m m\u1ea1i */\n"
"}\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.widget_7)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_29)

        self.login_title_label = QLabel(self.widget_7)
        self.login_title_label.setObjectName(u"login_title_label")
        font4 = QFont()
        font4.setPointSize(22)
        font4.setBold(True)
        self.login_title_label.setFont(font4)
        self.login_title_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* N\u1ec1n trong su\u1ed1t */\n"
"    color: #ffffff; /* M\u00e0u ch\u1eef tr\u1eafng (ho\u1eb7c t\u00f9y ch\u1ec9nh theo \u00fd b\u1ea1n) */\n"
"}\n"
"")
        self.login_title_label.setFrameShape(QFrame.NoFrame)
        self.login_title_label.setScaledContents(False)
        self.login_title_label.setAlignment(Qt.AlignCenter)
        self.login_title_label.setWordWrap(False)

        self.verticalLayout_20.addWidget(self.login_title_label)

        self.verticalSpacer_30 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_30)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.login_logo_label = QLabel(self.widget_7)
        self.login_logo_label.setObjectName(u"login_logo_label")
        sizePolicy4.setHeightForWidth(self.login_logo_label.sizePolicy().hasHeightForWidth())
        self.login_logo_label.setSizePolicy(sizePolicy4)
        self.login_logo_label.setMaximumSize(QSize(100, 70))
        self.login_logo_label.setFont(font1)
        self.login_logo_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* N\u1ec1n trong su\u1ed1t */\n"
"}\n"
"")
        self.login_logo_label.setPixmap(QPixmap(u":/icon/images/icon/logo.png"))
        self.login_logo_label.setScaledContents(True)
        self.login_logo_label.setAlignment(Qt.AlignCenter)
        self.login_logo_label.setWordWrap(False)

        self.horizontalLayout_23.addWidget(self.login_logo_label)


        self.verticalLayout_20.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_31 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_31)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.login_msnv_lineedit = QLineEdit(self.widget_7)
        self.login_msnv_lineedit.setObjectName(u"login_msnv_lineedit")
        sizePolicy3.setHeightForWidth(self.login_msnv_lineedit.sizePolicy().hasHeightForWidth())
        self.login_msnv_lineedit.setSizePolicy(sizePolicy3)
        self.login_msnv_lineedit.setMinimumSize(QSize(300, 40))
        self.login_msnv_lineedit.setFont(font)
        self.login_msnv_lineedit.setAutoFillBackground(False)
        self.login_msnv_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.login_msnv_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.login_msnv_lineedit)


        self.verticalLayout_20.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_32 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_32)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.login_password_lineedit = QLineEdit(self.widget_7)
        self.login_password_lineedit.setObjectName(u"login_password_lineedit")
        sizePolicy3.setHeightForWidth(self.login_password_lineedit.sizePolicy().hasHeightForWidth())
        self.login_password_lineedit.setSizePolicy(sizePolicy3)
        self.login_password_lineedit.setMinimumSize(QSize(300, 40))
        self.login_password_lineedit.setFont(font)
        self.login_password_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.login_password_lineedit.setMaxLength(16)
        self.login_password_lineedit.setEchoMode(QLineEdit.Password)
        self.login_password_lineedit.setAlignment(Qt.AlignCenter)
        self.login_password_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_25.addWidget(self.login_password_lineedit)


        self.verticalLayout_20.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_33 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_33)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.login_login_button = QPushButton(self.widget_7)
        self.login_login_button.setObjectName(u"login_login_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.login_login_button.sizePolicy().hasHeightForWidth())
        self.login_login_button.setSizePolicy(sizePolicy5)
        self.login_login_button.setMinimumSize(QSize(300, 50))
        self.login_login_button.setMaximumSize(QSize(16777215, 50))
        self.login_login_button.setSizeIncrement(QSize(0, 40))
        self.login_login_button.setFont(font)
        self.login_login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_login_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    color: #fff;\n"
"    font-size: 14px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font: 75 16pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        self.login_login_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.login_login_button)


        self.verticalLayout_20.addLayout(self.horizontalLayout_26)

        self.login_info_label = QLabel(self.widget_7)
        self.login_info_label.setObjectName(u"login_info_label")
        self.login_info_label.setFont(font3)
        self.login_info_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* N\u1ec1n trong su\u1ed1t */\n"
"	color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.login_info_label.setFrameShape(QFrame.NoFrame)
        self.login_info_label.setScaledContents(False)
        self.login_info_label.setAlignment(Qt.AlignCenter)
        self.login_info_label.setWordWrap(False)

        self.verticalLayout_20.addWidget(self.login_info_label)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_34)


        self.verticalLayout_19.addWidget(self.widget_7)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_35)


        self.horizontalLayout_22.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_25)


        self.verticalLayout_21.addWidget(self.horizontalWidget_Login_3)

        icon1 = QIcon()
        icon1.addFile(u":/icon/images/icon/login_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabLogin, icon1, "")
        self.tabInput = QWidget()
        self.tabInput.setObjectName(u"tabInput")
        self.verticalLayout_5 = QVBoxLayout(self.tabInput)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.widget_nhap_tabin = QWidget(self.tabInput)
        self.widget_nhap_tabin.setObjectName(u"widget_nhap_tabin")
        self.gridLayout_NhapKho = QGridLayout(self.widget_nhap_tabin)
        self.gridLayout_NhapKho.setSpacing(5)
        self.gridLayout_NhapKho.setObjectName(u"gridLayout_NhapKho")
        self.gridLayout_NhapKho.setContentsMargins(5, 5, 5, 5)
        self.input_component_name_labels = QLabel(self.widget_nhap_tabin)
        self.input_component_name_labels.setObjectName(u"input_component_name_labels")
        sizePolicy4.setHeightForWidth(self.input_component_name_labels.sizePolicy().hasHeightForWidth())
        self.input_component_name_labels.setSizePolicy(sizePolicy4)
        self.input_component_name_labels.setFont(font1)
        self.input_component_name_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(self.input_component_name_labels, 1, 6, 1, 1)

        self.input_size_horizontalLayout = QHBoxLayout()
        self.input_size_horizontalLayout.setSpacing(0)
        self.input_size_horizontalLayout.setObjectName(u"input_size_horizontalLayout")
        self.input_length_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_length_lineedit.setObjectName(u"input_length_lineedit")
        self.input_length_lineedit.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.input_length_lineedit.sizePolicy().hasHeightForWidth())
        self.input_length_lineedit.setSizePolicy(sizePolicy3)
        self.input_length_lineedit.setMinimumSize(QSize(100, 29))
        self.input_length_lineedit.setMaximumSize(QSize(100, 29))
        self.input_length_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_length_lineedit.setMaxLength(32767)
        self.input_length_lineedit.setAlignment(Qt.AlignCenter)

        self.input_size_horizontalLayout.addWidget(self.input_length_lineedit)

        self.input_size_label_3 = QLabel(self.widget_nhap_tabin)
        self.input_size_label_3.setObjectName(u"input_size_label_3")
        sizePolicy4.setHeightForWidth(self.input_size_label_3.sizePolicy().hasHeightForWidth())
        self.input_size_label_3.setSizePolicy(sizePolicy4)
        self.input_size_label_3.setFont(font1)
        self.input_size_label_3.setMargin(7)

        self.input_size_horizontalLayout.addWidget(self.input_size_label_3)

        self.input_width_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_width_lineedit.setObjectName(u"input_width_lineedit")
        self.input_width_lineedit.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.input_width_lineedit.sizePolicy().hasHeightForWidth())
        self.input_width_lineedit.setSizePolicy(sizePolicy3)
        self.input_width_lineedit.setMinimumSize(QSize(100, 29))
        self.input_width_lineedit.setMaximumSize(QSize(100, 29))
        self.input_width_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_width_lineedit.setMaxLength(32767)
        self.input_width_lineedit.setAlignment(Qt.AlignCenter)

        self.input_size_horizontalLayout.addWidget(self.input_width_lineedit)

        self.input_size_label_4 = QLabel(self.widget_nhap_tabin)
        self.input_size_label_4.setObjectName(u"input_size_label_4")
        sizePolicy4.setHeightForWidth(self.input_size_label_4.sizePolicy().hasHeightForWidth())
        self.input_size_label_4.setSizePolicy(sizePolicy4)
        self.input_size_label_4.setFont(font1)
        self.input_size_label_4.setMargin(7)

        self.input_size_horizontalLayout.addWidget(self.input_size_label_4)

        self.input_height_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_height_lineedit.setObjectName(u"input_height_lineedit")
        self.input_height_lineedit.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.input_height_lineedit.sizePolicy().hasHeightForWidth())
        self.input_height_lineedit.setSizePolicy(sizePolicy3)
        self.input_height_lineedit.setMinimumSize(QSize(100, 29))
        self.input_height_lineedit.setMaximumSize(QSize(100, 29))
        self.input_height_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_height_lineedit.setMaxLength(32767)
        self.input_height_lineedit.setAlignment(Qt.AlignCenter)

        self.input_size_horizontalLayout.addWidget(self.input_height_lineedit)

        self.input_size_label_2 = QLabel(self.widget_nhap_tabin)
        self.input_size_label_2.setObjectName(u"input_size_label_2")
        sizePolicy4.setHeightForWidth(self.input_size_label_2.sizePolicy().hasHeightForWidth())
        self.input_size_label_2.setSizePolicy(sizePolicy4)
        self.input_size_label_2.setFont(font1)
        self.input_size_label_2.setMargin(7)

        self.input_size_horizontalLayout.addWidget(self.input_size_label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.input_size_horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_NhapKho.addLayout(self.input_size_horizontalLayout, 4, 3, 1, 1)

        self.widget_zoom_tabin = QWidget(self.widget_nhap_tabin)
        self.widget_zoom_tabin.setObjectName(u"widget_zoom_tabin")
        self.input_hz_layout_zoom_radio = QHBoxLayout(self.widget_zoom_tabin)
        self.input_hz_layout_zoom_radio.setSpacing(6)
        self.input_hz_layout_zoom_radio.setObjectName(u"input_hz_layout_zoom_radio")
        self.input_hz_layout_zoom_radio.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.input_hz_layout_zoom_radio.setContentsMargins(5, 5, 5, 5)
        self.input_zoom_dec_button = QPushButton(self.widget_zoom_tabin)
        self.input_zoom_dec_button.setObjectName(u"input_zoom_dec_button")
        sizePolicy3.setHeightForWidth(self.input_zoom_dec_button.sizePolicy().hasHeightForWidth())
        self.input_zoom_dec_button.setSizePolicy(sizePolicy3)
        self.input_zoom_dec_button.setMinimumSize(QSize(28, 28))
        self.input_zoom_dec_button.setMaximumSize(QSize(28, 28))
        self.input_zoom_dec_button.setSizeIncrement(QSize(0, 40))
        self.input_zoom_dec_button.setFont(font)
        self.input_zoom_dec_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_zoom_dec_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    padding: 8px 16px; /* \u0110i\u1ec1u ch\u1ec9nh padding \u0111\u1ec3 n\u00fat c\u00f3 kh\u00f4ng gian tho\u1ea3i m\u00e1i h\u01a1n */\n"
"    border-radius: 11px; /* Bo tr\u00f2n g\u00f3c */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/icon/Zoom_des.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_zoom_dec_button.setIcon(icon2)
        self.input_zoom_dec_button.setIconSize(QSize(24, 24))

        self.input_hz_layout_zoom_radio.addWidget(self.input_zoom_dec_button)

        self.horizontalSpacer_16 = QSpacerItem(120, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.input_hz_layout_zoom_radio.addItem(self.horizontalSpacer_16)

        self.input_zoom_inc_button = QPushButton(self.widget_zoom_tabin)
        self.input_zoom_inc_button.setObjectName(u"input_zoom_inc_button")
        sizePolicy3.setHeightForWidth(self.input_zoom_inc_button.sizePolicy().hasHeightForWidth())
        self.input_zoom_inc_button.setSizePolicy(sizePolicy3)
        self.input_zoom_inc_button.setMinimumSize(QSize(28, 28))
        self.input_zoom_inc_button.setMaximumSize(QSize(25, 25))
        self.input_zoom_inc_button.setSizeIncrement(QSize(0, 40))
        self.input_zoom_inc_button.setFont(font)
        self.input_zoom_inc_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_zoom_inc_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    padding: 8px 16px; /* \u0110i\u1ec1u ch\u1ec9nh padding \u0111\u1ec3 n\u00fat c\u00f3 kh\u00f4ng gian tho\u1ea3i m\u00e1i h\u01a1n */\n"
"    border-radius: 11px; /* Bo tr\u00f2n g\u00f3c */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/images/icon/Zoom_ins.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_zoom_inc_button.setIcon(icon3)
        self.input_zoom_inc_button.setIconSize(QSize(24, 24))

        self.input_hz_layout_zoom_radio.addWidget(self.input_zoom_inc_button)


        self.gridLayout_NhapKho.addWidget(self.widget_zoom_tabin, 1, 17, 1, 1)

        self.input_model_widget = QWidget(self.widget_nhap_tabin)
        self.input_model_widget.setObjectName(u"input_model_widget")
        self.input_storage_location_widget_8 = QHBoxLayout(self.input_model_widget)
        self.input_storage_location_widget_8.setSpacing(0)
        self.input_storage_location_widget_8.setObjectName(u"input_storage_location_widget_8")
        self.input_storage_location_widget_8.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(self.input_model_widget, 4, 11, 1, 1)

        self.input_process_widget = QWidget(self.widget_nhap_tabin)
        self.input_process_widget.setObjectName(u"input_process_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.input_process_widget.sizePolicy().hasHeightForWidth())
        self.input_process_widget.setSizePolicy(sizePolicy6)
        self.input_storage_location_widget_4 = QHBoxLayout(self.input_process_widget)
        self.input_storage_location_widget_4.setSpacing(0)
        self.input_storage_location_widget_4.setObjectName(u"input_storage_location_widget_4")
        self.input_storage_location_widget_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(self.input_process_widget, 2, 11, 1, 1)

        self.input_groups_widget = QWidget(self.widget_nhap_tabin)
        self.input_groups_widget.setObjectName(u"input_groups_widget")
        self.input_storage_location_widget_10 = QHBoxLayout(self.input_groups_widget)
        self.input_storage_location_widget_10.setSpacing(0)
        self.input_storage_location_widget_10.setObjectName(u"input_storage_location_widget_10")
        self.input_storage_location_widget_10.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(self.input_groups_widget, 3, 11, 1, 1)

        self.input_search_size_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_size_checkBox.setObjectName(u"input_search_size_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_size_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_size_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_size_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_size_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_size_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_size_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_size_checkBox, 4, 1, 1, 1)

        self.input_search_storage_location_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_storage_location_checkBox.setObjectName(u"input_search_storage_location_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_storage_location_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_storage_location_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_storage_location_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_storage_location_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_storage_location_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_storage_location_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_storage_location_checkBox, 1, 1, 1, 1)

        self.input_storage_location_labels = QLabel(self.widget_nhap_tabin)
        self.input_storage_location_labels.setObjectName(u"input_storage_location_labels")
        sizePolicy4.setHeightForWidth(self.input_storage_location_labels.sizePolicy().hasHeightForWidth())
        self.input_storage_location_labels.setSizePolicy(sizePolicy4)
        self.input_storage_location_labels.setFont(font1)

        self.gridLayout_NhapKho.addWidget(self.input_storage_location_labels, 1, 0, 1, 1)

        self.input_note_textedit = QTextEdit(self.widget_nhap_tabin)
        self.input_note_textedit.setObjectName(u"input_note_textedit")
        self.input_note_textedit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #4a90e2;\n"
"}")
        self.input_note_textedit.setFrameShape(QFrame.StyledPanel)
        self.input_note_textedit.setFrameShadow(QFrame.Plain)

        self.gridLayout_NhapKho.addWidget(self.input_note_textedit, 2, 15, 4, 2)

        self.input_images_label = QLabel(self.widget_nhap_tabin)
        self.input_images_label.setObjectName(u"input_images_label")
        self.input_images_label.setEnabled(True)
        self.input_images_label.setMinimumSize(QSize(280, 200))
        self.input_images_label.setMaximumSize(QSize(280, 16777215))
        self.input_images_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_images_label.setStyleSheet(u"/* QLabel styling */\n"
"QLabel {\n"
"    background-color: #ffffff; /* N\u1ec1n tr\u1eafng t\u1ea1o c\u1ea3m gi\u00e1c chuy\u00ean nghi\u1ec7p */\n"
"    border: 2px solid #e0e0e0; /* Vi\u1ec1n m\u1ecfng v\u00e0 nh\u1eb9 nh\u00e0ng */\n"
"    border-radius: 10px; /* G\u00f3c bo v\u1eeba ph\u1ea3i */\n"
"    padding: 6px; /* \u0110\u1ec7m \u0111\u1ec1u h\u01a1n */\n"
"    color: #444444; /* M\u00e0u ch\u1eef trung t\u00ednh, d\u1ec5 \u0111\u1ecdc */\n"
"}\n"
"/* Hi\u1ec7u \u1ee9ng khi hover */\n"
"QLabel:hover {\n"
"    background-color: #f7faff; /* Thay \u0111\u1ed5i n\u1ec1n nh\u1eb9 khi hover */\n"
"}\n"
"\n"
"")
        self.input_images_label.setFrameShape(QFrame.StyledPanel)
        self.input_images_label.setPixmap(QPixmap(u":/icon/images/icon/no_image.png"))
        self.input_images_label.setScaledContents(True)
        self.input_images_label.setAlignment(Qt.AlignCenter)
        self.input_images_label.setWordWrap(False)

        self.gridLayout_NhapKho.addWidget(self.input_images_label, 1, 17, 5, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.input_note_labels = QLabel(self.widget_nhap_tabin)
        self.input_note_labels.setObjectName(u"input_note_labels")
        sizePolicy4.setHeightForWidth(self.input_note_labels.sizePolicy().hasHeightForWidth())
        self.input_note_labels.setSizePolicy(sizePolicy4)
        self.input_note_labels.setFont(font1)
        self.input_note_labels.setTextFormat(Qt.AutoText)
        self.input_note_labels.setScaledContents(False)
        self.input_note_labels.setWordWrap(False)
        self.input_note_labels.setMargin(7)

        self.horizontalLayout_8.addWidget(self.input_note_labels)

        self.input_search_note_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_note_checkBox.setObjectName(u"input_search_note_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_note_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_note_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_note_checkBox.setMinimumSize(QSize(22, 24))
        self.input_search_note_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_note_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_note_checkBox.setChecked(False)

        self.horizontalLayout_8.addWidget(self.input_search_note_checkBox)

        self.input_note_fillter_combobox = QComboBox(self.widget_nhap_tabin)
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.addItem("")
        self.input_note_fillter_combobox.setObjectName(u"input_note_fillter_combobox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.input_note_fillter_combobox.sizePolicy().hasHeightForWidth())
        self.input_note_fillter_combobox.setSizePolicy(sizePolicy7)
        self.input_note_fillter_combobox.setFont(font)
        self.input_note_fillter_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_note_fillter_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 12px;\n"
"    color: #ff3907;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.input_note_fillter_combobox.setEditable(False)

        self.horizontalLayout_8.addWidget(self.input_note_fillter_combobox)

        self.input_paste_button = QPushButton(self.widget_nhap_tabin)
        self.input_paste_button.setObjectName(u"input_paste_button")
        self.input_paste_button.setSizeIncrement(QSize(0, 40))
        self.input_paste_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_paste_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #157117;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        self.input_paste_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.input_paste_button)


        self.gridLayout_NhapKho.addLayout(self.horizontalLayout_8, 1, 15, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, -1, -1, -1)
        self.input_storage_location_combobox = QComboBox(self.widget_nhap_tabin)
        self.input_storage_location_combobox.setObjectName(u"input_storage_location_combobox")
        sizePolicy3.setHeightForWidth(self.input_storage_location_combobox.sizePolicy().hasHeightForWidth())
        self.input_storage_location_combobox.setSizePolicy(sizePolicy3)
        self.input_storage_location_combobox.setMinimumSize(QSize(60, 0))
        self.input_storage_location_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_storage_location_combobox.setLayoutDirection(Qt.LeftToRight)
        self.input_storage_location_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.input_storage_location_combobox.setEditable(False)

        self.horizontalLayout_34.addWidget(self.input_storage_location_combobox)

        self.input_search_component_id_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_component_id_checkBox.setObjectName(u"input_search_component_id_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_component_id_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_component_id_checkBox.setMinimumSize(QSize(22, 24))
        self.input_search_component_id_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_component_id_checkBox.setChecked(False)

        self.horizontalLayout_34.addWidget(self.input_search_component_id_checkBox)

        self.input_component_id_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_component_id_lineedit.setObjectName(u"input_component_id_lineedit")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.input_component_id_lineedit.sizePolicy().hasHeightForWidth())
        self.input_component_id_lineedit.setSizePolicy(sizePolicy8)
        self.input_component_id_lineedit.setMinimumSize(QSize(150, 0))
        self.input_component_id_lineedit.setFont(font)
        self.input_component_id_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_component_id_lineedit.setMaxLength(8)
        self.input_component_id_lineedit.setAlignment(Qt.AlignCenter)
        self.input_component_id_lineedit.setClearButtonEnabled(True)

        self.horizontalLayout_34.addWidget(self.input_component_id_lineedit)

        self.input_check_id_auto_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_check_id_auto_checkBox.setObjectName(u"input_check_id_auto_checkBox")
        sizePolicy3.setHeightForWidth(self.input_check_id_auto_checkBox.sizePolicy().hasHeightForWidth())
        self.input_check_id_auto_checkBox.setSizePolicy(sizePolicy3)
        self.input_check_id_auto_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/check_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/check_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_check_id_auto_checkBox.setIconSize(QSize(16, 16))
        self.input_check_id_auto_checkBox.setChecked(False)

        self.horizontalLayout_34.addWidget(self.input_check_id_auto_checkBox)


        self.gridLayout_NhapKho.addLayout(self.horizontalLayout_34, 1, 3, 1, 1)

        self.input_qty_horizontalLayout = QHBoxLayout()
        self.input_qty_horizontalLayout.setSpacing(0)
        self.input_qty_horizontalLayout.setObjectName(u"input_qty_horizontalLayout")
        self.input_status_combobox = QComboBox(self.widget_nhap_tabin)
        self.input_status_combobox.setObjectName(u"input_status_combobox")
        self.input_status_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_status_combobox.setLayoutDirection(Qt.LeftToRight)
        self.input_status_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.input_status_combobox.setEditable(False)

        self.input_qty_horizontalLayout.addWidget(self.input_status_combobox)

        self.input_quantity_labels = QLabel(self.widget_nhap_tabin)
        self.input_quantity_labels.setObjectName(u"input_quantity_labels")
        sizePolicy4.setHeightForWidth(self.input_quantity_labels.sizePolicy().hasHeightForWidth())
        self.input_quantity_labels.setSizePolicy(sizePolicy4)
        self.input_quantity_labels.setFont(font1)
        self.input_quantity_labels.setMargin(7)

        self.input_qty_horizontalLayout.addWidget(self.input_quantity_labels)

        self.input_quantity_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_quantity_lineedit.setObjectName(u"input_quantity_lineedit")
        sizePolicy8.setHeightForWidth(self.input_quantity_lineedit.sizePolicy().hasHeightForWidth())
        self.input_quantity_lineedit.setSizePolicy(sizePolicy8)
        self.input_quantity_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_quantity_lineedit.setAlignment(Qt.AlignCenter)

        self.input_qty_horizontalLayout.addWidget(self.input_quantity_lineedit)

        self.input_unit_combobox = QComboBox(self.widget_nhap_tabin)
        self.input_unit_combobox.setObjectName(u"input_unit_combobox")
        sizePolicy3.setHeightForWidth(self.input_unit_combobox.sizePolicy().hasHeightForWidth())
        self.input_unit_combobox.setSizePolicy(sizePolicy3)
        self.input_unit_combobox.setMinimumSize(QSize(60, 0))
        self.input_unit_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_unit_combobox.setLayoutDirection(Qt.LeftToRight)
        self.input_unit_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.input_unit_combobox.setEditable(False)

        self.input_qty_horizontalLayout.addWidget(self.input_unit_combobox)


        self.gridLayout_NhapKho.addLayout(self.input_qty_horizontalLayout, 2, 3, 1, 1)

        self.input_size_labels = QLabel(self.widget_nhap_tabin)
        self.input_size_labels.setObjectName(u"input_size_labels")
        sizePolicy4.setHeightForWidth(self.input_size_labels.sizePolicy().hasHeightForWidth())
        self.input_size_labels.setSizePolicy(sizePolicy4)
        self.input_size_labels.setFont(font1)
        self.input_size_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(self.input_size_labels, 4, 0, 1, 1)

        self.input_process_labels = QLabel(self.widget_nhap_tabin)
        self.input_process_labels.setObjectName(u"input_process_labels")
        sizePolicy4.setHeightForWidth(self.input_process_labels.sizePolicy().hasHeightForWidth())
        self.input_process_labels.setSizePolicy(sizePolicy4)
        self.input_process_labels.setFont(font1)
        self.input_process_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(self.input_process_labels, 2, 6, 1, 1)

        self.input_search_component_name_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_component_name_checkBox.setObjectName(u"input_search_component_name_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_component_name_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_component_name_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_component_name_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_component_name_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_component_name_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_component_name_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_component_name_checkBox, 1, 8, 1, 1)

        self.input_component_name_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_component_name_lineedit.setObjectName(u"input_component_name_lineedit")
        self.input_component_name_lineedit.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.input_component_name_lineedit.sizePolicy().hasHeightForWidth())
        self.input_component_name_lineedit.setSizePolicy(sizePolicy8)
        self.input_component_name_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_component_name_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho.addWidget(self.input_component_name_lineedit, 1, 11, 1, 1)

        self.input_groups_labels = QLabel(self.widget_nhap_tabin)
        self.input_groups_labels.setObjectName(u"input_groups_labels")
        sizePolicy4.setHeightForWidth(self.input_groups_labels.sizePolicy().hasHeightForWidth())
        self.input_groups_labels.setSizePolicy(sizePolicy4)
        self.input_groups_labels.setFont(font1)
        self.input_groups_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(self.input_groups_labels, 3, 6, 1, 1)

        self.input_search_process_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_process_checkBox.setObjectName(u"input_search_process_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_process_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_process_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_process_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_process_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_process_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_process_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_process_checkBox, 2, 8, 1, 1)

        self.input_model_labels = QLabel(self.widget_nhap_tabin)
        self.input_model_labels.setObjectName(u"input_model_labels")
        sizePolicy4.setHeightForWidth(self.input_model_labels.sizePolicy().hasHeightForWidth())
        self.input_model_labels.setSizePolicy(sizePolicy4)
        self.input_model_labels.setFont(font1)
        self.input_model_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(self.input_model_labels, 4, 6, 1, 1)

        self.input_search_model_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_model_checkBox.setObjectName(u"input_search_model_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_model_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_model_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_model_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_model_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_model_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_model_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_model_checkBox, 4, 8, 1, 1)

        self.input_search_groups_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_groups_checkBox.setObjectName(u"input_search_groups_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_groups_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_groups_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_groups_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_groups_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_groups_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_groups_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_groups_checkBox, 3, 8, 1, 1)

        self.input_material_labels = QLabel(self.widget_nhap_tabin)
        self.input_material_labels.setObjectName(u"input_material_labels")
        sizePolicy4.setHeightForWidth(self.input_material_labels.sizePolicy().hasHeightForWidth())
        self.input_material_labels.setSizePolicy(sizePolicy4)
        self.input_material_labels.setFont(font1)
        self.input_material_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(self.input_material_labels, 3, 0, 1, 1)

        self.input_search_material_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_material_checkBox.setObjectName(u"input_search_material_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_material_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_material_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_material_checkBox.setMinimumSize(QSize(22, 22))
        self.input_search_material_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_material_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_material_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_material_checkBox, 3, 1, 1, 1)

        self.input_desinvoice_labels = QLabel(self.widget_nhap_tabin)
        self.input_desinvoice_labels.setObjectName(u"input_desinvoice_labels")
        sizePolicy4.setHeightForWidth(self.input_desinvoice_labels.sizePolicy().hasHeightForWidth())
        self.input_desinvoice_labels.setSizePolicy(sizePolicy4)
        self.input_desinvoice_labels.setFont(font1)
        self.input_desinvoice_labels.setMargin(7)

        self.gridLayout_NhapKho.addWidget(self.input_desinvoice_labels, 5, 6, 1, 1)

        self.input_search_desinvoice_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_desinvoice_checkBox.setObjectName(u"input_search_desinvoice_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_desinvoice_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_desinvoice_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_desinvoice_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_desinvoice_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_desinvoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_desinvoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_desinvoice_checkBox, 5, 8, 1, 1)

        self.input_desinvoice_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_desinvoice_lineedit.setObjectName(u"input_desinvoice_lineedit")
        self.input_desinvoice_lineedit.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.input_desinvoice_lineedit.sizePolicy().hasHeightForWidth())
        self.input_desinvoice_lineedit.setSizePolicy(sizePolicy8)
        self.input_desinvoice_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_desinvoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho.addWidget(self.input_desinvoice_lineedit, 5, 11, 1, 1)

        self.input_invoice_labels = QLabel(self.widget_nhap_tabin)
        self.input_invoice_labels.setObjectName(u"input_invoice_labels")
        sizePolicy4.setHeightForWidth(self.input_invoice_labels.sizePolicy().hasHeightForWidth())
        self.input_invoice_labels.setSizePolicy(sizePolicy4)
        self.input_invoice_labels.setFont(font1)
        self.input_invoice_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(self.input_invoice_labels, 5, 0, 1, 1)

        self.input_search_invoice_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_invoice_checkBox.setObjectName(u"input_search_invoice_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_invoice_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_invoice_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_invoice_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_invoice_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_invoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_invoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_invoice_checkBox, 5, 1, 1, 1)

        self.input_invoice_lineedit = QLineEdit(self.widget_nhap_tabin)
        self.input_invoice_lineedit.setObjectName(u"input_invoice_lineedit")
        self.input_invoice_lineedit.setEnabled(True)
        self.input_invoice_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.input_invoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho.addWidget(self.input_invoice_lineedit, 5, 3, 1, 1)

        self.input_status_labels = QLabel(self.widget_nhap_tabin)
        self.input_status_labels.setObjectName(u"input_status_labels")
        sizePolicy4.setHeightForWidth(self.input_status_labels.sizePolicy().hasHeightForWidth())
        self.input_status_labels.setSizePolicy(sizePolicy4)
        self.input_status_labels.setFont(font1)
        self.input_status_labels.setMargin(0)

        self.gridLayout_NhapKho.addWidget(self.input_status_labels, 2, 0, 1, 1)

        self.input_search_status_checkBox = QCheckBox(self.widget_nhap_tabin)
        self.input_search_status_checkBox.setObjectName(u"input_search_status_checkBox")
        sizePolicy3.setHeightForWidth(self.input_search_status_checkBox.sizePolicy().hasHeightForWidth())
        self.input_search_status_checkBox.setSizePolicy(sizePolicy3)
        self.input_search_status_checkBox.setMinimumSize(QSize(22, 20))
        self.input_search_status_checkBox.setMaximumSize(QSize(22, 24))
        self.input_search_status_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_search_status_checkBox.setChecked(False)

        self.gridLayout_NhapKho.addWidget(self.input_search_status_checkBox, 2, 1, 1, 1)

        self.input_material_widget = QWidget(self.widget_nhap_tabin)
        self.input_material_widget.setObjectName(u"input_material_widget")
        self.input_material_widget.setStyleSheet(u"")
        self.input_storage_location_widget_5 = QHBoxLayout(self.input_material_widget)
        self.input_storage_location_widget_5.setSpacing(0)
        self.input_storage_location_widget_5.setObjectName(u"input_storage_location_widget_5")
        self.input_storage_location_widget_5.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho.addWidget(self.input_material_widget, 3, 3, 1, 1)

        self.input_images_label.raise_()
        self.widget_zoom_tabin.raise_()
        self.input_note_textedit.raise_()
        self.input_search_storage_location_checkBox.raise_()
        self.input_storage_location_labels.raise_()
        self.input_size_labels.raise_()
        self.input_search_size_checkBox.raise_()
        self.input_component_name_labels.raise_()
        self.input_search_component_name_checkBox.raise_()
        self.input_component_name_lineedit.raise_()
        self.input_process_labels.raise_()
        self.input_search_process_checkBox.raise_()
        self.input_process_widget.raise_()
        self.input_groups_labels.raise_()
        self.input_search_groups_checkBox.raise_()
        self.input_groups_widget.raise_()
        self.input_model_labels.raise_()
        self.input_search_model_checkBox.raise_()
        self.input_model_widget.raise_()
        self.input_material_labels.raise_()
        self.input_search_material_checkBox.raise_()
        self.input_desinvoice_labels.raise_()
        self.input_search_desinvoice_checkBox.raise_()
        self.input_desinvoice_lineedit.raise_()
        self.input_invoice_labels.raise_()
        self.input_search_invoice_checkBox.raise_()
        self.input_invoice_lineedit.raise_()
        self.input_status_labels.raise_()
        self.input_search_status_checkBox.raise_()
        self.input_material_widget.raise_()

        self.verticalLayout_5.addWidget(self.widget_nhap_tabin)

        self.widget_button_tabin = QWidget(self.tabInput)
        self.widget_button_tabin.setObjectName(u"widget_button_tabin")
        self.inputButtonLayout = QHBoxLayout(self.widget_button_tabin)
        self.inputButtonLayout.setSpacing(5)
        self.inputButtonLayout.setObjectName(u"inputButtonLayout")
        self.inputButtonLayout.setContentsMargins(5, 5, 5, 5)
        self.input_filter_component_id_checkBox = QCheckBox(self.widget_button_tabin)
        self.input_filter_component_id_checkBox.setObjectName(u"input_filter_component_id_checkBox")
        sizePolicy3.setHeightForWidth(self.input_filter_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.input_filter_component_id_checkBox.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setBold(False)
        self.input_filter_component_id_checkBox.setFont(font5)
        self.input_filter_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 32px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 32px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/filter_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/filter_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.input_filter_component_id_checkBox.setChecked(False)

        self.inputButtonLayout.addWidget(self.input_filter_component_id_checkBox)

        self.input_new_button = QPushButton(self.widget_button_tabin)
        self.input_new_button.setObjectName(u"input_new_button")
        sizePolicy2.setHeightForWidth(self.input_new_button.sizePolicy().hasHeightForWidth())
        self.input_new_button.setSizePolicy(sizePolicy2)
        self.input_new_button.setMinimumSize(QSize(0, 40))
        self.input_new_button.setMaximumSize(QSize(16777215, 40))
        self.input_new_button.setSizeIncrement(QSize(0, 40))
        self.input_new_button.setFont(font1)
        self.input_new_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_new_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"	font-weight: bold;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/images/icon/New.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_new_button.setIcon(icon4)
        self.input_new_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_new_button)

        self.input_edit_button = QPushButton(self.widget_button_tabin)
        self.input_edit_button.setObjectName(u"input_edit_button")
        sizePolicy2.setHeightForWidth(self.input_edit_button.sizePolicy().hasHeightForWidth())
        self.input_edit_button.setSizePolicy(sizePolicy2)
        self.input_edit_button.setMinimumSize(QSize(0, 40))
        self.input_edit_button.setMaximumSize(QSize(16777215, 40))
        self.input_edit_button.setSizeIncrement(QSize(0, 40))
        self.input_edit_button.setFont(font)
        self.input_edit_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_edit_button.setStyleSheet(u"/* QPushButton - Modern style */\n"
"QPushButton {\n"
"    background-color: #ffd700;        /* M\u00e0u v\u00e0ng m\u1ec1m h\u01a1n */\n"
"    border: 1px solid #e6c200;        /* Vi\u1ec1n nh\u1eb9 \u0111\u1ec3 t\u1ea1o chi\u1ec1u s\u00e2u */\n"
"    border-radius: 8px;               /* Bo g\u00f3c nh\u1eb9 nh\u00e0ng */\n"
"    color: #222;                      /* M\u00e0u ch\u1eef t\u1ed1i h\u01a1n \u0111\u1ec3 d\u1ec5 \u0111\u1ecdc */\n"
"    font-size: 12px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffc400;        /* V\u00e0ng \u0111\u1eadm khi hover */\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e6b800;        /* M\u00e0u nh\u1ea5n m\u1ea1nh h\u01a1n */\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    color: #aaa;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/images/icon/Edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_edit_button.setIcon(icon5)
        self.input_edit_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_edit_button)

        self.input_delete_button = QPushButton(self.widget_button_tabin)
        self.input_delete_button.setObjectName(u"input_delete_button")
        sizePolicy2.setHeightForWidth(self.input_delete_button.sizePolicy().hasHeightForWidth())
        self.input_delete_button.setSizePolicy(sizePolicy2)
        self.input_delete_button.setMinimumSize(QSize(0, 40))
        self.input_delete_button.setMaximumSize(QSize(16777215, 40))
        self.input_delete_button.setSizeIncrement(QSize(0, 40))
        self.input_delete_button.setFont(font1)
        self.input_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_delete_button.setStyleSheet(u"/* QPushButton - Red alert style */\n"
"QPushButton {\n"
"    background-color: #e53935;       /* \u0110\u1ecf c\u1ea3nh b\u00e1o hi\u1ec7n \u0111\u1ea1i */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f;       /* \u0110\u1ecf \u0111\u1eadm h\u01a1n khi hover */\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b71c1c;       /* \u0110\u1ecf t\u1ed1i khi nh\u1ea5n */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #e0e0e0;\n"
"    color: #999;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/images/icon/Delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_delete_button.setIcon(icon6)
        self.input_delete_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_delete_button)

        self.input_export_button = QPushButton(self.widget_button_tabin)
        self.input_export_button.setObjectName(u"input_export_button")
        sizePolicy2.setHeightForWidth(self.input_export_button.sizePolicy().hasHeightForWidth())
        self.input_export_button.setSizePolicy(sizePolicy2)
        self.input_export_button.setMinimumSize(QSize(0, 40))
        self.input_export_button.setMaximumSize(QSize(16777215, 40))
        self.input_export_button.setSizeIncrement(QSize(0, 40))
        self.input_export_button.setFont(font1)
        self.input_export_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_export_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"	font-weight: bold;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icon/images/icon/export_excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_export_button.setIcon(icon7)
        self.input_export_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_export_button)

        self.input_down_button = QPushButton(self.widget_button_tabin)
        self.input_down_button.setObjectName(u"input_down_button")
        sizePolicy2.setHeightForWidth(self.input_down_button.sizePolicy().hasHeightForWidth())
        self.input_down_button.setSizePolicy(sizePolicy2)
        self.input_down_button.setMinimumSize(QSize(0, 40))
        self.input_down_button.setMaximumSize(QSize(16777215, 40))
        self.input_down_button.setSizeIncrement(QSize(0, 40))
        self.input_down_button.setFont(font1)
        self.input_down_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_down_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #08e7f6;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-size: 12px;\n"
"	font-weight: bold;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #08d1f6;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #08d1f6;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icon/images/icon/down_image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_down_button.setIcon(icon8)
        self.input_down_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_down_button)

        self.input_search_button = QPushButton(self.widget_button_tabin)
        self.input_search_button.setObjectName(u"input_search_button")
        sizePolicy2.setHeightForWidth(self.input_search_button.sizePolicy().hasHeightForWidth())
        self.input_search_button.setSizePolicy(sizePolicy2)
        self.input_search_button.setMinimumSize(QSize(0, 40))
        self.input_search_button.setMaximumSize(QSize(16777215, 40))
        self.input_search_button.setSizeIncrement(QSize(0, 40))
        self.input_search_button.setFont(font1)
        self.input_search_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
"QPushButton {\n"
"    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
"    font-size: 15px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #d3d3d3;\n"
"    color: #888;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icon/images/icon/Search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.input_search_button.setIcon(icon9)
        self.input_search_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout.addWidget(self.input_search_button)


        self.verticalLayout_5.addWidget(self.widget_button_tabin)

        self.input_data_tablewidget = QTableWidget(self.tabInput)
        if (self.input_data_tablewidget.columnCount() < 3):
            self.input_data_tablewidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.input_data_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.input_data_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.input_data_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.input_data_tablewidget.setObjectName(u"input_data_tablewidget")
        self.input_data_tablewidget.setStyleSheet(u"/* QTableWidget styling */\n"
"QTableWidget {\n"
"    background-color: #f9fbfd; /* N\u1ec1n b\u1ea3ng xanh nh\u1ea1t */\n"
"    border: 1px solid #d3d9e3; /* \u0110\u01b0\u1eddng vi\u1ec1n nh\u1eb9 */\n"
"    font-size: 12px; /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    color: #333333; /* M\u00e0u ch\u1eef ch\u00ednh */\n"
"    gridline-color: #e7edf3; /* M\u00e0u \u0111\u01b0\u1eddng l\u01b0\u1edbi nh\u1ea1t */\n"
"    selection-background-color: #3b82cc; /* M\u00e0u n\u1ec1n khi ch\u1ecdn */\n"
"    selection-color: #ffffff; /* M\u00e0u ch\u1eef khi ch\u1ecdn */\n"
"    outline: none; /* Lo\u1ea1i b\u1ecf vi\u1ec1n s\u00e1ng khi focus */\n"
"}\n"
"\n"
"/* Ti\u00eau \u0111\u1ec1 c\u1ed9t */\n"
"QHeaderView::section {\n"
"    background-color: #e5effb; /* N\u1ec1n ti\u00eau \u0111\u1ec1 xanh nh\u1ea1t */\n"
"    color: #4a4a4a; /* M\u00e0u ch\u1eef ti\u00eau \u0111\u1ec1 */\n"
"    padding: 10px;\n"
"    border: 1px solid #d3d9e3; /* Vi\u1ec1n gi\u1eefa c\u00e1c ti\u00eau \u0111\u1ec1 */\n"
"    font-size"
                        ": 12px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* C\u00e1c \u00f4 */\n"
"QTableWidget::item {\n"
"    background-color: #ffffff; /* N\u1ec1n \u00f4 m\u1eb7c \u0111\u1ecbnh */\n"
"    border: none;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #333333; /* M\u00e0u ch\u1eef */\n"
"}\n"
"\n"
"/* \u00d4 xen k\u1ebd */\n"
"QTableWidget::item:alternate {\n"
"    background-color: #f4f8fc; /* N\u1ec1n xen k\u1ebd xanh nh\u1eb9 */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng hover */\n"
"QTableWidget::item:hover {\n"
"    background-color: #dceaf7; /* M\u00e0u hover xanh nh\u1ea1t */\n"
"    color: #333333; /* Ch\u1eef v\u1eabn d\u1ec5 \u0111\u1ecdc */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng hover n\u1ed5i b\u1eadt to\u00e0n d\u00f2ng */\n"
"QTableWidget::row:hover {\n"
"    background-color: #cce1f4; /* N\u1ec1n hover n\u1ed5i b\u1eadt c\u1ea3 d\u00f2ng */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi ch\u1ecdn */\n"
"QTableWidget::item:selected {\n"
"    background-color: #3b82cc; /* M"
                        "\u00e0u n\u1ec1n xanh \u0111\u1eadm khi ch\u1ecdn */\n"
"    color: #ffffff; /* M\u00e0u ch\u1eef tr\u1eafng khi ch\u1ecdn */\n"
"}\n"
"\n"
"/* Scrollbar */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f4f8fc; /* N\u1ec1n thanh cu\u1ed9n xanh nh\u1ea1t */\n"
"    width: 12px;\n"
"    margin: 2px 0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3b82cc; /* Thanh tr\u01b0\u1ee3t xanh \u0111\u1eadm */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #2f6fa5; /* Thanh tr\u01b0\u1ee3t khi hover */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* G\u00f3c cu\u1ed9n */\n"
"QScrollBar::corner {\n"
"    background: #ffffff;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi focus */\n"
"QTableWidget:focus {\n"
"    border: 1px solid #3b82cc; /* Vi\u1ec1n xanh \u0111\u1eadm khi focus */\n"
"}\n"
"")
        self.input_data_tablewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.input_data_tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.input_data_tablewidget.setSortingEnabled(False)

        self.verticalLayout_5.addWidget(self.input_data_tablewidget)

        icon10 = QIcon()
        icon10.addFile(u":/icon/images/icon/stock_entry_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabInput, icon10, "")
        self.tabOutput = QWidget()
        self.tabOutput.setObjectName(u"tabOutput")
        self.verticalLayout_6 = QVBoxLayout(self.tabOutput)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.widget_nhap_tabout = QWidget(self.tabOutput)
        self.widget_nhap_tabout.setObjectName(u"widget_nhap_tabout")
        self.widget_nhap_tabout.setMaximumSize(QSize(16777215, 220))
        self.gridLayout_4 = QGridLayout(self.widget_nhap_tabout)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.widget_zoom_tabout = QWidget(self.widget_nhap_tabout)
        self.widget_zoom_tabout.setObjectName(u"widget_zoom_tabout")
        self.output_hz_layout_zoom_radio = QHBoxLayout(self.widget_zoom_tabout)
        self.output_hz_layout_zoom_radio.setSpacing(5)
        self.output_hz_layout_zoom_radio.setObjectName(u"output_hz_layout_zoom_radio")
        self.output_hz_layout_zoom_radio.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.output_hz_layout_zoom_radio.setContentsMargins(5, 5, 5, 5)
        self.output_zoom_dec_button = QPushButton(self.widget_zoom_tabout)
        self.output_zoom_dec_button.setObjectName(u"output_zoom_dec_button")
        sizePolicy3.setHeightForWidth(self.output_zoom_dec_button.sizePolicy().hasHeightForWidth())
        self.output_zoom_dec_button.setSizePolicy(sizePolicy3)
        self.output_zoom_dec_button.setMinimumSize(QSize(28, 28))
        self.output_zoom_dec_button.setMaximumSize(QSize(28, 28))
        self.output_zoom_dec_button.setSizeIncrement(QSize(0, 40))
        self.output_zoom_dec_button.setFont(font)
        self.output_zoom_dec_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.output_zoom_dec_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    padding: 8px 16px; /* \u0110i\u1ec1u ch\u1ec9nh padding \u0111\u1ec3 n\u00fat c\u00f3 kh\u00f4ng gian tho\u1ea3i m\u00e1i h\u01a1n */\n"
"    border-radius: 11px; /* Bo tr\u00f2n g\u00f3c */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"")
        self.output_zoom_dec_button.setIcon(icon2)
        self.output_zoom_dec_button.setIconSize(QSize(24, 24))

        self.output_hz_layout_zoom_radio.addWidget(self.output_zoom_dec_button)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.output_hz_layout_zoom_radio.addItem(self.horizontalSpacer_17)

        self.output_zoom_inc_button = QPushButton(self.widget_zoom_tabout)
        self.output_zoom_inc_button.setObjectName(u"output_zoom_inc_button")
        sizePolicy3.setHeightForWidth(self.output_zoom_inc_button.sizePolicy().hasHeightForWidth())
        self.output_zoom_inc_button.setSizePolicy(sizePolicy3)
        self.output_zoom_inc_button.setMinimumSize(QSize(28, 28))
        self.output_zoom_inc_button.setMaximumSize(QSize(28, 28))
        self.output_zoom_inc_button.setSizeIncrement(QSize(0, 40))
        self.output_zoom_inc_button.setFont(font)
        self.output_zoom_inc_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.output_zoom_inc_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    padding: 8px 16px; /* \u0110i\u1ec1u ch\u1ec9nh padding \u0111\u1ec3 n\u00fat c\u00f3 kh\u00f4ng gian tho\u1ea3i m\u00e1i h\u01a1n */\n"
"    border-radius: 11px; /* Bo tr\u00f2n g\u00f3c */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"")
        self.output_zoom_inc_button.setIcon(icon3)
        self.output_zoom_inc_button.setIconSize(QSize(24, 24))

        self.output_hz_layout_zoom_radio.addWidget(self.output_zoom_inc_button)


        self.gridLayout_4.addWidget(self.widget_zoom_tabout, 1, 9, 1, 1)

        self.output_inventory_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_inventory_label_2.setObjectName(u"output_inventory_label_2")
        self.output_inventory_label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.output_inventory_label_2, 5, 0, 1, 1)

        self.output_quantity_label = QLabel(self.widget_nhap_tabout)
        self.output_quantity_label.setObjectName(u"output_quantity_label")
        self.output_quantity_label.setFont(font1)

        self.gridLayout_4.addWidget(self.output_quantity_label, 4, 0, 1, 1)

        self.output_note_textedit = QTextEdit(self.widget_nhap_tabout)
        self.output_note_textedit.setObjectName(u"output_note_textedit")
        self.output_note_textedit.setMinimumSize(QSize(250, 0))
        self.output_note_textedit.setFont(font5)
        self.output_note_textedit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #4a90e2;\n"
"}")
        self.output_note_textedit.setFrameShape(QFrame.StyledPanel)
        self.output_note_textedit.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.output_note_textedit, 2, 8, 4, 1)

        self.output_size_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_size_label_2.setObjectName(u"output_size_label_2")
        self.output_size_label_2.setFont(font1)
        self.output_size_label_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_size_label_2, 1, 4, 1, 1)

        self.output_images_label = QLabel(self.widget_nhap_tabout)
        self.output_images_label.setObjectName(u"output_images_label")
        self.output_images_label.setMinimumSize(QSize(280, 0))
        self.output_images_label.setMaximumSize(QSize(280, 16777215))
        self.output_images_label.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.output_images_label.setStyleSheet(u"/* QLabel styling */\n"
"QLabel {\n"
"    background-color: #ffffff; /* N\u1ec1n tr\u1eafng t\u1ea1o c\u1ea3m gi\u00e1c chuy\u00ean nghi\u1ec7p */\n"
"    border: 2px solid #e0e0e0; /* Vi\u1ec1n m\u1ecfng v\u00e0 nh\u1eb9 nh\u00e0ng */\n"
"    border-radius: 10px; /* G\u00f3c bo v\u1eeba ph\u1ea3i */\n"
"    padding: 5px; /* \u0110\u1ec7m \u0111\u1ec1u h\u01a1n */\n"
"    color: #444444; /* M\u00e0u ch\u1eef trung t\u00ednh, d\u1ec5 \u0111\u1ecdc */\n"
"}")
        self.output_images_label.setFrameShape(QFrame.StyledPanel)
        self.output_images_label.setPixmap(QPixmap(u":/icon/images/icon/no_image.png"))
        self.output_images_label.setScaledContents(True)
        self.output_images_label.setWordWrap(False)

        self.gridLayout_4.addWidget(self.output_images_label, 1, 9, 5, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.output_storage_location_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_storage_location_label_2.setObjectName(u"output_storage_location_label_2")
        self.output_storage_location_label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.output_storage_location_label_2)

        self.output_search_component_id_checkBox = QCheckBox(self.widget_nhap_tabout)
        self.output_search_component_id_checkBox.setObjectName(u"output_search_component_id_checkBox")
        sizePolicy3.setHeightForWidth(self.output_search_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.output_search_component_id_checkBox.setSizePolicy(sizePolicy3)
        self.output_search_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.output_search_component_id_checkBox.setChecked(False)

        self.horizontalLayout_4.addWidget(self.output_search_component_id_checkBox)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.output_storage_location_label = QLabel(self.widget_nhap_tabout)
        self.output_storage_location_label.setObjectName(u"output_storage_location_label")
        sizePolicy8.setHeightForWidth(self.output_storage_location_label.sizePolicy().hasHeightForWidth())
        self.output_storage_location_label.setSizePolicy(sizePolicy8)
        self.output_storage_location_label.setMinimumSize(QSize(0, 0))
        self.output_storage_location_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_storage_location_label.setAlignment(Qt.AlignCenter)
        self.output_storage_location_label.setMargin(7)

        self.horizontalLayout_5.addWidget(self.output_storage_location_label)

        self.output_component_id_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_component_id_lineedit.setObjectName(u"output_component_id_lineedit")
        sizePolicy8.setHeightForWidth(self.output_component_id_lineedit.sizePolicy().hasHeightForWidth())
        self.output_component_id_lineedit.setSizePolicy(sizePolicy8)
        self.output_component_id_lineedit.setMinimumSize(QSize(0, 30))
        self.output_component_id_lineedit.setFont(font)
        self.output_component_id_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.output_component_id_lineedit.setMaxLength(8)
        self.output_component_id_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.output_component_id_lineedit)

        self.output_check_id_auto_checkBox = QCheckBox(self.widget_nhap_tabout)
        self.output_check_id_auto_checkBox.setObjectName(u"output_check_id_auto_checkBox")
        sizePolicy3.setHeightForWidth(self.output_check_id_auto_checkBox.sizePolicy().hasHeightForWidth())
        self.output_check_id_auto_checkBox.setSizePolicy(sizePolicy3)
        self.output_check_id_auto_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/load_off.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/load_on.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.output_check_id_auto_checkBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.output_check_id_auto_checkBox)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)

        self.output_component_name_label = QLabel(self.widget_nhap_tabout)
        self.output_component_name_label.setObjectName(u"output_component_name_label")
        sizePolicy8.setHeightForWidth(self.output_component_name_label.sizePolicy().hasHeightForWidth())
        self.output_component_name_label.setSizePolicy(sizePolicy8)
        self.output_component_name_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_component_name_label.setMargin(7)

        self.gridLayout_4.addWidget(self.output_component_name_label, 2, 5, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.output_quantity_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_quantity_lineedit.setObjectName(u"output_quantity_lineedit")
        sizePolicy8.setHeightForWidth(self.output_quantity_lineedit.sizePolicy().hasHeightForWidth())
        self.output_quantity_lineedit.setSizePolicy(sizePolicy8)
        self.output_quantity_lineedit.setMinimumSize(QSize(0, 30))
        self.output_quantity_lineedit.setFont(font)
        self.output_quantity_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.output_quantity_lineedit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.output_quantity_lineedit)

        self.output_inventory_label = QLabel(self.widget_nhap_tabout)
        self.output_inventory_label.setObjectName(u"output_inventory_label")
        sizePolicy8.setHeightForWidth(self.output_inventory_label.sizePolicy().hasHeightForWidth())
        self.output_inventory_label.setSizePolicy(sizePolicy8)
        self.output_inventory_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_inventory_label.setAlignment(Qt.AlignCenter)
        self.output_inventory_label.setMargin(7)

        self.verticalLayout.addWidget(self.output_inventory_label)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.output_unit_label = QLabel(self.widget_nhap_tabout)
        self.output_unit_label.setObjectName(u"output_unit_label")
        sizePolicy6.setHeightForWidth(self.output_unit_label.sizePolicy().hasHeightForWidth())
        self.output_unit_label.setSizePolicy(sizePolicy6)
        self.output_unit_label.setFont(font5)
        self.output_unit_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_unit_label.setAlignment(Qt.AlignCenter)
        self.output_unit_label.setMargin(0)

        self.horizontalLayout_7.addWidget(self.output_unit_label)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 4, 2, 2, 1)

        self.output_component_name_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_component_name_label_2.setObjectName(u"output_component_name_label_2")
        self.output_component_name_label_2.setFont(font1)
        self.output_component_name_label_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_component_name_label_2, 2, 4, 1, 1)

        self.output_model_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_model_label_2.setObjectName(u"output_model_label_2")
        self.output_model_label_2.setFont(font1)
        self.output_model_label_2.setMargin(0)

        self.gridLayout_4.addWidget(self.output_model_label_2, 3, 0, 1, 1)

        self.output_process_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_process_label_2.setObjectName(u"output_process_label_2")
        self.output_process_label_2.setFont(font1)
        self.output_process_label_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_process_label_2, 3, 4, 1, 1)

        self.output_invoice_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_invoice_label_2.setObjectName(u"output_invoice_label_2")
        self.output_invoice_label_2.setFont(font1)
        self.output_invoice_label_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_invoice_label_2, 4, 4, 1, 1)

        self.output_model_label = QLabel(self.widget_nhap_tabout)
        self.output_model_label.setObjectName(u"output_model_label")
        sizePolicy8.setHeightForWidth(self.output_model_label.sizePolicy().hasHeightForWidth())
        self.output_model_label.setSizePolicy(sizePolicy8)
        self.output_model_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_model_label.setAlignment(Qt.AlignCenter)
        self.output_model_label.setMargin(7)

        self.gridLayout_4.addWidget(self.output_model_label, 3, 2, 1, 1)

        self.output_desinvoice_labels_2 = QLabel(self.widget_nhap_tabout)
        self.output_desinvoice_labels_2.setObjectName(u"output_desinvoice_labels_2")
        self.output_desinvoice_labels_2.setFont(font1)
        self.output_desinvoice_labels_2.setMargin(7)

        self.gridLayout_4.addWidget(self.output_desinvoice_labels_2, 5, 4, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.output_size_label = QLabel(self.widget_nhap_tabout)
        self.output_size_label.setObjectName(u"output_size_label")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.output_size_label.sizePolicy().hasHeightForWidth())
        self.output_size_label.setSizePolicy(sizePolicy9)
        self.output_size_label.setMinimumSize(QSize(100, 0))
        font6 = QFont()
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        font6.setStyleStrategy(QFont.NoAntialias)
        self.output_size_label.setFont(font6)
        self.output_size_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_size_label.setAlignment(Qt.AlignCenter)
        self.output_size_label.setMargin(7)

        self.horizontalLayout_10.addWidget(self.output_size_label)

        self.output_material_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_material_label_2.setObjectName(u"output_material_label_2")
        self.output_material_label_2.setFont(font1)
        self.output_material_label_2.setMargin(7)

        self.horizontalLayout_10.addWidget(self.output_material_label_2)

        self.output_material_label = QLabel(self.widget_nhap_tabout)
        self.output_material_label.setObjectName(u"output_material_label")
        sizePolicy9.setHeightForWidth(self.output_material_label.sizePolicy().hasHeightForWidth())
        self.output_material_label.setSizePolicy(sizePolicy9)
        self.output_material_label.setMinimumSize(QSize(120, 0))
        self.output_material_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_material_label.setAlignment(Qt.AlignCenter)
        self.output_material_label.setMargin(7)

        self.horizontalLayout_10.addWidget(self.output_material_label)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 1, 5, 1, 1)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.output_process_label = QLabel(self.widget_nhap_tabout)
        self.output_process_label.setObjectName(u"output_process_label")
        sizePolicy8.setHeightForWidth(self.output_process_label.sizePolicy().hasHeightForWidth())
        self.output_process_label.setSizePolicy(sizePolicy8)
        self.output_process_label.setMinimumSize(QSize(100, 0))
        self.output_process_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_process_label.setAlignment(Qt.AlignCenter)
        self.output_process_label.setMargin(7)

        self.horizontalLayout_31.addWidget(self.output_process_label)

        self.output_groups_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_groups_label_2.setObjectName(u"output_groups_label_2")
        self.output_groups_label_2.setFont(font1)
        self.output_groups_label_2.setMargin(7)

        self.horizontalLayout_31.addWidget(self.output_groups_label_2)

        self.output_groups_label = QLabel(self.widget_nhap_tabout)
        self.output_groups_label.setObjectName(u"output_groups_label")
        sizePolicy8.setHeightForWidth(self.output_groups_label.sizePolicy().hasHeightForWidth())
        self.output_groups_label.setSizePolicy(sizePolicy8)
        self.output_groups_label.setMinimumSize(QSize(120, 0))
        self.output_groups_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_groups_label.setAlignment(Qt.AlignCenter)
        self.output_groups_label.setMargin(7)

        self.horizontalLayout_31.addWidget(self.output_groups_label)


        self.gridLayout_4.addLayout(self.horizontalLayout_31, 3, 5, 1, 1)

        self.output_invoice_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_invoice_lineedit.setObjectName(u"output_invoice_lineedit")
        sizePolicy8.setHeightForWidth(self.output_invoice_lineedit.sizePolicy().hasHeightForWidth())
        self.output_invoice_lineedit.setSizePolicy(sizePolicy8)
        self.output_invoice_lineedit.setMinimumSize(QSize(0, 30))
        self.output_invoice_lineedit.setFont(font)
        self.output_invoice_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.output_invoice_lineedit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.output_invoice_lineedit, 4, 5, 1, 1)

        self.output_desinvoice_lineedit = QLineEdit(self.widget_nhap_tabout)
        self.output_desinvoice_lineedit.setObjectName(u"output_desinvoice_lineedit")
        sizePolicy8.setHeightForWidth(self.output_desinvoice_lineedit.sizePolicy().hasHeightForWidth())
        self.output_desinvoice_lineedit.setSizePolicy(sizePolicy8)
        self.output_desinvoice_lineedit.setMinimumSize(QSize(0, 30))
        self.output_desinvoice_lineedit.setFont(font)
        self.output_desinvoice_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.output_desinvoice_lineedit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.output_desinvoice_lineedit, 5, 5, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.output_note_label = QLabel(self.widget_nhap_tabout)
        self.output_note_label.setObjectName(u"output_note_label")
        self.output_note_label.setFont(font1)
        self.output_note_label.setTextFormat(Qt.AutoText)
        self.output_note_label.setScaledContents(False)
        self.output_note_label.setWordWrap(False)
        self.output_note_label.setMargin(0)

        self.horizontalLayout_32.addWidget(self.output_note_label)

        self.output_search_note_checkBox = QCheckBox(self.widget_nhap_tabout)
        self.output_search_note_checkBox.setObjectName(u"output_search_note_checkBox")
        sizePolicy3.setHeightForWidth(self.output_search_note_checkBox.sizePolicy().hasHeightForWidth())
        self.output_search_note_checkBox.setSizePolicy(sizePolicy3)
        self.output_search_note_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.output_search_note_checkBox.setChecked(False)

        self.horizontalLayout_32.addWidget(self.output_search_note_checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer)


        self.gridLayout_4.addLayout(self.horizontalLayout_32, 1, 8, 1, 1)

        self.output_status_label_2 = QLabel(self.widget_nhap_tabout)
        self.output_status_label_2.setObjectName(u"output_status_label_2")
        self.output_status_label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.output_status_label_2, 2, 0, 1, 1)

        self.output_status_label = QLabel(self.widget_nhap_tabout)
        self.output_status_label.setObjectName(u"output_status_label")
        sizePolicy8.setHeightForWidth(self.output_status_label.sizePolicy().hasHeightForWidth())
        self.output_status_label.setSizePolicy(sizePolicy8)
        self.output_status_label.setMinimumSize(QSize(0, 0))
        self.output_status_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.output_status_label.setAlignment(Qt.AlignCenter)
        self.output_status_label.setMargin(7)

        self.gridLayout_4.addWidget(self.output_status_label, 2, 2, 1, 1)

        self.output_images_label.raise_()
        self.widget_zoom_tabout.raise_()
        self.output_inventory_label_2.raise_()
        self.output_quantity_label.raise_()
        self.output_size_label_2.raise_()
        self.output_note_textedit.raise_()
        self.output_component_name_label_2.raise_()
        self.output_component_name_label.raise_()
        self.output_model_label_2.raise_()
        self.output_model_label.raise_()
        self.output_process_label_2.raise_()
        self.output_invoice_label_2.raise_()
        self.output_desinvoice_labels_2.raise_()
        self.output_invoice_lineedit.raise_()
        self.output_desinvoice_lineedit.raise_()
        self.output_status_label_2.raise_()
        self.output_status_label.raise_()

        self.verticalLayout_6.addWidget(self.widget_nhap_tabout)

        self.widget_button_tabout = QWidget(self.tabOutput)
        self.widget_button_tabout.setObjectName(u"widget_button_tabout")
        self.widget_button_tabout.setMaximumSize(QSize(16777215, 60))
        self.outputButtonLayout = QHBoxLayout(self.widget_button_tabout)
        self.outputButtonLayout.setSpacing(5)
        self.outputButtonLayout.setObjectName(u"outputButtonLayout")
        self.outputButtonLayout.setContentsMargins(5, 5, 5, 5)
        self.output_new_button = QPushButton(self.widget_button_tabout)
        self.output_new_button.setObjectName(u"output_new_button")
        sizePolicy2.setHeightForWidth(self.output_new_button.sizePolicy().hasHeightForWidth())
        self.output_new_button.setSizePolicy(sizePolicy2)
        self.output_new_button.setMinimumSize(QSize(0, 40))
        self.output_new_button.setFont(font)
        self.output_new_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font: 75 14pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        self.output_new_button.setIcon(icon4)
        self.output_new_button.setIconSize(QSize(36, 32))

        self.outputButtonLayout.addWidget(self.output_new_button)

        self.output_delete_button = QPushButton(self.widget_button_tabout)
        self.output_delete_button.setObjectName(u"output_delete_button")
        sizePolicy2.setHeightForWidth(self.output_delete_button.sizePolicy().hasHeightForWidth())
        self.output_delete_button.setSizePolicy(sizePolicy2)
        self.output_delete_button.setMinimumSize(QSize(0, 40))
        self.output_delete_button.setFont(font1)
        self.output_delete_button.setStyleSheet(u"/* QPushButton - Red alert style */\n"
"QPushButton {\n"
"    background-color: #e53935;       /* \u0110\u1ecf c\u1ea3nh b\u00e1o hi\u1ec7n \u0111\u1ea1i */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f;       /* \u0110\u1ecf \u0111\u1eadm h\u01a1n khi hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b71c1c;       /* \u0110\u1ecf t\u1ed1i khi nh\u1ea5n */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #e0e0e0;\n"
"    color: #999;\n"
"}\n"
"")
        self.output_delete_button.setIcon(icon6)
        self.output_delete_button.setIconSize(QSize(32, 32))

        self.outputButtonLayout.addWidget(self.output_delete_button)

        self.output_export_button = QPushButton(self.widget_button_tabout)
        self.output_export_button.setObjectName(u"output_export_button")
        sizePolicy2.setHeightForWidth(self.output_export_button.sizePolicy().hasHeightForWidth())
        self.output_export_button.setSizePolicy(sizePolicy2)
        self.output_export_button.setMinimumSize(QSize(0, 40))
        self.output_export_button.setFont(font)
        self.output_export_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font: 75 14pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        self.output_export_button.setIcon(icon7)
        self.output_export_button.setIconSize(QSize(32, 32))

        self.outputButtonLayout.addWidget(self.output_export_button)

        self.output_search_button = QPushButton(self.widget_button_tabout)
        self.output_search_button.setObjectName(u"output_search_button")
        sizePolicy2.setHeightForWidth(self.output_search_button.sizePolicy().hasHeightForWidth())
        self.output_search_button.setSizePolicy(sizePolicy2)
        self.output_search_button.setMinimumSize(QSize(0, 40))
        self.output_search_button.setFont(font1)
        self.output_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
"QPushButton {\n"
"    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
"    font-size: 14px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #d3d3d3;\n"
"    color: #888;\n"
"}\n"
"")
        self.output_search_button.setIcon(icon9)
        self.output_search_button.setIconSize(QSize(32, 32))

        self.outputButtonLayout.addWidget(self.output_search_button)


        self.verticalLayout_6.addWidget(self.widget_button_tabout)

        self.output_data_tablewidget = QTableWidget(self.tabOutput)
        if (self.output_data_tablewidget.columnCount() < 3):
            self.output_data_tablewidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.output_data_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.output_data_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.output_data_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.output_data_tablewidget.setObjectName(u"output_data_tablewidget")
        self.output_data_tablewidget.setStyleSheet(u"/* QTableWidget styling */\n"
"QTableWidget {\n"
"    background-color: #f9fbfd; /* N\u1ec1n b\u1ea3ng xanh nh\u1ea1t */\n"
"    border: 1px solid #d3d9e3; /* \u0110\u01b0\u1eddng vi\u1ec1n nh\u1eb9 */\n"
"    font-size: 12px; /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    color: #333333; /* M\u00e0u ch\u1eef ch\u00ednh */\n"
"    gridline-color: #e7edf3; /* M\u00e0u \u0111\u01b0\u1eddng l\u01b0\u1edbi nh\u1ea1t */\n"
"    selection-background-color: #3b82cc; /* M\u00e0u n\u1ec1n khi ch\u1ecdn */\n"
"    selection-color: #ffffff; /* M\u00e0u ch\u1eef khi ch\u1ecdn */\n"
"    outline: none; /* Lo\u1ea1i b\u1ecf vi\u1ec1n s\u00e1ng khi focus */\n"
"}\n"
"\n"
"/* Ti\u00eau \u0111\u1ec1 c\u1ed9t */\n"
"QHeaderView::section {\n"
"    background-color: #e5effb; /* N\u1ec1n ti\u00eau \u0111\u1ec1 xanh nh\u1ea1t */\n"
"    color: #4a4a4a; /* M\u00e0u ch\u1eef ti\u00eau \u0111\u1ec1 */\n"
"    padding: 10px;\n"
"    border: 1px solid #d3d9e3; /* Vi\u1ec1n gi\u1eefa c\u00e1c ti\u00eau \u0111\u1ec1 */\n"
"    font-size"
                        ": 12px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* C\u00e1c \u00f4 */\n"
"QTableWidget::item {\n"
"    background-color: #ffffff; /* N\u1ec1n \u00f4 m\u1eb7c \u0111\u1ecbnh */\n"
"    border: none;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #333333; /* M\u00e0u ch\u1eef */\n"
"}\n"
"\n"
"/* \u00d4 xen k\u1ebd */\n"
"QTableWidget::item:alternate {\n"
"    background-color: #f4f8fc; /* N\u1ec1n xen k\u1ebd xanh nh\u1eb9 */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng hover */\n"
"QTableWidget::item:hover {\n"
"    background-color: #dceaf7; /* M\u00e0u hover xanh nh\u1ea1t */\n"
"    color: #333333; /* Ch\u1eef v\u1eabn d\u1ec5 \u0111\u1ecdc */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng hover n\u1ed5i b\u1eadt to\u00e0n d\u00f2ng */\n"
"QTableWidget::row:hover {\n"
"    background-color: #cce1f4; /* N\u1ec1n hover n\u1ed5i b\u1eadt c\u1ea3 d\u00f2ng */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi ch\u1ecdn */\n"
"QTableWidget::item:selected {\n"
"    background-color: #3b82cc; /* M"
                        "\u00e0u n\u1ec1n xanh \u0111\u1eadm khi ch\u1ecdn */\n"
"    color: #ffffff; /* M\u00e0u ch\u1eef tr\u1eafng khi ch\u1ecdn */\n"
"}\n"
"\n"
"/* Scrollbar */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f4f8fc; /* N\u1ec1n thanh cu\u1ed9n xanh nh\u1ea1t */\n"
"    width: 12px;\n"
"    margin: 2px 0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3b82cc; /* Thanh tr\u01b0\u1ee3t xanh \u0111\u1eadm */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #2f6fa5; /* Thanh tr\u01b0\u1ee3t khi hover */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* G\u00f3c cu\u1ed9n */\n"
"QScrollBar::corner {\n"
"    background: #ffffff;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi focus */\n"
"QTableWidget:focus {\n"
"    border: 1px solid #3b82cc; /* Vi\u1ec1n xanh \u0111\u1eadm khi focus */\n"
"}\n"
"")
        self.output_data_tablewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.output_data_tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_6.addWidget(self.output_data_tablewidget)

        icon11 = QIcon()
        icon11.addFile(u":/icon/images/icon/stock_release_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabOutput, icon11, "")
        self.tabLayout = QWidget()
        self.tabLayout.setObjectName(u"tabLayout")
        self.verticalLayout_7 = QVBoxLayout(self.tabLayout)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.widget_search_tablayout = QWidget(self.tabLayout)
        self.widget_search_tablayout.setObjectName(u"widget_search_tablayout")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_search_tablayout)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.layout_process_label = QLabel(self.widget_search_tablayout)
        self.layout_process_label.setObjectName(u"layout_process_label")
        sizePolicy4.setHeightForWidth(self.layout_process_label.sizePolicy().hasHeightForWidth())
        self.layout_process_label.setSizePolicy(sizePolicy4)
        self.layout_process_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.layout_process_label)

        self.layout_search_process_radio = QRadioButton(self.widget_search_tablayout)
        self.layout_search_process_radio.setObjectName(u"layout_search_process_radio")
        sizePolicy3.setHeightForWidth(self.layout_search_process_radio.sizePolicy().hasHeightForWidth())
        self.layout_search_process_radio.setSizePolicy(sizePolicy3)
        self.layout_search_process_radio.setStyleSheet(u"QRadioButton::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.layout_search_process_radio)

        self.layout_process_combobox = QComboBox(self.widget_search_tablayout)
        self.layout_process_combobox.setObjectName(u"layout_process_combobox")
        sizePolicy8.setHeightForWidth(self.layout_process_combobox.sizePolicy().hasHeightForWidth())
        self.layout_process_combobox.setSizePolicy(sizePolicy8)
        self.layout_process_combobox.setMaximumSize(QSize(300, 16777215))
        self.layout_process_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout_process_combobox.setLayoutDirection(Qt.LeftToRight)
        self.layout_process_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.layout_process_combobox.setEditable(False)

        self.horizontalLayout_3.addWidget(self.layout_process_combobox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.layout_storage_location_label = QLabel(self.widget_search_tablayout)
        self.layout_storage_location_label.setObjectName(u"layout_storage_location_label")
        sizePolicy4.setHeightForWidth(self.layout_storage_location_label.sizePolicy().hasHeightForWidth())
        self.layout_storage_location_label.setSizePolicy(sizePolicy4)
        self.layout_storage_location_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.layout_storage_location_label)

        self.layout_search_storage_location_radio = QRadioButton(self.widget_search_tablayout)
        self.layout_search_storage_location_radio.setObjectName(u"layout_search_storage_location_radio")
        sizePolicy3.setHeightForWidth(self.layout_search_storage_location_radio.sizePolicy().hasHeightForWidth())
        self.layout_search_storage_location_radio.setSizePolicy(sizePolicy3)
        self.layout_search_storage_location_radio.setStyleSheet(u"QRadioButton::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.layout_search_storage_location_radio)

        self.layout_storage_location_combobox = QComboBox(self.widget_search_tablayout)
        self.layout_storage_location_combobox.setObjectName(u"layout_storage_location_combobox")
        sizePolicy8.setHeightForWidth(self.layout_storage_location_combobox.sizePolicy().hasHeightForWidth())
        self.layout_storage_location_combobox.setSizePolicy(sizePolicy8)
        self.layout_storage_location_combobox.setMaximumSize(QSize(300, 16777215))
        self.layout_storage_location_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout_storage_location_combobox.setFocusPolicy(Qt.WheelFocus)
        self.layout_storage_location_combobox.setLayoutDirection(Qt.LeftToRight)
        self.layout_storage_location_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.layout_storage_location_combobox.setEditable(False)

        self.horizontalLayout_3.addWidget(self.layout_storage_location_combobox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addWidget(self.widget_search_tablayout)

        self.layout_search_button = QPushButton(self.tabLayout)
        self.layout_search_button.setObjectName(u"layout_search_button")
        self.layout_search_button.setMinimumSize(QSize(0, 40))
        self.layout_search_button.setMaximumSize(QSize(16777215, 40))
        self.layout_search_button.setSizeIncrement(QSize(0, 40))
        self.layout_search_button.setFont(font1)
        self.layout_search_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
"QPushButton {\n"
"    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
"    font-size: 14px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #d3d3d3;\n"
"    color: #888;\n"
"}\n"
"")
        self.layout_search_button.setIcon(icon9)
        self.layout_search_button.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.layout_search_button)

        self.widget_box_tablayout = QWidget(self.tabLayout)
        self.widget_box_tablayout.setObjectName(u"widget_box_tablayout")
        self.gridLayout_boxs = QGridLayout(self.widget_box_tablayout)
        self.gridLayout_boxs.setSpacing(5)
        self.gridLayout_boxs.setObjectName(u"gridLayout_boxs")
        self.gridLayout_boxs.setContentsMargins(5, 5, 5, 5)
        self.layout_label = QLabel(self.widget_box_tablayout)
        self.layout_label.setObjectName(u"layout_label")
        self.layout_label.setFont(font4)
        self.layout_label.setFrameShape(QFrame.NoFrame)
        self.layout_label.setScaledContents(False)
        self.layout_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_boxs.addWidget(self.layout_label, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_box_tablayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        icon12 = QIcon()
        icon12.addFile(u":/icon/images/icon/layout_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabLayout, icon12, "")
        self.tabOther = QWidget()
        self.tabOther.setObjectName(u"tabOther")
        self.verticalLayout_4 = QVBoxLayout(self.tabOther)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.widget_camera = QWidget(self.tabOther)
        self.widget_camera.setObjectName(u"widget_camera")
        self.verticalLayout_2 = QVBoxLayout(self.widget_camera)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.other_camera_label = QLabel(self.widget_camera)
        self.other_camera_label.setObjectName(u"other_camera_label")
        self.other_camera_label.setStyleSheet(u"/* QLabel styling */\n"
"QLabel {\n"
"    background-color: #ffffff; /* N\u1ec1n tr\u1eafng t\u1ea1o c\u1ea3m gi\u00e1c chuy\u00ean nghi\u1ec7p */\n"
"    border: 2px solid #e0e0e0; /* Vi\u1ec1n m\u1ecfng v\u00e0 nh\u1eb9 nh\u00e0ng */\n"
"    border-radius: 15px; /* G\u00f3c bo v\u1eeba ph\u1ea3i */\n"
"    padding: 8px; /* \u0110\u1ec7m \u0111\u1ec1u h\u01a1n */\n"
"    color: #444444; /* M\u00e0u ch\u1eef trung t\u00ednh, d\u1ec5 \u0111\u1ecdc */\n"
"}")
        self.other_camera_label.setFrameShape(QFrame.StyledPanel)
        self.other_camera_label.setPixmap(QPixmap(u":/icon/images/icon/Camera.png"))
        self.other_camera_label.setScaledContents(False)
        self.other_camera_label.setAlignment(Qt.AlignCenter)
        self.other_camera_label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.other_camera_label)

        self.other_capture_button = QPushButton(self.widget_camera)
        self.other_capture_button.setObjectName(u"other_capture_button")
        sizePolicy2.setHeightForWidth(self.other_capture_button.sizePolicy().hasHeightForWidth())
        self.other_capture_button.setSizePolicy(sizePolicy2)
        self.other_capture_button.setMinimumSize(QSize(0, 40))
        self.other_capture_button.setMaximumSize(QSize(16777215, 40))
        self.other_capture_button.setSizeIncrement(QSize(0, 40))
        self.other_capture_button.setFont(font)
        self.other_capture_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    font-size: 14px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font: 75 16pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icon/images/icon/Capture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.other_capture_button.setIcon(icon13)
        self.other_capture_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.other_capture_button)


        self.verticalLayout_4.addWidget(self.widget_camera)

        self.tabWidget_main.addTab(self.tabOther, "")
        self.tabInventory = QWidget()
        self.tabInventory.setObjectName(u"tabInventory")
        self.verticalLayout_10 = QVBoxLayout(self.tabInventory)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.widget_nhap_tabinventory = QWidget(self.tabInventory)
        self.widget_nhap_tabinventory.setObjectName(u"widget_nhap_tabinventory")
        self.gridLayout_NhapKho_2 = QGridLayout(self.widget_nhap_tabinventory)
        self.gridLayout_NhapKho_2.setSpacing(5)
        self.gridLayout_NhapKho_2.setObjectName(u"gridLayout_NhapKho_2")
        self.gridLayout_NhapKho_2.setContentsMargins(5, 5, 5, 5)
        self.inventory_search_material_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_material_checkBox.setObjectName(u"inventory_search_material_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_material_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_material_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_material_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_material_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_material_checkBox, 3, 2, 1, 1)

        self.inventory_status_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_status_label.setObjectName(u"inventory_status_label")
        sizePolicy4.setHeightForWidth(self.inventory_status_label.sizePolicy().hasHeightForWidth())
        self.inventory_status_label.setSizePolicy(sizePolicy4)
        self.inventory_status_label.setFont(font1)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_status_label, 2, 0, 1, 1)

        self.widget_zoom_tabinventory = QWidget(self.widget_nhap_tabinventory)
        self.widget_zoom_tabinventory.setObjectName(u"widget_zoom_tabinventory")
        self.inventory_hz_layout_zoom_radio = QHBoxLayout(self.widget_zoom_tabinventory)
        self.inventory_hz_layout_zoom_radio.setSpacing(6)
        self.inventory_hz_layout_zoom_radio.setObjectName(u"inventory_hz_layout_zoom_radio")
        self.inventory_hz_layout_zoom_radio.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.inventory_hz_layout_zoom_radio.setContentsMargins(5, 0, 1, 0)
        self.inventory_zoom_dec_button = QPushButton(self.widget_zoom_tabinventory)
        self.inventory_zoom_dec_button.setObjectName(u"inventory_zoom_dec_button")
        sizePolicy3.setHeightForWidth(self.inventory_zoom_dec_button.sizePolicy().hasHeightForWidth())
        self.inventory_zoom_dec_button.setSizePolicy(sizePolicy3)
        self.inventory_zoom_dec_button.setMinimumSize(QSize(28, 28))
        self.inventory_zoom_dec_button.setMaximumSize(QSize(28, 28))
        self.inventory_zoom_dec_button.setSizeIncrement(QSize(0, 40))
        self.inventory_zoom_dec_button.setFont(font)
        self.inventory_zoom_dec_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_zoom_dec_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    padding: 8px 16px; /* \u0110i\u1ec1u ch\u1ec9nh padding \u0111\u1ec3 n\u00fat c\u00f3 kh\u00f4ng gian tho\u1ea3i m\u00e1i h\u01a1n */\n"
"    border-radius: 11px; /* Bo tr\u00f2n g\u00f3c */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"")
        self.inventory_zoom_dec_button.setIcon(icon2)
        self.inventory_zoom_dec_button.setIconSize(QSize(24, 24))

        self.inventory_hz_layout_zoom_radio.addWidget(self.inventory_zoom_dec_button)

        self.horizontalSpacer_39 = QSpacerItem(120, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.inventory_hz_layout_zoom_radio.addItem(self.horizontalSpacer_39)

        self.inventory_zoom_inc_button = QPushButton(self.widget_zoom_tabinventory)
        self.inventory_zoom_inc_button.setObjectName(u"inventory_zoom_inc_button")
        sizePolicy3.setHeightForWidth(self.inventory_zoom_inc_button.sizePolicy().hasHeightForWidth())
        self.inventory_zoom_inc_button.setSizePolicy(sizePolicy3)
        self.inventory_zoom_inc_button.setMinimumSize(QSize(28, 28))
        self.inventory_zoom_inc_button.setMaximumSize(QSize(25, 25))
        self.inventory_zoom_inc_button.setSizeIncrement(QSize(0, 40))
        self.inventory_zoom_inc_button.setFont(font)
        self.inventory_zoom_inc_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_zoom_inc_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    padding: 8px 16px; /* \u0110i\u1ec1u ch\u1ec9nh padding \u0111\u1ec3 n\u00fat c\u00f3 kh\u00f4ng gian tho\u1ea3i m\u00e1i h\u01a1n */\n"
"    border-radius: 11px; /* Bo tr\u00f2n g\u00f3c */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"")
        self.inventory_zoom_inc_button.setIcon(icon3)
        self.inventory_zoom_inc_button.setIconSize(QSize(24, 24))

        self.inventory_hz_layout_zoom_radio.addWidget(self.inventory_zoom_inc_button)


        self.gridLayout_NhapKho_2.addWidget(self.widget_zoom_tabinventory, 1, 14, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.inventory_status_combobox = QComboBox(self.widget_nhap_tabinventory)
        self.inventory_status_combobox.setObjectName(u"inventory_status_combobox")
        sizePolicy3.setHeightForWidth(self.inventory_status_combobox.sizePolicy().hasHeightForWidth())
        self.inventory_status_combobox.setSizePolicy(sizePolicy3)
        self.inventory_status_combobox.setMinimumSize(QSize(65, 0))
        self.inventory_status_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_status_combobox.setLayoutDirection(Qt.LeftToRight)
        self.inventory_status_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.inventory_status_combobox.setEditable(False)

        self.horizontalLayout_29.addWidget(self.inventory_status_combobox)

        self.inventory_quantity_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_quantity_label.setObjectName(u"inventory_quantity_label")
        sizePolicy4.setHeightForWidth(self.inventory_quantity_label.sizePolicy().hasHeightForWidth())
        self.inventory_quantity_label.setSizePolicy(sizePolicy4)
        self.inventory_quantity_label.setFont(font1)
        self.inventory_quantity_label.setMargin(7)

        self.horizontalLayout_29.addWidget(self.inventory_quantity_label)

        self.inventory_quantity_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_quantity_lineedit.setObjectName(u"inventory_quantity_lineedit")
        sizePolicy8.setHeightForWidth(self.inventory_quantity_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_quantity_lineedit.setSizePolicy(sizePolicy8)
        self.inventory_quantity_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_quantity_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.inventory_quantity_lineedit)

        self.inventory_unit_combobox = QComboBox(self.widget_nhap_tabinventory)
        self.inventory_unit_combobox.setObjectName(u"inventory_unit_combobox")
        sizePolicy3.setHeightForWidth(self.inventory_unit_combobox.sizePolicy().hasHeightForWidth())
        self.inventory_unit_combobox.setSizePolicy(sizePolicy3)
        self.inventory_unit_combobox.setMinimumSize(QSize(65, 0))
        self.inventory_unit_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_unit_combobox.setLayoutDirection(Qt.LeftToRight)
        self.inventory_unit_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.inventory_unit_combobox.setEditable(False)

        self.horizontalLayout_29.addWidget(self.inventory_unit_combobox)


        self.gridLayout_NhapKho_2.addLayout(self.horizontalLayout_29, 2, 3, 1, 1)

        self.inventory_search_size_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_size_checkBox.setObjectName(u"inventory_search_size_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_size_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_size_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_size_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_size_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_size_checkBox, 4, 2, 1, 1)

        self.inventory_search_storage_location_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_storage_location_checkBox.setObjectName(u"inventory_search_storage_location_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_storage_location_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_storage_location_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_storage_location_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_storage_location_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_storage_location_checkBox, 1, 2, 1, 1)

        self.inventory_note_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_note_label.setObjectName(u"inventory_note_label")
        sizePolicy4.setHeightForWidth(self.inventory_note_label.sizePolicy().hasHeightForWidth())
        self.inventory_note_label.setSizePolicy(sizePolicy4)
        self.inventory_note_label.setFont(font1)
        self.inventory_note_label.setTextFormat(Qt.AutoText)
        self.inventory_note_label.setScaledContents(False)
        self.inventory_note_label.setWordWrap(False)
        self.inventory_note_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_note_label, 1, 12, 1, 1)

        self.inventory_images_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_images_label.setObjectName(u"inventory_images_label")
        self.inventory_images_label.setEnabled(True)
        self.inventory_images_label.setMinimumSize(QSize(280, 200))
        self.inventory_images_label.setMaximumSize(QSize(280, 16777215))
        self.inventory_images_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_images_label.setStyleSheet(u"/* QLabel styling */\n"
"QLabel {\n"
"    background-color: #ffffff; /* N\u1ec1n tr\u1eafng t\u1ea1o c\u1ea3m gi\u00e1c chuy\u00ean nghi\u1ec7p */\n"
"    border: 2px solid #e0e0e0; /* Vi\u1ec1n m\u1ecfng v\u00e0 nh\u1eb9 nh\u00e0ng */\n"
"    border-radius: 15px; /* G\u00f3c bo v\u1eeba ph\u1ea3i */\n"
"    padding: 6px; /* \u0110\u1ec7m \u0111\u1ec1u h\u01a1n */\n"
"    color: #444444; /* M\u00e0u ch\u1eef trung t\u00ednh, d\u1ec5 \u0111\u1ecdc */\n"
"}\n"
"/* Hi\u1ec7u \u1ee9ng khi hover */\n"
"QLabel:hover {\n"
"    background-color: #f7faff; /* Thay \u0111\u1ed5i n\u1ec1n nh\u1eb9 khi hover */\n"
"}\n"
"\n"
"")
        self.inventory_images_label.setFrameShape(QFrame.StyledPanel)
        self.inventory_images_label.setPixmap(QPixmap(u":/icon/images/icon/no_image.png"))
        self.inventory_images_label.setScaledContents(True)
        self.inventory_images_label.setAlignment(Qt.AlignCenter)
        self.inventory_images_label.setWordWrap(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_images_label, 1, 14, 5, 1)

        self.inventory_storage_location_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_storage_location_label.setObjectName(u"inventory_storage_location_label")
        sizePolicy4.setHeightForWidth(self.inventory_storage_location_label.sizePolicy().hasHeightForWidth())
        self.inventory_storage_location_label.setSizePolicy(sizePolicy4)
        self.inventory_storage_location_label.setFont(font1)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_storage_location_label, 1, 0, 1, 1)

        self.inventory_note_textedit = QTextEdit(self.widget_nhap_tabinventory)
        self.inventory_note_textedit.setObjectName(u"inventory_note_textedit")
        self.inventory_note_textedit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #4a90e2;\n"
"}")
        self.inventory_note_textedit.setFrameShape(QFrame.StyledPanel)
        self.inventory_note_textedit.setFrameShadow(QFrame.Plain)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_note_textedit, 2, 12, 4, 2)

        self.inventory_search_note_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_note_checkBox.setObjectName(u"inventory_search_note_checkBox")
        self.inventory_search_note_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_note_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_note_checkBox, 1, 13, 1, 1)

        self.inventory_desinvoice_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_desinvoice_label.setObjectName(u"inventory_desinvoice_label")
        sizePolicy4.setHeightForWidth(self.inventory_desinvoice_label.sizePolicy().hasHeightForWidth())
        self.inventory_desinvoice_label.setSizePolicy(sizePolicy4)
        self.inventory_desinvoice_label.setFont(font1)
        self.inventory_desinvoice_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_desinvoice_label, 5, 6, 1, 1)

        self.inventory_search_desinvoice_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_desinvoice_checkBox.setObjectName(u"inventory_search_desinvoice_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_desinvoice_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_desinvoice_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_desinvoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_desinvoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_desinvoice_checkBox, 5, 7, 1, 1)

        self.inventory_desinvoice_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_desinvoice_lineedit.setObjectName(u"inventory_desinvoice_lineedit")
        self.inventory_desinvoice_lineedit.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.inventory_desinvoice_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_desinvoice_lineedit.setSizePolicy(sizePolicy8)
        self.inventory_desinvoice_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_desinvoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_desinvoice_lineedit, 5, 8, 1, 1)

        self.inventory_size_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_size_label.setObjectName(u"inventory_size_label")
        sizePolicy4.setHeightForWidth(self.inventory_size_label.sizePolicy().hasHeightForWidth())
        self.inventory_size_label.setSizePolicy(sizePolicy4)
        self.inventory_size_label.setFont(font1)
        self.inventory_size_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_size_label, 4, 0, 1, 1)

        self.inventory_material_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_material_label.setObjectName(u"inventory_material_label")
        sizePolicy4.setHeightForWidth(self.inventory_material_label.sizePolicy().hasHeightForWidth())
        self.inventory_material_label.setSizePolicy(sizePolicy4)
        self.inventory_material_label.setFont(font1)
        self.inventory_material_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_material_label, 3, 0, 1, 1)

        self.output_size_horizontalLayout = QHBoxLayout()
        self.output_size_horizontalLayout.setObjectName(u"output_size_horizontalLayout")
        self.inventory_length_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_length_lineedit.setObjectName(u"inventory_length_lineedit")
        self.inventory_length_lineedit.setEnabled(True)
        self.inventory_length_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.inventory_length_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_length_lineedit.setMaxLength(32767)
        self.inventory_length_lineedit.setAlignment(Qt.AlignCenter)

        self.output_size_horizontalLayout.addWidget(self.inventory_length_lineedit)

        self.input_size_label_5 = QLabel(self.widget_nhap_tabinventory)
        self.input_size_label_5.setObjectName(u"input_size_label_5")
        sizePolicy4.setHeightForWidth(self.input_size_label_5.sizePolicy().hasHeightForWidth())
        self.input_size_label_5.setSizePolicy(sizePolicy4)
        self.input_size_label_5.setFont(font1)
        self.input_size_label_5.setMargin(7)

        self.output_size_horizontalLayout.addWidget(self.input_size_label_5)

        self.inventory_width_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_width_lineedit.setObjectName(u"inventory_width_lineedit")
        self.inventory_width_lineedit.setEnabled(True)
        self.inventory_width_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.inventory_width_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_width_lineedit.setMaxLength(32767)
        self.inventory_width_lineedit.setAlignment(Qt.AlignCenter)

        self.output_size_horizontalLayout.addWidget(self.inventory_width_lineedit)

        self.input_size_label_6 = QLabel(self.widget_nhap_tabinventory)
        self.input_size_label_6.setObjectName(u"input_size_label_6")
        sizePolicy4.setHeightForWidth(self.input_size_label_6.sizePolicy().hasHeightForWidth())
        self.input_size_label_6.setSizePolicy(sizePolicy4)
        self.input_size_label_6.setFont(font1)
        self.input_size_label_6.setMargin(7)

        self.output_size_horizontalLayout.addWidget(self.input_size_label_6)

        self.inventory_height_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_height_lineedit.setObjectName(u"inventory_height_lineedit")
        self.inventory_height_lineedit.setEnabled(True)
        self.inventory_height_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.inventory_height_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_height_lineedit.setMaxLength(32767)
        self.inventory_height_lineedit.setAlignment(Qt.AlignCenter)

        self.output_size_horizontalLayout.addWidget(self.inventory_height_lineedit)

        self.input_size_label_7 = QLabel(self.widget_nhap_tabinventory)
        self.input_size_label_7.setObjectName(u"input_size_label_7")
        sizePolicy4.setHeightForWidth(self.input_size_label_7.sizePolicy().hasHeightForWidth())
        self.input_size_label_7.setSizePolicy(sizePolicy4)
        self.input_size_label_7.setFont(font1)
        self.input_size_label_7.setMargin(7)

        self.output_size_horizontalLayout.addWidget(self.input_size_label_7)


        self.gridLayout_NhapKho_2.addLayout(self.output_size_horizontalLayout, 4, 3, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.inventory_storage_location_combobox = QComboBox(self.widget_nhap_tabinventory)
        self.inventory_storage_location_combobox.setObjectName(u"inventory_storage_location_combobox")
        sizePolicy8.setHeightForWidth(self.inventory_storage_location_combobox.sizePolicy().hasHeightForWidth())
        self.inventory_storage_location_combobox.setSizePolicy(sizePolicy8)
        self.inventory_storage_location_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_storage_location_combobox.setLayoutDirection(Qt.LeftToRight)
        self.inventory_storage_location_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.inventory_storage_location_combobox.setEditable(False)

        self.horizontalLayout_33.addWidget(self.inventory_storage_location_combobox)

        self.inventory_component_id_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_component_id_label.setObjectName(u"inventory_component_id_label")
        sizePolicy4.setHeightForWidth(self.inventory_component_id_label.sizePolicy().hasHeightForWidth())
        self.inventory_component_id_label.setSizePolicy(sizePolicy4)
        self.inventory_component_id_label.setFont(font1)
        self.inventory_component_id_label.setMargin(7)

        self.horizontalLayout_33.addWidget(self.inventory_component_id_label)

        self.inventory_search_component_id_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_component_id_checkBox.setObjectName(u"inventory_search_component_id_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_component_id_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_component_id_checkBox.setChecked(False)

        self.horizontalLayout_33.addWidget(self.inventory_search_component_id_checkBox)

        self.inventory_component_id_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_component_id_lineedit.setObjectName(u"inventory_component_id_lineedit")
        sizePolicy8.setHeightForWidth(self.inventory_component_id_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_component_id_lineedit.setSizePolicy(sizePolicy8)
        self.inventory_component_id_lineedit.setFont(font)
        self.inventory_component_id_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_component_id_lineedit.setMaxLength(8)
        self.inventory_component_id_lineedit.setAlignment(Qt.AlignCenter)
        self.inventory_component_id_lineedit.setClearButtonEnabled(True)

        self.horizontalLayout_33.addWidget(self.inventory_component_id_lineedit)


        self.gridLayout_NhapKho_2.addLayout(self.horizontalLayout_33, 1, 3, 1, 1)

        self.inventory_invoice_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_invoice_label.setObjectName(u"inventory_invoice_label")
        sizePolicy4.setHeightForWidth(self.inventory_invoice_label.sizePolicy().hasHeightForWidth())
        self.inventory_invoice_label.setSizePolicy(sizePolicy4)
        self.inventory_invoice_label.setFont(font1)
        self.inventory_invoice_label.setMargin(0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_invoice_label, 5, 0, 1, 1)

        self.inventory_search_groups_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_groups_checkBox.setObjectName(u"inventory_search_groups_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_groups_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_groups_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_groups_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_groups_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_groups_checkBox, 3, 7, 1, 1)

        self.inventory_search_invoice_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_invoice_checkBox.setObjectName(u"inventory_search_invoice_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_invoice_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_invoice_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_invoice_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_invoice_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_invoice_checkBox, 5, 2, 1, 1)

        self.inventory_groups_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_groups_label.setObjectName(u"inventory_groups_label")
        sizePolicy4.setHeightForWidth(self.inventory_groups_label.sizePolicy().hasHeightForWidth())
        self.inventory_groups_label.setSizePolicy(sizePolicy4)
        self.inventory_groups_label.setFont(font1)
        self.inventory_groups_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_groups_label, 3, 6, 1, 1)

        self.inventory_invoice_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_invoice_lineedit.setObjectName(u"inventory_invoice_lineedit")
        self.inventory_invoice_lineedit.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.inventory_invoice_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_invoice_lineedit.setSizePolicy(sizePolicy8)
        self.inventory_invoice_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_invoice_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_invoice_lineedit, 5, 3, 1, 1)

        self.inventory_search_model_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_model_checkBox.setObjectName(u"inventory_search_model_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_model_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_model_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_model_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_model_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_model_checkBox, 4, 7, 1, 1)

        self.inventory_model_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_model_label.setObjectName(u"inventory_model_label")
        sizePolicy4.setHeightForWidth(self.inventory_model_label.sizePolicy().hasHeightForWidth())
        self.inventory_model_label.setSizePolicy(sizePolicy4)
        self.inventory_model_label.setFont(font1)
        self.inventory_model_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_model_label, 4, 6, 1, 1)

        self.inventory_component_name_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_component_name_label.setObjectName(u"inventory_component_name_label")
        sizePolicy4.setHeightForWidth(self.inventory_component_name_label.sizePolicy().hasHeightForWidth())
        self.inventory_component_name_label.setSizePolicy(sizePolicy4)
        self.inventory_component_name_label.setFont(font1)
        self.inventory_component_name_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_component_name_label, 1, 6, 1, 1)

        self.inventory_search_component_name_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_component_name_checkBox.setObjectName(u"inventory_search_component_name_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_component_name_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_component_name_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_component_name_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_component_name_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_component_name_checkBox, 1, 7, 1, 1)

        self.inventory_process_label = QLabel(self.widget_nhap_tabinventory)
        self.inventory_process_label.setObjectName(u"inventory_process_label")
        sizePolicy4.setHeightForWidth(self.inventory_process_label.sizePolicy().hasHeightForWidth())
        self.inventory_process_label.setSizePolicy(sizePolicy4)
        self.inventory_process_label.setFont(font1)
        self.inventory_process_label.setMargin(7)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_process_label, 2, 6, 1, 1)

        self.inventory_component_name_lineedit = QLineEdit(self.widget_nhap_tabinventory)
        self.inventory_component_name_lineedit.setObjectName(u"inventory_component_name_lineedit")
        self.inventory_component_name_lineedit.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.inventory_component_name_lineedit.sizePolicy().hasHeightForWidth())
        self.inventory_component_name_lineedit.setSizePolicy(sizePolicy8)
        self.inventory_component_name_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.inventory_component_name_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.inventory_component_name_lineedit.setClearButtonEnabled(True)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_component_name_lineedit, 1, 8, 1, 1)

        self.inventory_search_process_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_process_checkBox.setObjectName(u"inventory_search_process_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_process_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_process_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_process_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_process_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_process_checkBox, 2, 7, 1, 1)

        self.inventory_material_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_material_widget.setObjectName(u"inventory_material_widget")
        self.horizontalLayout_30 = QHBoxLayout(self.inventory_material_widget)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_material_widget, 3, 3, 1, 1)

        self.inventory_process_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_process_widget.setObjectName(u"inventory_process_widget")
        self.horizontalLayout_36 = QHBoxLayout(self.inventory_process_widget)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_process_widget, 2, 8, 1, 1)

        self.inventory_groups_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_groups_widget.setObjectName(u"inventory_groups_widget")
        self.horizontalLayout_37 = QHBoxLayout(self.inventory_groups_widget)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_groups_widget, 3, 8, 1, 1)

        self.inventory_model_widget = QWidget(self.widget_nhap_tabinventory)
        self.inventory_model_widget.setObjectName(u"inventory_model_widget")
        self.horizontalLayout_38 = QHBoxLayout(self.inventory_model_widget)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_model_widget, 4, 8, 1, 1)

        self.inventory_search_status_checkBox = QCheckBox(self.widget_nhap_tabinventory)
        self.inventory_search_status_checkBox.setObjectName(u"inventory_search_status_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_search_status_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_search_status_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_search_status_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 24px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 24px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/Search_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/Search_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_search_status_checkBox.setChecked(False)

        self.gridLayout_NhapKho_2.addWidget(self.inventory_search_status_checkBox, 2, 2, 1, 1)

        self.inventory_images_label.raise_()
        self.widget_zoom_tabinventory.raise_()
        self.inventory_note_label.raise_()
        self.inventory_search_storage_location_checkBox.raise_()
        self.inventory_note_textedit.raise_()
        self.inventory_storage_location_label.raise_()
        self.inventory_search_note_checkBox.raise_()
        self.inventory_desinvoice_label.raise_()
        self.inventory_search_desinvoice_checkBox.raise_()
        self.inventory_desinvoice_lineedit.raise_()
        self.inventory_status_label.raise_()
        self.inventory_material_label.raise_()
        self.inventory_search_material_checkBox.raise_()
        self.inventory_size_label.raise_()
        self.inventory_search_size_checkBox.raise_()
        self.inventory_invoice_lineedit.raise_()
        self.inventory_search_model_checkBox.raise_()
        self.inventory_model_label.raise_()
        self.inventory_invoice_label.raise_()
        self.inventory_search_invoice_checkBox.raise_()
        self.inventory_component_name_label.raise_()
        self.inventory_search_component_name_checkBox.raise_()
        self.inventory_component_name_lineedit.raise_()
        self.inventory_process_label.raise_()
        self.inventory_search_process_checkBox.raise_()
        self.inventory_groups_label.raise_()
        self.inventory_search_groups_checkBox.raise_()
        self.inventory_material_widget.raise_()
        self.inventory_process_widget.raise_()
        self.inventory_groups_widget.raise_()
        self.inventory_model_widget.raise_()
        self.inventory_search_status_checkBox.raise_()

        self.verticalLayout_10.addWidget(self.widget_nhap_tabinventory)

        self.widget_button_tabinventory = QWidget(self.tabInventory)
        self.widget_button_tabinventory.setObjectName(u"widget_button_tabinventory")
        self.inputButtonLayout_2 = QHBoxLayout(self.widget_button_tabinventory)
        self.inputButtonLayout_2.setSpacing(5)
        self.inputButtonLayout_2.setObjectName(u"inputButtonLayout_2")
        self.inputButtonLayout_2.setContentsMargins(5, 5, 5, 5)
        self.inventory_filter_component_id_checkBox = QCheckBox(self.widget_button_tabinventory)
        self.inventory_filter_component_id_checkBox.setObjectName(u"inventory_filter_component_id_checkBox")
        sizePolicy3.setHeightForWidth(self.inventory_filter_component_id_checkBox.sizePolicy().hasHeightForWidth())
        self.inventory_filter_component_id_checkBox.setSizePolicy(sizePolicy3)
        self.inventory_filter_component_id_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 32px; /* Chi\u1ec1u r\u1ed9ng icon */\n"
"    height: 32px; /* Chi\u1ec1u cao icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/images/icon/filter_no.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng unchecked */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/images/icon/filter_yes.png); /* \u0110\u01b0\u1eddng d\u1eabn \u0111\u1ebfn bi\u1ec3u t\u01b0\u1ee3ng checked */\n"
"}\n"
"")
        self.inventory_filter_component_id_checkBox.setChecked(False)

        self.inputButtonLayout_2.addWidget(self.inventory_filter_component_id_checkBox)

        self.inventory_search_button = QPushButton(self.widget_button_tabinventory)
        self.inventory_search_button.setObjectName(u"inventory_search_button")
        sizePolicy2.setHeightForWidth(self.inventory_search_button.sizePolicy().hasHeightForWidth())
        self.inventory_search_button.setSizePolicy(sizePolicy2)
        self.inventory_search_button.setMinimumSize(QSize(0, 40))
        self.inventory_search_button.setMaximumSize(QSize(16777215, 40))
        self.inventory_search_button.setSizeIncrement(QSize(0, 40))
        self.inventory_search_button.setFont(font1)
        self.inventory_search_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_search_button.setStyleSheet(u"/* QPushButton - Green modern style */\n"
"QPushButton {\n"
"    background-color: #4CAF50;       /* Xanh l\u00e1 hi\u1ec7n \u0111\u1ea1i */\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;       /* Xanh \u0111\u1eadm h\u01a1n khi hover */\n"
"    font-size: 14px;                 /* Gi\u1eef font-size, kh\u00f4ng nh\u1ea3y */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41;       /* Xanh t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #d3d3d3;\n"
"    color: #888;\n"
"}\n"
"")
        self.inventory_search_button.setIcon(icon9)
        self.inventory_search_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout_2.addWidget(self.inventory_search_button)

        self.inventory_export_button = QPushButton(self.widget_button_tabinventory)
        self.inventory_export_button.setObjectName(u"inventory_export_button")
        sizePolicy2.setHeightForWidth(self.inventory_export_button.sizePolicy().hasHeightForWidth())
        self.inventory_export_button.setSizePolicy(sizePolicy2)
        self.inventory_export_button.setMinimumSize(QSize(0, 40))
        self.inventory_export_button.setMaximumSize(QSize(16777215, 40))
        self.inventory_export_button.setSizeIncrement(QSize(0, 40))
        self.inventory_export_button.setFont(font)
        self.inventory_export_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.inventory_export_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font: 75 14pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        self.inventory_export_button.setIcon(icon7)
        self.inventory_export_button.setIconSize(QSize(32, 32))

        self.inputButtonLayout_2.addWidget(self.inventory_export_button)


        self.verticalLayout_10.addWidget(self.widget_button_tabinventory)

        self.inventory_data_tablewidget = QTableWidget(self.tabInventory)
        if (self.inventory_data_tablewidget.columnCount() < 3):
            self.inventory_data_tablewidget.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.inventory_data_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.inventory_data_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.inventory_data_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.inventory_data_tablewidget.setObjectName(u"inventory_data_tablewidget")
        self.inventory_data_tablewidget.setStyleSheet(u"/* QTableWidget styling */\n"
"QTableWidget {\n"
"    background-color: #f9fbfd; /* N\u1ec1n b\u1ea3ng xanh nh\u1ea1t */\n"
"    border: 1px solid #d3d9e3; /* \u0110\u01b0\u1eddng vi\u1ec1n nh\u1eb9 */\n"
"    font-size: 12px; /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    color: #333333; /* M\u00e0u ch\u1eef ch\u00ednh */\n"
"    gridline-color: #e7edf3; /* M\u00e0u \u0111\u01b0\u1eddng l\u01b0\u1edbi nh\u1ea1t */\n"
"    selection-background-color: #3b82cc; /* M\u00e0u n\u1ec1n khi ch\u1ecdn */\n"
"    selection-color: #ffffff; /* M\u00e0u ch\u1eef khi ch\u1ecdn */\n"
"    outline: none; /* Lo\u1ea1i b\u1ecf vi\u1ec1n s\u00e1ng khi focus */\n"
"}\n"
"\n"
"/* Ti\u00eau \u0111\u1ec1 c\u1ed9t */\n"
"QHeaderView::section {\n"
"    background-color: #e5effb; /* N\u1ec1n ti\u00eau \u0111\u1ec1 xanh nh\u1ea1t */\n"
"    color: #4a4a4a; /* M\u00e0u ch\u1eef ti\u00eau \u0111\u1ec1 */\n"
"    padding: 10px;\n"
"    border: 1px solid #d3d9e3; /* Vi\u1ec1n gi\u1eefa c\u00e1c ti\u00eau \u0111\u1ec1 */\n"
"    font-size"
                        ": 12px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* C\u00e1c \u00f4 */\n"
"QTableWidget::item {\n"
"    background-color: #ffffff; /* N\u1ec1n \u00f4 m\u1eb7c \u0111\u1ecbnh */\n"
"    border: none;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #333333; /* M\u00e0u ch\u1eef */\n"
"}\n"
"\n"
"/* \u00d4 xen k\u1ebd */\n"
"QTableWidget::item:alternate {\n"
"    background-color: #f4f8fc; /* N\u1ec1n xen k\u1ebd xanh nh\u1eb9 */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng hover */\n"
"QTableWidget::item:hover {\n"
"    background-color: #dceaf7; /* M\u00e0u hover xanh nh\u1ea1t */\n"
"    color: #333333; /* Ch\u1eef v\u1eabn d\u1ec5 \u0111\u1ecdc */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng hover n\u1ed5i b\u1eadt to\u00e0n d\u00f2ng */\n"
"QTableWidget::row:hover {\n"
"    background-color: #cce1f4; /* N\u1ec1n hover n\u1ed5i b\u1eadt c\u1ea3 d\u00f2ng */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi ch\u1ecdn */\n"
"QTableWidget::item:selected {\n"
"    background-color: #3b82cc; /* M"
                        "\u00e0u n\u1ec1n xanh \u0111\u1eadm khi ch\u1ecdn */\n"
"    color: #ffffff; /* M\u00e0u ch\u1eef tr\u1eafng khi ch\u1ecdn */\n"
"}\n"
"\n"
"/* Scrollbar */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f4f8fc; /* N\u1ec1n thanh cu\u1ed9n xanh nh\u1ea1t */\n"
"    width: 12px;\n"
"    margin: 2px 0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3b82cc; /* Thanh tr\u01b0\u1ee3t xanh \u0111\u1eadm */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #2f6fa5; /* Thanh tr\u01b0\u1ee3t khi hover */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* G\u00f3c cu\u1ed9n */\n"
"QScrollBar::corner {\n"
"    background: #ffffff;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi focus */\n"
"QTableWidget:focus {\n"
"    border: 1px solid #3b82cc; /* Vi\u1ec1n xanh \u0111\u1eadm khi focus */\n"
"}\n"
"")
        self.inventory_data_tablewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.inventory_data_tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inventory_data_tablewidget.setSortingEnabled(False)

        self.verticalLayout_10.addWidget(self.inventory_data_tablewidget)

        self.tabWidget_main.addTab(self.tabInventory, icon, "")
        self.tabChangepassword = QWidget()
        self.tabChangepassword.setObjectName(u"tabChangepassword")
        self.verticalLayout_11 = QVBoxLayout(self.tabChangepassword)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.horizontalWidget_Change = QWidget(self.tabChangepassword)
        self.horizontalWidget_Change.setObjectName(u"horizontalWidget_Change")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_Change)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)

        self.widgetk = QWidget(self.horizontalWidget_Change)
        self.widgetk.setObjectName(u"widgetk")
        self.verticalLayout_14 = QVBoxLayout(self.widgetk)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_changepassword = QWidget(self.widgetk)
        self.widget_changepassword.setObjectName(u"widget_changepassword")
        sizePolicy4.setHeightForWidth(self.widget_changepassword.sizePolicy().hasHeightForWidth())
        self.widget_changepassword.setSizePolicy(sizePolicy4)
        self.widget_changepassword.setMinimumSize(QSize(400, 0))
        self.widget_changepassword.setMaximumSize(QSize(600, 500))
        self.widget_changepassword.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0, 0.6); /* M\u00e0u n\u1ec1n \u0111en m\u1edd */\n"
"    border-radius: 15px; /* Bo g\u00f3c m\u1ec1m m\u1ea1i */\n"
"}\n"
"")
        self.verticalLayout_15 = QVBoxLayout(self.widget_changepassword)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.change_logo_label = QLabel(self.widget_changepassword)
        self.change_logo_label.setObjectName(u"change_logo_label")
        sizePolicy4.setHeightForWidth(self.change_logo_label.sizePolicy().hasHeightForWidth())
        self.change_logo_label.setSizePolicy(sizePolicy4)
        self.change_logo_label.setMaximumSize(QSize(100, 70))
        self.change_logo_label.setFont(font1)
        self.change_logo_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* N\u1ec1n trong su\u1ed1t */\n"
"}\n"
"")
        self.change_logo_label.setPixmap(QPixmap(u":/icon/images/icon/logo.png"))
        self.change_logo_label.setScaledContents(True)
        self.change_logo_label.setAlignment(Qt.AlignCenter)
        self.change_logo_label.setWordWrap(False)

        self.horizontalLayout_11.addWidget(self.change_logo_label)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.change_msnv_label = QLabel(self.widget_changepassword)
        self.change_msnv_label.setObjectName(u"change_msnv_label")
        sizePolicy3.setHeightForWidth(self.change_msnv_label.sizePolicy().hasHeightForWidth())
        self.change_msnv_label.setSizePolicy(sizePolicy3)
        self.change_msnv_label.setMinimumSize(QSize(300, 40))
        self.change_msnv_label.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}")
        self.change_msnv_label.setAlignment(Qt.AlignCenter)
        self.change_msnv_label.setMargin(7)

        self.horizontalLayout_12.addWidget(self.change_msnv_label)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_15 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.change_password_old_lineedit = QLineEdit(self.widget_changepassword)
        self.change_password_old_lineedit.setObjectName(u"change_password_old_lineedit")
        sizePolicy3.setHeightForWidth(self.change_password_old_lineedit.sizePolicy().hasHeightForWidth())
        self.change_password_old_lineedit.setSizePolicy(sizePolicy3)
        self.change_password_old_lineedit.setMinimumSize(QSize(300, 40))
        self.change_password_old_lineedit.setFont(font)
        self.change_password_old_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.change_password_old_lineedit.setMaxLength(16)
        self.change_password_old_lineedit.setEchoMode(QLineEdit.Password)
        self.change_password_old_lineedit.setAlignment(Qt.AlignCenter)
        self.change_password_old_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_13.addWidget(self.change_password_old_lineedit)


        self.verticalLayout_15.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_16 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.change_password_new_lineedit = QLineEdit(self.widget_changepassword)
        self.change_password_new_lineedit.setObjectName(u"change_password_new_lineedit")
        sizePolicy3.setHeightForWidth(self.change_password_new_lineedit.sizePolicy().hasHeightForWidth())
        self.change_password_new_lineedit.setSizePolicy(sizePolicy3)
        self.change_password_new_lineedit.setMinimumSize(QSize(300, 40))
        self.change_password_new_lineedit.setFont(font)
        self.change_password_new_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.change_password_new_lineedit.setMaxLength(16)
        self.change_password_new_lineedit.setEchoMode(QLineEdit.Password)
        self.change_password_new_lineedit.setAlignment(Qt.AlignCenter)
        self.change_password_new_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_15.addWidget(self.change_password_new_lineedit)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.change_password_new2_lineedit = QLineEdit(self.widget_changepassword)
        self.change_password_new2_lineedit.setObjectName(u"change_password_new2_lineedit")
        sizePolicy3.setHeightForWidth(self.change_password_new2_lineedit.sizePolicy().hasHeightForWidth())
        self.change_password_new2_lineedit.setSizePolicy(sizePolicy3)
        self.change_password_new2_lineedit.setMinimumSize(QSize(300, 40))
        self.change_password_new2_lineedit.setFont(font)
        self.change_password_new2_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.change_password_new2_lineedit.setMaxLength(16)
        self.change_password_new2_lineedit.setEchoMode(QLineEdit.Password)
        self.change_password_new2_lineedit.setAlignment(Qt.AlignCenter)
        self.change_password_new2_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_16.addWidget(self.change_password_new2_lineedit)


        self.verticalLayout_15.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_19 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_19)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.change_changing_button = QPushButton(self.widget_changepassword)
        self.change_changing_button.setObjectName(u"change_changing_button")
        sizePolicy5.setHeightForWidth(self.change_changing_button.sizePolicy().hasHeightForWidth())
        self.change_changing_button.setSizePolicy(sizePolicy5)
        self.change_changing_button.setMinimumSize(QSize(300, 50))
        self.change_changing_button.setMaximumSize(QSize(16777215, 50))
        self.change_changing_button.setSizeIncrement(QSize(0, 40))
        self.change_changing_button.setFont(font)
        self.change_changing_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.change_changing_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    color: #fff;\n"
"    font-size: 14px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font: 75 16pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        self.change_changing_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_14.addWidget(self.change_changing_button)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_17)


        self.verticalLayout_14.addWidget(self.widget_changepassword)


        self.horizontalLayout_6.addWidget(self.widgetk)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_21)


        self.verticalLayout_11.addWidget(self.horizontalWidget_Change)

        icon14 = QIcon()
        icon14.addFile(u":/icon/images/icon/changepassword_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabChangepassword, icon14, "")
        self.tabadduser = QWidget()
        self.tabadduser.setObjectName(u"tabadduser")
        self.verticalLayout_18 = QVBoxLayout(self.tabadduser)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.horizontalWidget_Login_2 = QWidget(self.tabadduser)
        self.horizontalWidget_Login_2.setObjectName(u"horizontalWidget_Login_2")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget_Login_2)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)

        self.widget_themUser = QWidget(self.horizontalWidget_Login_2)
        self.widget_themUser.setObjectName(u"widget_themUser")
        self.verticalLayout_16 = QVBoxLayout(self.widget_themUser)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_adduser = QWidget(self.widget_themUser)
        self.widget_adduser.setObjectName(u"widget_adduser")
        sizePolicy4.setHeightForWidth(self.widget_adduser.sizePolicy().hasHeightForWidth())
        self.widget_adduser.setSizePolicy(sizePolicy4)
        self.widget_adduser.setMinimumSize(QSize(400, 0))
        self.widget_adduser.setMaximumSize(QSize(600, 500))
        self.widget_adduser.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0, 0.6); /* M\u00e0u n\u1ec1n \u0111en m\u1edd */\n"
"    border-radius: 15px; /* Bo g\u00f3c m\u1ec1m m\u1ea1i */\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_adduser)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_22 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_22)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.adduser_logo_label = QLabel(self.widget_adduser)
        self.adduser_logo_label.setObjectName(u"adduser_logo_label")
        sizePolicy4.setHeightForWidth(self.adduser_logo_label.sizePolicy().hasHeightForWidth())
        self.adduser_logo_label.setSizePolicy(sizePolicy4)
        self.adduser_logo_label.setMaximumSize(QSize(100, 70))
        self.adduser_logo_label.setFont(font1)
        self.adduser_logo_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* N\u1ec1n trong su\u1ed1t */\n"
"}\n"
"")
        self.adduser_logo_label.setPixmap(QPixmap(u":/icon/images/icon/logo.png"))
        self.adduser_logo_label.setScaledContents(True)
        self.adduser_logo_label.setAlignment(Qt.AlignCenter)
        self.adduser_logo_label.setWordWrap(False)

        self.horizontalLayout_18.addWidget(self.adduser_logo_label)


        self.verticalLayout_17.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_23)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.adduser_msnv_lineedit = QLineEdit(self.widget_adduser)
        self.adduser_msnv_lineedit.setObjectName(u"adduser_msnv_lineedit")
        sizePolicy3.setHeightForWidth(self.adduser_msnv_lineedit.sizePolicy().hasHeightForWidth())
        self.adduser_msnv_lineedit.setSizePolicy(sizePolicy3)
        self.adduser_msnv_lineedit.setMinimumSize(QSize(300, 40))
        self.adduser_msnv_lineedit.setFont(font)
        self.adduser_msnv_lineedit.setAutoFillBackground(False)
        self.adduser_msnv_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.adduser_msnv_lineedit.setMaxLength(30)
        self.adduser_msnv_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.adduser_msnv_lineedit)


        self.verticalLayout_17.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_24 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_24)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.adduser_password_lineedit = QLineEdit(self.widget_adduser)
        self.adduser_password_lineedit.setObjectName(u"adduser_password_lineedit")
        sizePolicy3.setHeightForWidth(self.adduser_password_lineedit.sizePolicy().hasHeightForWidth())
        self.adduser_password_lineedit.setSizePolicy(sizePolicy3)
        self.adduser_password_lineedit.setMinimumSize(QSize(300, 40))
        self.adduser_password_lineedit.setFont(font)
        self.adduser_password_lineedit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}")
        self.adduser_password_lineedit.setMaxLength(16)
        self.adduser_password_lineedit.setEchoMode(QLineEdit.Password)
        self.adduser_password_lineedit.setAlignment(Qt.AlignCenter)
        self.adduser_password_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_20.addWidget(self.adduser_password_lineedit)


        self.verticalLayout_17.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_36 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_36)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.tabadduser_level_combobox = QComboBox(self.widget_adduser)
        self.tabadduser_level_combobox.setObjectName(u"tabadduser_level_combobox")
        sizePolicy3.setHeightForWidth(self.tabadduser_level_combobox.sizePolicy().hasHeightForWidth())
        self.tabadduser_level_combobox.setSizePolicy(sizePolicy3)
        self.tabadduser_level_combobox.setMinimumSize(QSize(300, 40))
        self.tabadduser_level_combobox.setFont(font)
        self.tabadduser_level_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabadduser_level_combobox.setLayoutDirection(Qt.LeftToRight)
        self.tabadduser_level_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.tabadduser_level_combobox.setEditable(False)

        self.horizontalLayout_27.addWidget(self.tabadduser_level_combobox)


        self.verticalLayout_17.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_27 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.tabadduser_team_combobox = QComboBox(self.widget_adduser)
        self.tabadduser_team_combobox.setObjectName(u"tabadduser_team_combobox")
        sizePolicy3.setHeightForWidth(self.tabadduser_team_combobox.sizePolicy().hasHeightForWidth())
        self.tabadduser_team_combobox.setSizePolicy(sizePolicy3)
        self.tabadduser_team_combobox.setMinimumSize(QSize(300, 40))
        self.tabadduser_team_combobox.setFont(font)
        self.tabadduser_team_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabadduser_team_combobox.setLayoutDirection(Qt.LeftToRight)
        self.tabadduser_team_combobox.setStyleSheet(u"/* QComboBox styling */\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"/* Khi QComboBox \u0111\u01b0\u1ee3c focus */\n"
"QComboBox:focus {\n"
"    border: 2px solid #4a90e2; /* M\u00e0u vi\u1ec1n khi focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/images/icon/pngwing.com.png); /* \u0110\u1ea3m b\u1ea3o b\u1ea1n c\u00f3 m\u1ed9t bi\u1ec3u t\u01b0\u1ee3ng m\u0169i t\u00ean trong th\u01b0 m\u1ee5c 'icons' */\n"
"}")
        self.tabadduser_team_combobox.setEditable(False)

        self.horizontalLayout_28.addWidget(self.tabadduser_team_combobox)


        self.verticalLayout_17.addLayout(self.horizontalLayout_28)

        self.verticalSpacer_25 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_25)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.adduser_them_button = QPushButton(self.widget_adduser)
        self.adduser_them_button.setObjectName(u"adduser_them_button")
        sizePolicy5.setHeightForWidth(self.adduser_them_button.sizePolicy().hasHeightForWidth())
        self.adduser_them_button.setSizePolicy(sizePolicy5)
        self.adduser_them_button.setMinimumSize(QSize(300, 50))
        self.adduser_them_button.setMaximumSize(QSize(16777215, 50))
        self.adduser_them_button.setSizeIncrement(QSize(0, 40))
        self.adduser_them_button.setFont(font)
        self.adduser_them_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.adduser_them_button.setStyleSheet(u"/* QPushButton styling */\n"
"QPushButton {\n"
"    background-color: #4a90e2;\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    color: #fff;\n"
"    font-size: 14px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ab7;\n"
"	font: 16pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}")
        self.adduser_them_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.adduser_them_button)


        self.verticalLayout_17.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_26)


        self.verticalLayout_16.addWidget(self.widget_adduser)


        self.horizontalLayout_17.addWidget(self.widget_themUser)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_23)


        self.verticalLayout_18.addWidget(self.horizontalWidget_Login_2)

        icon15 = QIcon()
        icon15.addFile(u":/icon/images/icon/add_user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabadduser, icon15, "")
        self.tabChat = QWidget()
        self.tabChat.setObjectName(u"tabChat")
        self.horizontalLayout_9 = QHBoxLayout(self.tabChat)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frameUsers = QFrame(self.tabChat)
        self.frameUsers.setObjectName(u"frameUsers")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frameUsers.sizePolicy().hasHeightForWidth())
        self.frameUsers.setSizePolicy(sizePolicy10)
        self.frameUsers.setFrameShape(QFrame.NoFrame)
        self.verticalLayoutUsers = QVBoxLayout(self.frameUsers)
        self.verticalLayoutUsers.setObjectName(u"verticalLayoutUsers")
        self.labelOnline = QLabel(self.frameUsers)
        self.labelOnline.setObjectName(u"labelOnline")

        self.verticalLayoutUsers.addWidget(self.labelOnline)

        self.chat_list_user_online_qlistwidget = QListWidget(self.frameUsers)
        self.chat_list_user_online_qlistwidget.setObjectName(u"chat_list_user_online_qlistwidget")
        sizePolicy10.setHeightForWidth(self.chat_list_user_online_qlistwidget.sizePolicy().hasHeightForWidth())
        self.chat_list_user_online_qlistwidget.setSizePolicy(sizePolicy10)
        self.chat_list_user_online_qlistwidget.setMinimumSize(QSize(150, 0))
        self.chat_list_user_online_qlistwidget.setMaximumSize(QSize(150, 16777215))
        self.chat_list_user_online_qlistwidget.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QListWidget:focus {\n"
"    border: 2px solid #4a90e2;\n"
"}")

        self.verticalLayoutUsers.addWidget(self.chat_list_user_online_qlistwidget)


        self.horizontalLayout_9.addWidget(self.frameUsers)

        self.frameChat = QFrame(self.tabChat)
        self.frameChat.setObjectName(u"frameChat")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frameChat.sizePolicy().hasHeightForWidth())
        self.frameChat.setSizePolicy(sizePolicy11)
        self.frameChat.setFrameShape(QFrame.NoFrame)
        self.verticalLayoutChat = QVBoxLayout(self.frameChat)
        self.verticalLayoutChat.setObjectName(u"verticalLayoutChat")
        self.chat_display_browser_qscrollarea = QScrollArea(self.frameChat)
        self.chat_display_browser_qscrollarea.setObjectName(u"chat_display_browser_qscrollarea")
        self.chat_display_browser_qscrollarea.setAutoFillBackground(True)
        self.chat_display_browser_qscrollarea.setStyleSheet(u"QWidget#scrollAreaWidgetContents {\n"
"    border-image: url(:/icon/images/icon/background_chat.png) 0 0 0 0 stretch stretch;\n"
"    border-radius: 50px; /* Bo tr\u00f2n 4 g\u00f3c */\n"
"    background-color: transparent; /* Gi\u00fap bo tr\u00f2n kh\u00f4ng b\u1ecb n\u1ec1n che m\u1ea5t */\n"
"}\n"
"")
        self.chat_display_browser_qscrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1607, 1752))
        self.verticalLayoutMessages = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayoutMessages.setObjectName(u"verticalLayoutMessages")
        self.chat_display_browser_qscrollarea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayoutChat.addWidget(self.chat_display_browser_qscrollarea)

        self.horizontalLayoutInput = QHBoxLayout()
        self.horizontalLayoutInput.setObjectName(u"horizontalLayoutInput")
        self.chat_text_input_chat_textedit = QTextEdit(self.frameChat)
        self.chat_text_input_chat_textedit.setObjectName(u"chat_text_input_chat_textedit")
        sizePolicy7.setHeightForWidth(self.chat_text_input_chat_textedit.sizePolicy().hasHeightForWidth())
        self.chat_text_input_chat_textedit.setSizePolicy(sizePolicy7)
        self.chat_text_input_chat_textedit.setMinimumSize(QSize(0, 100))
        self.chat_text_input_chat_textedit.setMaximumSize(QSize(16777215, 100))
        self.chat_text_input_chat_textedit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    color: #3333FF;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #4a90e2;\n"
"}")

        self.horizontalLayoutInput.addWidget(self.chat_text_input_chat_textedit)

        self.chat_sent_button = QPushButton(self.frameChat)
        self.chat_sent_button.setObjectName(u"chat_sent_button")
        self.chat_sent_button.setStyleSheet(u"QPushButton {\n"
"    /*background-color: #4a90e2;*/\n"
"    image: url(:/icon/images/icon/send_chat_off.png);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    font-size: 14px;\n"
"    padding: 6px 12px;\n"
"    width: 70px;\n"
"    height: 70px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /*background-color: #357ab7;*/\n"
"    image: url(:/icon/images/icon/send_chat_on.png);\n"
"    font: 75 16pt;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a6cae;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ccc;\n"
"    color: #666;\n"
"}\n"
"")
        self.chat_sent_button.setIconSize(QSize(100, 200))

        self.horizontalLayoutInput.addWidget(self.chat_sent_button)


        self.verticalLayoutChat.addLayout(self.horizontalLayoutInput)


        self.horizontalLayout_9.addWidget(self.frameChat)

        icon16 = QIcon()
        icon16.addFile(u":/icon/images/icon/chat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_main.addTab(self.tabChat, icon16, "")

        self.verticalLayout_22.addWidget(self.tabWidget_main)

        self.title_foot_label = QLabel(self.MyWidget)
        self.title_foot_label.setObjectName(u"title_foot_label")
        sizePolicy11.setHeightForWidth(self.title_foot_label.sizePolicy().hasHeightForWidth())
        self.title_foot_label.setSizePolicy(sizePolicy11)
        font7 = QFont()
        font7.setPointSize(9)
        font7.setBold(True)
        self.title_foot_label.setFont(font7)
        self.title_foot_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.title_foot_label)

        self.MyWidget.raise_()
        self.images_zoom_label.raise_()
        QWidget.setTabOrder(self.login_msnv_lineedit, self.login_password_lineedit)
        QWidget.setTabOrder(self.login_password_lineedit, self.login_login_button)
        QWidget.setTabOrder(self.login_login_button, self.input_quantity_lineedit)
        QWidget.setTabOrder(self.input_quantity_lineedit, self.input_unit_combobox)
        QWidget.setTabOrder(self.input_unit_combobox, self.input_length_lineedit)
        QWidget.setTabOrder(self.input_length_lineedit, self.input_width_lineedit)
        QWidget.setTabOrder(self.input_width_lineedit, self.input_height_lineedit)
        QWidget.setTabOrder(self.input_height_lineedit, self.input_note_textedit)
        QWidget.setTabOrder(self.input_note_textedit, self.input_new_button)
        QWidget.setTabOrder(self.input_new_button, self.input_edit_button)
        QWidget.setTabOrder(self.input_edit_button, self.input_delete_button)
        QWidget.setTabOrder(self.input_delete_button, self.input_filter_component_id_checkBox)
        QWidget.setTabOrder(self.input_filter_component_id_checkBox, self.input_search_storage_location_checkBox)
        QWidget.setTabOrder(self.input_search_storage_location_checkBox, self.input_search_note_checkBox)
        QWidget.setTabOrder(self.input_search_note_checkBox, self.input_data_tablewidget)
        QWidget.setTabOrder(self.input_data_tablewidget, self.output_component_id_lineedit)
        QWidget.setTabOrder(self.output_component_id_lineedit, self.output_check_id_auto_checkBox)
        QWidget.setTabOrder(self.output_check_id_auto_checkBox, self.output_quantity_lineedit)
        QWidget.setTabOrder(self.output_quantity_lineedit, self.output_note_textedit)
        QWidget.setTabOrder(self.output_note_textedit, self.output_new_button)
        QWidget.setTabOrder(self.output_new_button, self.output_data_tablewidget)
        QWidget.setTabOrder(self.output_data_tablewidget, self.output_delete_button)
        QWidget.setTabOrder(self.output_delete_button, self.output_search_component_id_checkBox)
        QWidget.setTabOrder(self.output_search_component_id_checkBox, self.inventory_search_storage_location_checkBox)
        QWidget.setTabOrder(self.inventory_search_storage_location_checkBox, self.inventory_quantity_lineedit)
        QWidget.setTabOrder(self.inventory_quantity_lineedit, self.inventory_unit_combobox)
        QWidget.setTabOrder(self.inventory_unit_combobox, self.inventory_length_lineedit)
        QWidget.setTabOrder(self.inventory_length_lineedit, self.inventory_width_lineedit)
        QWidget.setTabOrder(self.inventory_width_lineedit, self.inventory_height_lineedit)
        QWidget.setTabOrder(self.inventory_height_lineedit, self.inventory_search_desinvoice_checkBox)
        QWidget.setTabOrder(self.inventory_search_desinvoice_checkBox, self.inventory_desinvoice_lineedit)
        QWidget.setTabOrder(self.inventory_desinvoice_lineedit, self.inventory_search_note_checkBox)
        QWidget.setTabOrder(self.inventory_search_note_checkBox, self.inventory_note_textedit)
        QWidget.setTabOrder(self.inventory_note_textedit, self.inventory_search_button)
        QWidget.setTabOrder(self.inventory_search_button, self.inventory_filter_component_id_checkBox)
        QWidget.setTabOrder(self.inventory_filter_component_id_checkBox, self.inventory_data_tablewidget)
        QWidget.setTabOrder(self.inventory_data_tablewidget, self.change_password_old_lineedit)
        QWidget.setTabOrder(self.change_password_old_lineedit, self.change_password_new_lineedit)
        QWidget.setTabOrder(self.change_password_new_lineedit, self.change_password_new2_lineedit)
        QWidget.setTabOrder(self.change_password_new2_lineedit, self.change_changing_button)
        QWidget.setTabOrder(self.change_changing_button, self.tabWidget_main)
        QWidget.setTabOrder(self.tabWidget_main, self.layout_process_combobox)
        QWidget.setTabOrder(self.layout_process_combobox, self.output_zoom_inc_button)
        QWidget.setTabOrder(self.output_zoom_inc_button, self.adduser_password_lineedit)
        QWidget.setTabOrder(self.adduser_password_lineedit, self.adduser_msnv_lineedit)
        QWidget.setTabOrder(self.adduser_msnv_lineedit, self.layout_storage_location_combobox)
        QWidget.setTabOrder(self.layout_storage_location_combobox, self.inventory_zoom_inc_button)
        QWidget.setTabOrder(self.inventory_zoom_inc_button, self.input_zoom_dec_button)
        QWidget.setTabOrder(self.input_zoom_dec_button, self.tabadduser_team_combobox)
        QWidget.setTabOrder(self.tabadduser_team_combobox, self.other_capture_button)
        QWidget.setTabOrder(self.other_capture_button, self.layout_search_storage_location_radio)
        QWidget.setTabOrder(self.layout_search_storage_location_radio, self.adduser_them_button)
        QWidget.setTabOrder(self.adduser_them_button, self.tabadduser_level_combobox)
        QWidget.setTabOrder(self.tabadduser_level_combobox, self.layout_search_button)
        QWidget.setTabOrder(self.layout_search_button, self.output_zoom_dec_button)
        QWidget.setTabOrder(self.output_zoom_dec_button, self.inventory_zoom_dec_button)
        QWidget.setTabOrder(self.inventory_zoom_dec_button, self.input_zoom_inc_button)
        QWidget.setTabOrder(self.input_zoom_inc_button, self.layout_search_process_radio)

        self.retranslateUi(InventoryManager)

        self.tabWidget_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(InventoryManager)
    # setupUi

    def retranslateUi(self, InventoryManager):
        InventoryManager.setWindowTitle(QCoreApplication.translate("InventoryManager", u"Inventory Manager", None))
        self.images_zoom_label.setText("")
        self.input_open_invoice_button.setText("")
#if QT_CONFIG(tooltip)
        self.input_check_id_info_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Load th\u00f4ng tin li\u00ean quan m\u00e3 CID hi\u1ec7n t\u1ea1i", None))
#endif // QT_CONFIG(tooltip)
        self.input_check_id_info_checkBox.setText("")
        self.input_logo_label.setText("")
        self.title_label.setText(QCoreApplication.translate("InventoryManager", u"\u0110\u0102NG NH\u1eacP T\u00c0I KHO\u1ea2N", None))
        self.image_user_label.setText("")
        self.team_user_label.setText(QCoreApplication.translate("InventoryManager", u"(ENG)", None))
        self.name_user_label.setText(QCoreApplication.translate("InventoryManager", u"GUEST", None))
        self.login_title_label.setText(QCoreApplication.translate("InventoryManager", u"WELCOME", None))
        self.login_logo_label.setText("")
        self.login_msnv_lineedit.setInputMask("")
        self.login_msnv_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp MSNV", None))
        self.login_password_lineedit.setInputMask("")
        self.login_password_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp Password", None))
        self.login_login_button.setText(QCoreApplication.translate("InventoryManager", u"Sign in", None))
        self.login_info_label.setText("")
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabLogin), QCoreApplication.translate("InventoryManager", u"LOGIN", None))
        self.input_component_name_labels.setText(QCoreApplication.translate("InventoryManager", u"CName:", None))
#if QT_CONFIG(tooltip)
        self.input_length_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp k\u00edch th\u01b0\u1edbc chi\u1ec1u d\u00e0i linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_length_lineedit.setStatusTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp chi\u1ec1u d\u00e0i", None))
#endif // QT_CONFIG(statustip)
        self.input_length_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Length", None))
        self.input_size_label_3.setText(QCoreApplication.translate("InventoryManager", u"x", None))
#if QT_CONFIG(tooltip)
        self.input_width_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp k\u00edch th\u01b0\u1edbc chi\u1ec1u r\u1ed9ng linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_width_lineedit.setStatusTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp chi\u1ec1u r\u1ed9ng", None))
#endif // QT_CONFIG(statustip)
        self.input_width_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Width", None))
        self.input_size_label_4.setText(QCoreApplication.translate("InventoryManager", u"x", None))
#if QT_CONFIG(tooltip)
        self.input_height_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp k\u00edch th\u01b0\u1edbc chi\u1ec1u cao linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_height_lineedit.setStatusTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp chi\u1ec1u cao", None))
#endif // QT_CONFIG(statustip)
        self.input_height_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Height", None))
        self.input_size_label_2.setText(QCoreApplication.translate("InventoryManager", u"mm", None))
        self.input_zoom_dec_button.setText("")
        self.input_zoom_inc_button.setText("")
#if QT_CONFIG(tooltip)
        self.input_search_size_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_size_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_search_storage_location_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_storage_location_checkBox.setText("")
        self.input_storage_location_labels.setText(QCoreApplication.translate("InventoryManager", u"SLoc.:", None))
        self.input_images_label.setText("")
        self.input_note_labels.setText(QCoreApplication.translate("InventoryManager", u"Note:", None))
#if QT_CONFIG(tooltip)
        self.input_search_note_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_note_checkBox.setText("")
        self.input_note_fillter_combobox.setItemText(0, QCoreApplication.translate("InventoryManager", u"Contains", None))
        self.input_note_fillter_combobox.setItemText(1, QCoreApplication.translate("InventoryManager", u"Does not contains", None))
        self.input_note_fillter_combobox.setItemText(2, QCoreApplication.translate("InventoryManager", u"Is empty", None))
        self.input_note_fillter_combobox.setItemText(3, QCoreApplication.translate("InventoryManager", u"Is not empty", None))

#if QT_CONFIG(tooltip)
        self.input_note_fillter_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"Ch\u1ecdn t\u00ean c\u00f4ng \u0111o\u1ea1n \u0111\u1ec3 g\u1eafn linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_note_fillter_combobox.setStatusTip(QCoreApplication.translate("InventoryManager", u"Ch\u1ecdn \u0111i\u1ec1u ki\u1ec7n l\u1ecdc d\u1eef li\u1ec7u", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.input_paste_button.setToolTip(QCoreApplication.translate("InventoryManager", u"<html><head/><body><p>Ch\u1ee9c n\u0103ng :</p><p>Paste d\u1eef li\u1ec7u chuy\u1ec3n \u0111\u1ed5i copy trong invoice excel</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.input_paste_button.setText(QCoreApplication.translate("InventoryManager", u"Paste", None))
#if QT_CONFIG(tooltip)
        self.input_storage_location_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"\u0110\u01a1n v\u1ecb", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input_search_component_id_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_component_id_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_component_id_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.input_component_id_lineedit.setInputMask("")
#if QT_CONFIG(tooltip)
        self.input_check_id_auto_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"T\u1ea1o m\u1edbi m\u00e3 CID t\u1ef1 \u0111\u1ed9ng theo m\u00e3 s\u1ed1 th\u00f9ng hi\u1ec7n t\u1ea1i", None))
#endif // QT_CONFIG(tooltip)
        self.input_check_id_auto_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_status_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"\u0110\u01a1n v\u1ecb", None))
#endif // QT_CONFIG(tooltip)
        self.input_quantity_labels.setText(QCoreApplication.translate("InventoryManager", u"  Qty.:", None))
#if QT_CONFIG(tooltip)
        self.input_quantity_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp s\u1ed1 l\u01b0\u1ee3ng", None))
#endif // QT_CONFIG(tooltip)
        self.input_quantity_lineedit.setInputMask(QCoreApplication.translate("InventoryManager", u"0000;_", None))
#if QT_CONFIG(tooltip)
        self.input_unit_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"\u0110\u01a1n v\u1ecb", None))
#endif // QT_CONFIG(tooltip)
        self.input_size_labels.setText(QCoreApplication.translate("InventoryManager", u"Size:", None))
        self.input_process_labels.setText(QCoreApplication.translate("InventoryManager", u"Process:", None))
#if QT_CONFIG(tooltip)
        self.input_search_component_name_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_component_name_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_component_name_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp t\u00ean g\u1ecdi linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.input_groups_labels.setText(QCoreApplication.translate("InventoryManager", u"Groups:", None))
#if QT_CONFIG(tooltip)
        self.input_search_process_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_process_checkBox.setText("")
        self.input_model_labels.setText(QCoreApplication.translate("InventoryManager", u"Model:", None))
#if QT_CONFIG(tooltip)
        self.input_search_model_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_model_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_search_groups_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_groups_checkBox.setText("")
        self.input_material_labels.setText(QCoreApplication.translate("InventoryManager", u"Mat.:", None))
#if QT_CONFIG(tooltip)
        self.input_search_material_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_material_checkBox.setText("")
        self.input_desinvoice_labels.setText(QCoreApplication.translate("InventoryManager", u"Des. Inv.:", None))
#if QT_CONFIG(tooltip)
        self.input_search_desinvoice_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_desinvoice_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_desinvoice_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp t\u00ean mod linh ki\u1ec7n nh\u1eadp v\u1ec1", None))
#endif // QT_CONFIG(tooltip)
        self.input_invoice_labels.setText(QCoreApplication.translate("InventoryManager", u"Invoice:", None))
#if QT_CONFIG(tooltip)
        self.input_search_invoice_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_invoice_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_invoice_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp m\u00e3 s\u1ed1 invoice nh\u1eadp v\u1ec1", None))
#endif // QT_CONFIG(tooltip)
        self.input_status_labels.setText(QCoreApplication.translate("InventoryManager", u"Status:", None))
#if QT_CONFIG(tooltip)
        self.input_search_status_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.input_search_status_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.input_filter_component_id_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"S\u1eafp x\u1ebfp d\u1eef li\u1ec7u c\u1ed9t ID", None))
#endif // QT_CONFIG(tooltip)
        self.input_filter_component_id_checkBox.setText("")
        self.input_new_button.setText(QCoreApplication.translate("InventoryManager", u"New", None))
        self.input_edit_button.setText(QCoreApplication.translate("InventoryManager", u"Edit", None))
        self.input_delete_button.setText(QCoreApplication.translate("InventoryManager", u"Delete", None))
        self.input_export_button.setText(QCoreApplication.translate("InventoryManager", u"Export to Excel", None))
        self.input_down_button.setText(QCoreApplication.translate("InventoryManager", u"Download Image", None))
        self.input_search_button.setText(QCoreApplication.translate("InventoryManager", u"Search", None))
        ___qtablewidgetitem = self.input_data_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InventoryManager", u"ID", None));
        ___qtablewidgetitem1 = self.input_data_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InventoryManager", u"Component ID", None));
        ___qtablewidgetitem2 = self.input_data_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InventoryManager", u"Name", None));
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabInput), QCoreApplication.translate("InventoryManager", u"STOCK IN", None))
        self.output_zoom_dec_button.setText("")
        self.output_zoom_inc_button.setText("")
        self.output_inventory_label_2.setText(QCoreApplication.translate("InventoryManager", u"Inv.:", None))
        self.output_quantity_label.setText(QCoreApplication.translate("InventoryManager", u"Qty.:", None))
        self.output_size_label_2.setText(QCoreApplication.translate("InventoryManager", u"Size:", None))
        self.output_images_label.setText("")
        self.output_storage_location_label_2.setText(QCoreApplication.translate("InventoryManager", u"SLoc.:", None))
#if QT_CONFIG(tooltip)
        self.output_search_component_id_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.output_search_component_id_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.output_storage_location_label.setToolTip(QCoreApplication.translate("InventoryManager", u"V\u1ecb tr\u00ed b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.output_storage_location_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
#if QT_CONFIG(tooltip)
        self.output_component_id_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n c\u1ea7n xu\u1ea5t", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.output_check_id_auto_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Ki\u1ec3m tra t\u1ed3n kho v\u00e0 th\u00f4ng tin", None))
#endif // QT_CONFIG(tooltip)
        self.output_check_id_auto_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.output_component_name_label.setToolTip(QCoreApplication.translate("InventoryManager", u"T\u00ean g\u1ecdi linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.output_component_name_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
#if QT_CONFIG(tooltip)
        self.output_quantity_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp s\u1ed1 l\u01b0\u1ee3ng c\u1ea7n xu\u1ea5t", None))
#endif // QT_CONFIG(tooltip)
        self.output_quantity_lineedit.setInputMask(QCoreApplication.translate("InventoryManager", u"0000;_", None))
#if QT_CONFIG(tooltip)
        self.output_inventory_label.setToolTip(QCoreApplication.translate("InventoryManager", u"\u0110\u00e2y l\u00e0 s\u1ed1 l\u01b0\u1ee3ng t\u1ed3n kho hi\u1ec7n t\u1ea1i", None))
#endif // QT_CONFIG(tooltip)
        self.output_inventory_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
        self.output_unit_label.setText(QCoreApplication.translate("InventoryManager", u"pcs", None))
        self.output_component_name_label_2.setText(QCoreApplication.translate("InventoryManager", u"CName.:", None))
        self.output_model_label_2.setText(QCoreApplication.translate("InventoryManager", u"Model:", None))
        self.output_process_label_2.setText(QCoreApplication.translate("InventoryManager", u"Process:", None))
        self.output_invoice_label_2.setText(QCoreApplication.translate("InventoryManager", u"Invoice:", None))
#if QT_CONFIG(tooltip)
        self.output_model_label.setToolTip(QCoreApplication.translate("InventoryManager", u"Linh ki\u1ec7n n\u00e0y g\u1eafn cho model", None))
#endif // QT_CONFIG(tooltip)
        self.output_model_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
        self.output_desinvoice_labels_2.setText(QCoreApplication.translate("InventoryManager", u"Des. Inv.:", None))
#if QT_CONFIG(tooltip)
        self.output_size_label.setToolTip(QCoreApplication.translate("InventoryManager", u"K\u00edch th\u01b0\u1edbc linh ki\u1ec7n D\u00e0i x R\u1ed9ng x Cao", None))
#endif // QT_CONFIG(tooltip)
        self.output_size_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
        self.output_material_label_2.setText(QCoreApplication.translate("InventoryManager", u"Mat.:", None))
#if QT_CONFIG(tooltip)
        self.output_material_label.setToolTip(QCoreApplication.translate("InventoryManager", u"V\u1eadt li\u1ec7u linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.output_material_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
#if QT_CONFIG(tooltip)
        self.output_process_label.setToolTip(QCoreApplication.translate("InventoryManager", u"Linh ki\u1ec7n n\u00e0y g\u1eafn cho c\u00f4ng \u0111o\u1ea1n", None))
#endif // QT_CONFIG(tooltip)
        self.output_process_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
        self.output_groups_label_2.setText(QCoreApplication.translate("InventoryManager", u"Groups:", None))
#if QT_CONFIG(tooltip)
        self.output_groups_label.setToolTip(QCoreApplication.translate("InventoryManager", u"Linh ki\u1ec7n n\u00e0y thu\u1ed9c nh\u00f3m", None))
#endif // QT_CONFIG(tooltip)
        self.output_groups_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
#if QT_CONFIG(tooltip)
        self.output_invoice_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n c\u1ea7n xu\u1ea5t", None))
#endif // QT_CONFIG(tooltip)
        self.output_invoice_lineedit.setText(QCoreApplication.translate("InventoryManager", u"-", None))
#if QT_CONFIG(tooltip)
        self.output_desinvoice_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp m\u00e3 s\u1ed1 linh ki\u1ec7n c\u1ea7n xu\u1ea5t", None))
#endif // QT_CONFIG(tooltip)
        self.output_desinvoice_lineedit.setText(QCoreApplication.translate("InventoryManager", u"-", None))
        self.output_note_label.setText(QCoreApplication.translate("InventoryManager", u"Note:", None))
#if QT_CONFIG(tooltip)
        self.output_search_note_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.output_search_note_checkBox.setText("")
        self.output_status_label_2.setText(QCoreApplication.translate("InventoryManager", u"Status:", None))
#if QT_CONFIG(tooltip)
        self.output_status_label.setToolTip(QCoreApplication.translate("InventoryManager", u"V\u1ecb tr\u00ed b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.output_status_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
        self.output_new_button.setText(QCoreApplication.translate("InventoryManager", u"New", None))
        self.output_delete_button.setText(QCoreApplication.translate("InventoryManager", u"Delete", None))
        self.output_export_button.setText(QCoreApplication.translate("InventoryManager", u"Export to Excel", None))
        self.output_search_button.setText(QCoreApplication.translate("InventoryManager", u"Search", None))
        ___qtablewidgetitem3 = self.output_data_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InventoryManager", u"ID", None));
        ___qtablewidgetitem4 = self.output_data_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InventoryManager", u"Component ID", None));
        ___qtablewidgetitem5 = self.output_data_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InventoryManager", u"Name", None));
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabOutput), QCoreApplication.translate("InventoryManager", u"STOCK OUT", None))
        self.layout_process_label.setText(QCoreApplication.translate("InventoryManager", u"Process:", None))
        self.layout_search_process_radio.setText("")
#if QT_CONFIG(tooltip)
        self.layout_process_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"Ch\u1ecdn n\u01a1i b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.layout_storage_location_label.setText(QCoreApplication.translate("InventoryManager", u"Storage Location:", None))
        self.layout_search_storage_location_radio.setText("")
#if QT_CONFIG(tooltip)
        self.layout_storage_location_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"Ch\u1ecdn n\u01a1i b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.layout_search_button.setText(QCoreApplication.translate("InventoryManager", u"Search", None))
        self.layout_label.setText(QCoreApplication.translate("InventoryManager", u"Box", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabLayout), QCoreApplication.translate("InventoryManager", u"LAYOUT", None))
        self.other_camera_label.setText("")
        self.other_capture_button.setText(QCoreApplication.translate("InventoryManager", u"Capture", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabOther), QCoreApplication.translate("InventoryManager", u"OTHER", None))
#if QT_CONFIG(tooltip)
        self.inventory_search_material_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_material_checkBox.setText("")
        self.inventory_status_label.setText(QCoreApplication.translate("InventoryManager", u"Status:", None))
        self.inventory_zoom_dec_button.setText("")
        self.inventory_zoom_inc_button.setText("")
#if QT_CONFIG(tooltip)
        self.inventory_status_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"\u0110\u01a1n v\u1ecb", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_quantity_label.setText(QCoreApplication.translate("InventoryManager", u"Qty.:", None))
#if QT_CONFIG(tooltip)
        self.inventory_quantity_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"S\u1ed1 l\u01b0\u1ee3ng nh\u1eadp", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_quantity_lineedit.setInputMask(QCoreApplication.translate("InventoryManager", u"0000;_", None))
#if QT_CONFIG(tooltip)
        self.inventory_unit_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"\u0110\u01a1n v\u1ecb", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inventory_search_size_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_size_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.inventory_search_storage_location_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_storage_location_checkBox.setText("")
        self.inventory_note_label.setText(QCoreApplication.translate("InventoryManager", u"Note:", None))
        self.inventory_images_label.setText("")
        self.inventory_storage_location_label.setText(QCoreApplication.translate("InventoryManager", u"SLoc.:", None))
#if QT_CONFIG(tooltip)
        self.inventory_search_note_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_note_checkBox.setText("")
        self.inventory_desinvoice_label.setText(QCoreApplication.translate("InventoryManager", u"Des. Inv.:", None))
#if QT_CONFIG(tooltip)
        self.inventory_search_desinvoice_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_desinvoice_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.inventory_desinvoice_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"T\u00ean mod linh ki\u1ec7n c\u1ee7a invoice", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_size_label.setText(QCoreApplication.translate("InventoryManager", u"Size:", None))
        self.inventory_material_label.setText(QCoreApplication.translate("InventoryManager", u"Mat.:", None))
#if QT_CONFIG(tooltip)
        self.inventory_length_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"T\u00ean linh ki\u1ec7n nh\u1eadp", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inventory_length_lineedit.setStatusTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp chi\u1ec1u d\u00e0i", None))
#endif // QT_CONFIG(statustip)
        self.inventory_length_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"D\u00e0i", None))
        self.input_size_label_5.setText(QCoreApplication.translate("InventoryManager", u"x", None))
#if QT_CONFIG(tooltip)
        self.inventory_width_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"T\u00ean linh ki\u1ec7n nh\u1eadp", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inventory_width_lineedit.setStatusTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp chi\u1ec1u r\u1ed9ng", None))
#endif // QT_CONFIG(statustip)
        self.inventory_width_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"R\u1ed9ng", None))
        self.input_size_label_6.setText(QCoreApplication.translate("InventoryManager", u"x", None))
#if QT_CONFIG(tooltip)
        self.inventory_height_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"T\u00ean linh ki\u1ec7n nh\u1eadp", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inventory_height_lineedit.setStatusTip(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp chi\u1ec1u cao", None))
#endif // QT_CONFIG(statustip)
        self.inventory_height_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Cao", None))
        self.input_size_label_7.setText(QCoreApplication.translate("InventoryManager", u"mm", None))
#if QT_CONFIG(tooltip)
        self.inventory_storage_location_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"Ch\u1ecdn n\u01a1i b\u1ea3o qu\u1ea3n linh ki\u1ec7n", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_component_id_label.setText(QCoreApplication.translate("InventoryManager", u"CID.:", None))
#if QT_CONFIG(tooltip)
        self.inventory_search_component_id_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_component_id_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.inventory_component_id_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"M\u00e3 s\u1ed1 linh ki\u1ec7n nh\u1eadp", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_component_id_lineedit.setInputMask("")
        self.inventory_invoice_label.setText(QCoreApplication.translate("InventoryManager", u"Invoice:", None))
#if QT_CONFIG(tooltip)
        self.inventory_search_groups_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_groups_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.inventory_search_invoice_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_invoice_checkBox.setText("")
        self.inventory_groups_label.setText(QCoreApplication.translate("InventoryManager", u"Groups:", None))
#if QT_CONFIG(tooltip)
        self.inventory_invoice_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"M\u00e3 s\u1ed1 invoice", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inventory_search_model_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_model_checkBox.setText("")
        self.inventory_model_label.setText(QCoreApplication.translate("InventoryManager", u"Model:", None))
        self.inventory_component_name_label.setText(QCoreApplication.translate("InventoryManager", u"CName.:", None))
#if QT_CONFIG(tooltip)
        self.inventory_search_component_name_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_component_name_checkBox.setText("")
        self.inventory_process_label.setText(QCoreApplication.translate("InventoryManager", u"Process:", None))
#if QT_CONFIG(tooltip)
        self.inventory_component_name_lineedit.setToolTip(QCoreApplication.translate("InventoryManager", u"T\u00ean linh ki\u1ec7n nh\u1eadp", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inventory_search_process_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_process_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.inventory_search_status_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"Cho ph\u00e9p t\u00ecm ki\u1ebfm theo \u0111i\u1ec1u ki\u1ec7n ch\u1ecdn", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_search_status_checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.inventory_filter_component_id_checkBox.setToolTip(QCoreApplication.translate("InventoryManager", u"S\u1eafp x\u1ebfp d\u1eef li\u1ec7u c\u1ed9t Component ID", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_filter_component_id_checkBox.setText("")
        self.inventory_search_button.setText(QCoreApplication.translate("InventoryManager", u"Search", None))
        self.inventory_export_button.setText(QCoreApplication.translate("InventoryManager", u"Export to Excel", None))
        ___qtablewidgetitem6 = self.inventory_data_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InventoryManager", u"ID", None));
        ___qtablewidgetitem7 = self.inventory_data_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InventoryManager", u"Component ID", None));
        ___qtablewidgetitem8 = self.inventory_data_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("InventoryManager", u"Name", None));
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabInventory), QCoreApplication.translate("InventoryManager", u"STOCK SUMMARY", None))
        self.change_logo_label.setText("")
        self.change_msnv_label.setText(QCoreApplication.translate("InventoryManager", u"-", None))
        self.change_password_old_lineedit.setInputMask("")
        self.change_password_old_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Old Password", None))
        self.change_password_new_lineedit.setInputMask("")
        self.change_password_new_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"New Password", None))
        self.change_password_new2_lineedit.setInputMask("")
        self.change_password_new2_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"New Password again", None))
        self.change_changing_button.setText(QCoreApplication.translate("InventoryManager", u"Change password", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabChangepassword), QCoreApplication.translate("InventoryManager", u"CHANGE PASSWORD", None))
        self.adduser_logo_label.setText("")
        self.adduser_msnv_lineedit.setInputMask("")
        self.adduser_msnv_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp MSNV", None))
        self.adduser_password_lineedit.setInputMask("")
        self.adduser_password_lineedit.setPlaceholderText(QCoreApplication.translate("InventoryManager", u"Nh\u1eadp Password", None))
#if QT_CONFIG(tooltip)
        self.tabadduser_level_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"Level", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tabadduser_team_combobox.setToolTip(QCoreApplication.translate("InventoryManager", u"Level", None))
#endif // QT_CONFIG(tooltip)
        self.adduser_them_button.setText(QCoreApplication.translate("InventoryManager", u"Th\u00eam", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabadduser), QCoreApplication.translate("InventoryManager", u"ADD USER", None))
        self.labelOnline.setText(QCoreApplication.translate("InventoryManager", u"Danh s\u00e1ch Online", None))
        self.chat_sent_button.setText("")
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabChat), QCoreApplication.translate("InventoryManager", u"CHAT", None))
        self.title_foot_label.setText(QCoreApplication.translate("InventoryManager", u"\u00a9 2024 WSE Company - Developed by Khoa 14-1733. For internal use only. (verson 6.1_update 2025.10.30)", None))
    # retranslateUi

