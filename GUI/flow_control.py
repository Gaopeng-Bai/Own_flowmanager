# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flow_control.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_flow_control(object):
    def setupUi(self, flow_control):
        flow_control.setObjectName("flow_control")
        flow_control.resize(782, 783)
        flow_control.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(115, 210, 22);")
        self.groupBox = QtWidgets.QGroupBox(flow_control)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 211, 131))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.table_id_flow = QtWidgets.QSpinBox(self.groupBox)
        self.table_id_flow.setObjectName("table_id_flow")
        self.gridLayout.addWidget(self.table_id_flow, 2, 1, 1, 1)
        self.switch_id_flow = QtWidgets.QComboBox(self.groupBox)
        self.switch_id_flow.setObjectName("switch_id_flow")
        self.gridLayout.addWidget(self.switch_id_flow, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(flow_control)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 211, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add = QtWidgets.QRadioButton(self.groupBox_2)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.modify = QtWidgets.QRadioButton(self.groupBox_2)
        self.modify.setObjectName("modify")
        self.verticalLayout.addWidget(self.modify)
        self.modify_strict = QtWidgets.QRadioButton(self.groupBox_2)
        self.modify_strict.setObjectName("modify_strict")
        self.verticalLayout.addWidget(self.modify_strict)
        self.delete_flow = QtWidgets.QRadioButton(self.groupBox_2)
        self.delete_flow.setObjectName("delete_flow")
        self.verticalLayout.addWidget(self.delete_flow)
        self.delete_strict = QtWidgets.QRadioButton(self.groupBox_2)
        self.delete_strict.setObjectName("delete_strict")
        self.verticalLayout.addWidget(self.delete_strict)
        self.groupBox_3 = QtWidgets.QGroupBox(flow_control)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 370, 314, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.match_any = QtWidgets.QCheckBox(self.groupBox_3)
        self.match_any.setObjectName("match_any")
        self.gridLayout_2.addWidget(self.match_any, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.value_match_field = QtWidgets.QLineEdit(self.groupBox_3)
        self.value_match_field.setObjectName("value_match_field")
        self.gridLayout_2.addWidget(self.value_match_field, 2, 1, 1, 1)
        self.match_field = QtWidgets.QComboBox(self.groupBox_3)
        self.match_field.setObjectName("match_field")
        self.gridLayout_2.addWidget(self.match_field, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(flow_control)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 490, 311, 255))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.idle_timeout = QtWidgets.QLineEdit(self.groupBox_4)
        self.idle_timeout.setInputMask("")
        self.idle_timeout.setObjectName("idle_timeout")
        self.gridLayout_3.addWidget(self.idle_timeout, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.cookie = QtWidgets.QLineEdit(self.groupBox_4)
        self.cookie.setObjectName("cookie")
        self.gridLayout_3.addWidget(self.cookie, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.cookie_mask = QtWidgets.QLineEdit(self.groupBox_4)
        self.cookie_mask.setObjectName("cookie_mask")
        self.gridLayout_3.addWidget(self.cookie_mask, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.hard_timeout = QtWidgets.QLineEdit(self.groupBox_4)
        self.hard_timeout.setObjectName("hard_timeout")
        self.gridLayout_3.addWidget(self.hard_timeout, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 1)
        self.output_port = QtWidgets.QLineEdit(self.groupBox_4)
        self.output_port.setObjectName("output_port")
        self.gridLayout_3.addWidget(self.output_port, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 6, 0, 1, 1)
        self.output_group = QtWidgets.QLineEdit(self.groupBox_4)
        self.output_group.setObjectName("output_group")
        self.gridLayout_3.addWidget(self.output_group, 6, 1, 1, 1)
        self.priority = QtWidgets.QLineEdit(self.groupBox_4)
        self.priority.setObjectName("priority")
        self.gridLayout_3.addWidget(self.priority, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(flow_control)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 20, 314, 397))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.write_metadate = QtWidgets.QLineEdit(self.groupBox_5)
        self.write_metadate.setObjectName("write_metadate")
        self.gridLayout_4.addWidget(self.write_metadate, 7, 1, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 8, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_7)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)
        self.value_apply_action = QtWidgets.QLineEdit(self.groupBox_7)
        self.value_apply_action.setObjectName("value_apply_action")
        self.gridLayout_5.addWidget(self.value_apply_action, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_7)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 0, 1, 1, 1)
        self.action_type_apply = QtWidgets.QComboBox(self.groupBox_7)
        self.action_type_apply.setObjectName("action_type_apply")
        self.gridLayout_5.addWidget(self.action_type_apply, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_7, 1, 0, 3, 3)
        self.metadate_mask = QtWidgets.QLineEdit(self.groupBox_5)
        self.metadate_mask.setObjectName("metadate_mask")
        self.gridLayout_4.addWidget(self.metadate_mask, 8, 1, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 9, 0, 1, 1)
        self.goto_table = QtWidgets.QLineEdit(self.groupBox_5)
        self.goto_table.setObjectName("goto_table")
        self.gridLayout_4.addWidget(self.goto_table, 9, 1, 1, 2)
        self.clear_actions = QtWidgets.QCheckBox(self.groupBox_5)
        self.clear_actions.setObjectName("clear_actions")
        self.gridLayout_4.addWidget(self.clear_actions, 5, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.meter_id = QtWidgets.QLineEdit(self.groupBox_5)
        self.meter_id.setObjectName("meter_id")
        self.gridLayout_4.addWidget(self.meter_id, 0, 1, 1, 2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)
        self.value_write_action = QtWidgets.QLineEdit(self.groupBox_8)
        self.value_write_action.setObjectName("value_write_action")
        self.gridLayout_6.addWidget(self.value_write_action, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_8)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 1, 1, 1)
        self.action_type_write_action = QtWidgets.QComboBox(self.groupBox_8)
        self.action_type_write_action.setObjectName("action_type_write_action")
        self.gridLayout_6.addWidget(self.action_type_write_action, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_8, 6, 0, 1, 3)
        self.groupBox_6 = QtWidgets.QGroupBox(flow_control)
        self.groupBox_6.setGeometry(QtCore.QRect(380, 440, 391, 131))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.send_flowremoved_msg = QtWidgets.QCheckBox(self.groupBox_6)
        self.send_flowremoved_msg.setObjectName("send_flowremoved_msg")
        self.gridLayout_7.addWidget(self.send_flowremoved_msg, 0, 0, 1, 1)
        self.check_overlapping = QtWidgets.QCheckBox(self.groupBox_6)
        self.check_overlapping.setObjectName("check_overlapping")
        self.gridLayout_7.addWidget(self.check_overlapping, 0, 1, 2, 1)
        self.reset_counts = QtWidgets.QCheckBox(self.groupBox_6)
        self.reset_counts.setObjectName("reset_counts")
        self.gridLayout_7.addWidget(self.reset_counts, 1, 0, 2, 1)
        self.do_not_count_packets = QtWidgets.QCheckBox(self.groupBox_6)
        self.do_not_count_packets.setObjectName("do_not_count_packets")
        self.gridLayout_7.addWidget(self.do_not_count_packets, 2, 1, 1, 1)
        self.do_not_count_bytes = QtWidgets.QCheckBox(self.groupBox_6)
        self.do_not_count_bytes.setObjectName("do_not_count_bytes")
        self.gridLayout_7.addWidget(self.do_not_count_bytes, 3, 0, 1, 1)
        self.submit = QtWidgets.QPushButton(flow_control)
        self.submit.setGeometry(QtCore.QRect(380, 670, 101, 41))
        self.submit.setObjectName("submit")
        self.Clear = QtWidgets.QPushButton(flow_control)
        self.Clear.setGeometry(QtCore.QRect(580, 670, 101, 41))
        self.Clear.setObjectName("Clear")

        self.retranslateUi(flow_control)
        QtCore.QMetaObject.connectSlotsByName(flow_control)

    def retranslateUi(self, flow_control):
        _translate = QtCore.QCoreApplication.translate
        flow_control.setWindowTitle(_translate("flow_control", "Form"))
        self.groupBox.setTitle(_translate("flow_control", "Target:"))
        self.label_2.setText(_translate("flow_control", "Table ID"))
        self.label.setText(_translate("flow_control", "Switch ID"))
        self.groupBox_2.setTitle(_translate("flow_control", "Flow Operation:"))
        self.add.setText(_translate("flow_control", "add"))
        self.modify.setText(_translate("flow_control", "modify"))
        self.modify_strict.setText(_translate("flow_control", "Modify Strict"))
        self.delete_flow.setText(_translate("flow_control", "Delete "))
        self.delete_strict.setText(_translate("flow_control", "Delete Strict"))
        self.groupBox_3.setTitle(_translate("flow_control", "Match Fields:"))
        self.match_any.setText(_translate("flow_control", "Match Any"))
        self.label_3.setText(_translate("flow_control", "Match field"))
        self.label_4.setText(_translate("flow_control", "Value"))
        self.label_5.setText(_translate("flow_control", "Priority"))
        self.label_6.setText(_translate("flow_control", "Idle timeout"))
        self.idle_timeout.setPlaceholderText(_translate("flow_control", "seconds"))
        self.label_8.setText(_translate("flow_control", "Cookie"))
        self.cookie.setPlaceholderText(_translate("flow_control", "integer"))
        self.label_9.setText(_translate("flow_control", "Cookie Mask"))
        self.cookie_mask.setPlaceholderText(_translate("flow_control", "integer"))
        self.label_7.setText(_translate("flow_control", "Hard timeout"))
        self.hard_timeout.setPlaceholderText(_translate("flow_control", "seconds"))
        self.label_10.setText(_translate("flow_control", "Output Port"))
        self.output_port.setPlaceholderText(_translate("flow_control", "port number or -1 for any"))
        self.label_11.setText(_translate("flow_control", "Output Group"))
        self.output_group.setPlaceholderText(_translate("flow_control", "groud id or -1 for any"))
        self.priority.setPlaceholderText(_translate("flow_control", "entry priority"))
        self.groupBox_5.setTitle(_translate("flow_control", "Instuctions:"))
        self.write_metadate.setPlaceholderText(_translate("flow_control", "string"))
        self.label_20.setText(_translate("flow_control", "Metadata Mask:"))
        self.groupBox_7.setTitle(_translate("flow_control", "Apply action:"))
        self.label_14.setText(_translate("flow_control", "Action Type"))
        self.label_15.setText(_translate("flow_control", "Value"))
        self.metadate_mask.setPlaceholderText(_translate("flow_control", "string"))
        self.label_21.setText(_translate("flow_control", "Goto Table:"))
        self.goto_table.setPlaceholderText(_translate("flow_control", "table_id"))
        self.clear_actions.setText(_translate("flow_control", "Clear Actions"))
        self.label_19.setText(_translate("flow_control", "Write Metadate:"))
        self.label_12.setText(_translate("flow_control", "Goto Meter"))
        self.meter_id.setPlaceholderText(_translate("flow_control", "meter-id or -1 for any"))
        self.groupBox_8.setTitle(_translate("flow_control", "Write Actions:"))
        self.label_16.setText(_translate("flow_control", "Action Type"))
        self.label_17.setText(_translate("flow_control", "Value"))
        self.groupBox_6.setTitle(_translate("flow_control", "Flags"))
        self.send_flowremoved_msg.setText(_translate("flow_control", "Send flow-removed msg"))
        self.check_overlapping.setText(_translate("flow_control", "Check overlapping"))
        self.reset_counts.setText(_translate("flow_control", "Reset counts "))
        self.do_not_count_packets.setText(_translate("flow_control", "Do not count packets"))
        self.do_not_count_bytes.setText(_translate("flow_control", "Do not count bytes"))
        self.submit.setText(_translate("flow_control", "Submit"))
        self.Clear.setText(_translate("flow_control", "Clear"))
