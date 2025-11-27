import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap


from qt_py.form_vxod import Form_vxod
from qt_py.widget_adm import Wi_adm
from qt_py.add_task import Add_task
from qt_py.widget_rab import Wi_rab
from qt_py.delete_task import Delete_tsk
from qt_py.izmen_task import Ui_izmen
from orm_k import Department, User, Task,Session

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form_vxod()
        self.ui.setupUi(self)


class RabWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Wi_rab()
        self.ui.setupUi(self)

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Wi_adm()
        self.ui.setupUi(self)

class Add_t(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Add_task()
        self.ui.setupUi(self)

class Delete_tske(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Delete_tsk()
        self.ui.setupUi(self)
class Izmen_tsk(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_izmen()
        self.ui.setupUi(self)

class AppManager:
    def __init__(self):
        self.login_window = LoginWindow()
        self.rab_window = RabWindow()
        self.adm_window = AdminWindow()
        self.aad = Add_t()
        self.dele = Delete_tske()
        self.izm = Izmen_tsk()

# |||||||||||||||||||||  Подключение кнопок |||||||||||||||||||||||||||
        #|||||||||||||||||||||||||||||||||||  show, hide |||||||||||||||||||||||||||||||||||||||||||



        self.rab_window.ui.exit_avtoriz.clicked.connect(self.show_login_window_rab)
        self.adm_window.ui.exit_avtoriz.clicked.connect(self.show_login_window_adm)

        self.login_window.ui.vxod_butt.clicked.connect(self.vxod_akk)

        self.adm_window.ui.add_deadlines.clicked.connect(self.ad_dlshow)
        self.adm_window.ui.delete_deadlines.clicked.connect(self.del_dlshow)
        self.aad.ui.exit_save.clicked.connect(self.hide_ad)
        self.dele.ui.exit_del.clicked.connect(self.del_dlhide)
        self.adm_window.ui.btm_izmen_dead.clicked.connect(self.show_izm)
        self.izm.ui.exit_izmm.clicked.connect(self.hide_izm)


        #|||||||||||||||||||||||||||||||||||||||| кнопки работника  ||||||||||||||||||||||||||||||||||||||||||||||||
        self.load_com_box_rab()
        self.setup_cal_con_rab()
        self.load_combox_sot_rab()

        #self.rab_window.ui.look_info_text.clicked.connect(self.vid_inf_rad)

        # |||||||||||||||||||||||||||||||||||||||| кнопки администратора ||||||||||||||||||||||||||||||||||||||||||||||||
        self.load_com_box_adm()
        self.load_combox_sot_adm()
        self.settup_cal_con_adm()
        self.aad.ui.save_add.clicked.connect(self.create_new)
        self.load_com_box_add_rab()
        self.load_com_box_add_otdel()
        self.load_com_box_del()
        self.load_com_box_izm_otdel()
        self.dele.ui.dateEdit_del.dateChanged.connect(self.del_vv_text)
        self.dele.ui.joi_otdel_for_admin_del.currentTextChanged.connect(self.del_vv_text)
        self.dele.ui.joi_sotr_for_admin_del.currentTextChanged.connect(self.del_vv_text)

        self.dele.ui.save_delete.clicked.connect(self.del_st)
        self.izm.ui.dateEdit_izm.dateChanged.connect(self.izm_vv_text)
        self.izm.ui.joi_sotr_for_admin_izm.currentTextChanged.connect(self.izm_vv_text)
        self.izm.ui.joi_otdel_for_admin_izm.currentTextChanged.connect(self.izm_vv_text)
        self.izm.ui.izm_task.itemClicked.connect(self.on_izm_task_selected)
        self.izm.ui.save_izm.clicked.connect(self.save_izm)
        self.load_com_box_dele_rab()
        self.load_combox_rab_izm()

#||||||||||||||||||||||||  Переключение между формами show, hide ||||||||||||||||||||||||||||
    def vxod_akk(self):
        login = self.login_window.ui.textEdit_login.toPlainText()
        pasword = self.login_window.ui.textEdit_pasword.toPlainText()

        if not login or not pasword:
            QMessageBox.information(self.login_window, "Ошибка", "Введите логин и пароль!")
            return
        session = Session()
        try:
            user = session.query(User).filter_by(login=login,password=pasword).first()
            if user:
                if user.role == "admin":
                    self.adm_window.show()
                    self.adm_window.ui.name.clear()
                    self.adm_window.ui.doljnost.clear()
                    namee = f'{user.login}'
                    rolee = f"{user.role}"
                    self.adm_window.ui.doljnost.setText(rolee)
                    self.adm_window.ui.name.setText(namee)
                    self.adm_window.ui.avatar.setPixmap(QPixmap("path/avatar_kik.png"))
                    self.login_window.hide()
                else:
                    self.rab_window.ui.doljnost.clear()
                    self.rab_window.ui.avatar.setPixmap(QPixmap("path/avatar_kiv.png"))
                    self.rab_window.ui.name.clear()
                    nameee = f'{user.login}'
                    roleee = f"{user.role}"
                    self.rab_window.ui.doljnost.setText(roleee)
                    self.rab_window.ui.name.setText(nameee)
                    self.rab_window.show()
                    self.login_window.hide()
            else:
                QMessageBox.information(self.login_window, "Ошибка", "Пользователь не найден, повторите еще раз!")

            self.login_window.ui.textEdit_login.clear()
            self.login_window.ui.textEdit_pasword.clear()
        finally:
            session.close()

    def show_login_window_adm(self):
        self.adm_window.hide()
        self.login_window.show()
    def show_login_window_rab(self):
        self.rab_window.hide()
        self.login_window.show()

    def ad_dlshow(self):
        self.aad.show()
    def startshow(self):
        self.login_window.show()
    def del_dlshow(self):
        self.dele.show()
    def hide_ad(self):
        self.aad.hide()
    def del_dlhide(self):
        self.dele.hide()
    def show_izm(self):
        self.izm.show()
    def hide_izm(self):
        self.izm.hide()

#||||||||||| функции кнопок у работника: комбобокс, вывести ||||||||||||||||||||
    def setup_cal_con_rab(self):
        self.rab_window.ui.calendarWidget.selectionChanged.connect(self.vid_inf_rad)
        self.rab_window.ui.joi_otdel_for_admin.currentTextChanged.connect(self.vid_inf_rad)
        self.vid_inf_rad()

    def vid_inf_rad(self):
        session = Session()
        try:
            self.rab_window.ui.text_vv.clear()
            select_dept = self.rab_window.ui.joi_otdel_for_admin.currentText()
            select_date = self.rab_window.ui.calendarWidget.selectedDate()
            py_date = select_date.toPython()
            departament = session.query(Department).filter_by(name=select_dept).first()
            select_rab = self.rab_window.ui.joi_sotr_for_rab.currentText()
            rabot = session.query(User).filter_by(login=select_rab).first()
            if departament and rabot:
                tasks = session.query(Task).filter(Task.department_id == departament.id,
                                                   Task.deadline == py_date,
                                                   Task.assigned_to_id == rabot.id).all()
            elif not rabot and departament:
                tasks = session.query(Task).filter(Task.department_id == departament.id,
                                                   Task.deadline == py_date).all()
            elif rabot and not departament:
                tasks = session.query(Task).filter(Task.deadline == py_date,
                                                   Task.assigned_to_id == rabot.id).all()
            else:
                tasks = session.query(Task).filter(Task.deadline == py_date).all()

            if tasks:
                for task in tasks:
                    task_info = f"{task.title} \n{task.description}"
                    self.rab_window.ui.text_vv.addItem(task_info)
            else:
                self.rab_window.ui.text_vv.addItem("Задач нет.")
        finally:
            session.close()
    def load_com_box_rab(self):
        self.rab_window.ui.joi_otdel_for_admin.clear()
        session = Session()
        try:
            departments = session.query(Department).all()
            dept_names = [dept.name for dept in departments]
            self.rab_window.ui.joi_otdel_for_admin.addItems(dept_names)
        finally:
            session.close()

    def load_combox_sot_rab(self):
        self.rab_window.ui.joi_sotr_for_rab.clear()
        session = Session()
        try:
            sotryd = session.query(User).all()
            sotr_name = [rab.login for rab in sotryd]
            self.rab_window.ui.joi_sotr_for_rab.addItems(sotr_name)
        finally:
            session.close()

# ||||||||||| функции кнопок у админа: комбобокс, вывести ||||||||||||||||||||||

    # |||||||||||||||||||||||| выгрузка данных |||||||||||||||||||||||||||||||||||


    def settup_cal_con_adm(self):
        self.adm_window.ui.calendarWidget.selectionChanged.connect(self.vid_inf_adm)
        self.adm_window.ui.joi_otdel_for_admin.currentTextChanged.connect(self.vid_inf_adm)

    def vid_inf_adm(self):
        session = Session()
        try:
            self.adm_window.ui.text_vv.clear()
            select_dept = self.adm_window.ui.joi_otdel_for_admin.currentText()
            select_date = self.adm_window.ui.calendarWidget.selectedDate()
            py_date = select_date.toPython()
            departament = session.query(Department).filter_by(name=select_dept).first()

            select_rab = self.adm_window.ui.joi_sotr_for_admin.currentText()
            rabot = session.query(User).filter_by(login=select_rab).first()
            if departament and rabot:
                    tasks = session.query(Task).filter(Task.department_id == departament.id,
                                                       Task.deadline == py_date,
                                                       Task.assigned_to_id == rabot.id).all()
            elif not rabot and departament:
                    tasks = session.query(Task).filter(Task.department_id == departament.id,
                                                       Task.deadline == py_date).all()
            elif rabot and not departament:
                    tasks = session.query(Task).filter(Task.deadline == py_date,
                                                       Task.assigned_to_id == rabot.id).all()
            else:
                    tasks = session.query(Task).filter(Task.deadline == py_date).all()

            if tasks:
                    for task in tasks:
                        task_info = f"{task.title} \n{task.description}"
                        self.adm_window.ui.text_vv.addItem(task_info)
            else:
                   self.adm_window.ui.text_vv.addItem("Задач нет.")
        finally:
            session.close()

    def load_com_box_adm(self):
        self.adm_window.ui.joi_otdel_for_admin.clear()
        session = Session()
        try:
            departments = session.query(Department).all()
            dept_names = [dept.name for dept in departments]
            self.adm_window.ui.joi_otdel_for_admin.addItems(dept_names)
        finally:
            session.close()

    def load_combox_sot_adm(self):
        self.adm_window.ui.joi_sotr_for_admin.clear()
        session = Session()
        try:
            sotryd = session.query(User).all()
            sotr_name = [rab.login for rab in sotryd]
            self.adm_window.ui.joi_sotr_for_admin.addItems(sotr_name)
        finally:
            session.close()


    # ||||||||||| функции кнопок у админа: добавить изменить удалить ||||||||||||||||||||||

    #|||||||||||||||||||||||||||||| Добавить  ||||||||||||||||||||

    def load_com_box_add_otdel(self):
        self.aad.ui.joi_otdel_for_admin_add.clear()
        session = Session()
        try:
            departments = session.query(Department).all()
            dept_names = [dept.name for dept in departments]
            self.aad.ui.joi_otdel_for_admin_add.addItems(dept_names)
        finally:
            session.close()

    def load_com_box_add_rab(self):
        self.aad.ui.joi_sotrud_for_admin_add.clear()
        session = Session()
        try:
            sotryd = session.query(User).all()
            sotr_name = [rab.login for rab in sotryd]
            self.aad.ui.joi_sotrud_for_admin_add.addItems(sotr_name)
        finally:
            session.close()

    def create_new(self):
        session  = Session()
        try:
            select_dept = self.aad.ui.joi_otdel_for_admin_add.currentText()
            departament = session.query(Department).filter_by(name=select_dept).first()
            title_text = self.aad.ui.add_task_title.toPlainText().strip()
            descp_text = self.aad.ui.add_task_descrip.toPlainText().strip()
            select_date = self.aad.ui.dateEdit_add.date()
            py_date = select_date.toPython()
            select_rab = self.aad.ui.joi_sotrud_for_admin_add.currentText()
            rabot = session.query(User).filter_by(login = select_rab).first()
            task =  Task(title = title_text,description = descp_text, deadline = py_date,assigned_to_id = rabot.id,department_id=departament.id)
            session.add(task)
            session.commit()
            QMessageBox.information(self.aad,"Успех","Задача успешно добавлена!")
            self.aad.ui.add_task_title.clear()
            self.aad.ui.add_task_descrip.clear()
        finally:
            session.close()
        self.vid_inf_adm()


    #|||||||||||||||||||||||| удалить  |||||||||||||||||||||||||||||||||||
    def load_com_box_dele_rab(self):
        self.dele.ui.joi_sotr_for_admin_del.clear()
        session = Session()
        try:
            sotryd = session.query(User).all()
            sotr_name = [rab.login for rab in sotryd]
            self.dele.ui.joi_sotr_for_admin_del.addItems(sotr_name)
        finally:
            session.close()

    def load_com_box_del(self):
        self.dele.ui.joi_otdel_for_admin_del.clear()
        session = Session()
        try:
            departments = session.query(Department).all()
            dept_names = [dept.name for dept in departments]
            self.dele.ui.joi_otdel_for_admin_del.addItems(dept_names)
        finally:
            session.close()

    def del_vv_text(self):
        session = Session()
        try:
            self.dele.ui.listView_del.clear()
            select_dept = self.dele.ui.joi_otdel_for_admin_del.currentText()
            select_date = self.dele.ui.dateEdit_del.date()
            py_date = select_date.toPython()
            departament = session.query(Department).filter_by(name=select_dept).first()
            select_rab = self.dele.ui.joi_sotr_for_admin_del.currentText()
            rabot = session.query(User).filter_by(login = select_rab).first()
            if not departament or not rabot:
                self.dele.ui.listView_del.addItem("Выберите отдел и сотрудника")
                return
            if departament and rabot:
                    tasks = session.query(Task).filter(
                        Task.department_id == departament.id,
                        Task.deadline == py_date,
                        Task.assigned_to_id == rabot.id
                    ).all()

                    if tasks:
                        self.tasks_for_deletion = tasks
                        for task in tasks:
                            task_info = f"{task.title}"
                            self.dele.ui.listView_del.addItem(task_info)
                    else:
                        self.dele.ui.listView_del.addItem("Задач нет.")
        finally:
            session.close()

    def del_st(self):
        select_items = self.dele.ui.listView_del.selectedItems()
        if not select_items:
            QMessageBox.information(self.dele,"Ошибка", "Выберите задание")
        select_item = select_items[0]
        select_index = self.dele.ui.listView_del.row(select_item)
        if select_index < len(self.tasks_for_deletion):
            task_to_del = self.tasks_for_deletion[select_index]
        session = Session()
        try:
            task = session.query(Task).filter_by(id=task_to_del.id).first()
            if task:
                session.delete(task)
                session.commit()
                self.del_vv_text()
                QMessageBox.information(self.izm, "Успех", "Задача успешно удалена!")

        finally:
            session.close()
        self.vid_inf_adm()

    #|||||||||||||||||||||||||||||| Изменить ||||||||||||||||||||||||||||||||||||||||||||

    def load_com_box_izm_otdel(self):
        self.izm.ui.joi_otdel_for_admin_izm.clear()
        session = Session()
        try:
            depatamens = session.query(Department).all()
            dep_names = [dept.name for dept in depatamens]
            self.izm.ui.joi_otdel_for_admin_izm.addItems(dep_names)
        finally:
            session.close()
    def load_combox_rab_izm(self):
        self.izm.ui.joi_sotr_for_admin_izm.clear()
        session = Session()
        try:
            sotryd = session.query(User).all()
            sotr_name = [rab.login for rab in sotryd]
            self.izm.ui.joi_sotr_for_admin_izm.addItems(sotr_name)
        finally:
            session.close()

    def izm_vv_text(self):
        session = Session()
        try:
            self.izm.ui.izm_task.clear()
            select_dept = self.izm.ui.joi_otdel_for_admin_izm.currentText()
            select_date = self.izm.ui.dateEdit_izm.date()
            py_date = select_date.toPython()
            departament = session.query(Department).filter_by(name=select_dept).first()
            select_rab = self.izm.ui.joi_sotr_for_admin_izm.currentText()
            rabot = session.query(User).filter_by(login=select_rab).first()
            if not departament or not rabot:
                self.izm.ui.izm_task.addItem("Выберите отдел и сотрудника")
                return
            if departament and rabot:
                tasks = session.query(Task).filter(Task.deadline == py_date,Task.department_id == departament.id,Task.assigned_to_id == rabot.id).all()
                if tasks:
                    self.tasks_for_ism = tasks
                    for task in tasks:
                        task_info = f"{task.title}"
                        self.izm.ui.izm_task.addItem(task_info)
                else:
                    self.izm.ui.izm_task.addItem("Задач нет.")
        finally:
            session.close()

    def on_izm_task_selected(self,item):
        select_items = self.izm.ui.izm_task.selectedItems()
        if not select_items:
            QMessageBox.information(self.dele,"Ошибка", "Выберите задание")
        select_item = select_items[0]
        select_index = self.izm.ui.izm_task.row(select_item)
        if select_index < len(self.tasks_for_ism):
            self.task_to_izm = self.tasks_for_ism[select_index]
        session = Session()
        try:
            task = session.query(Task).filter_by(id = self.task_to_izm.id).first()
            if task:
                task_info = f"{task.description}"
                self.izm.ui.izm_task_descrip.setText(task_info)
        finally:
            session.close()

    def save_izm(self):
        session = Session()
        try:
            task = session.query(Task).filter_by(id=self.task_to_izm.id).first()
            if task:
                new_desc = self.izm.ui.izm_task_descrip.toPlainText().strip()
                task.description = new_desc
                session.commit()
                self.izm_vv_text()
                QMessageBox.information(self.izm, "Успех", "Задача успешно изменена!")
        finally:
            session.close()
        self.vid_inf_adm()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = AppManager()
    manager.startshow()
    sys.exit(app.exec())