from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import sys
from db.get_postgres_con import get_values_video_details


class TableView(QTableWidget):
    def __init__(self, data):
        super(TableView, self).__init__()
        self.data = data
        self.setData()
        self.resize(500, 300)

    def setData(self):
        row_count = (len(self.data))
        column_count = (len(self.data[0]))

        self.setColumnCount(column_count)
        self.setRowCount(row_count)

        self.setHorizontalHeaderLabels((list(self.data[0].keys())))

        for row in range(row_count):  # add items from array to QTableWidget
            for column in range(column_count):
                item = (list(self.data[row].values())[column])
                self.setItem(row, column, QTableWidgetItem(str(item)))

# def main():
#     vid_details_list = get_values_video_details('123')
#     final_vid_details_list = []
#     for item in vid_details_list:
#         item_list = list(item)
#         item_list.pop(0)
#         item_list.pop(4)
#         final_vid_details_list.append(tuple(item_list))
#     print(final_vid_details_list)
#
#     vid_details_dict_key_list = ['vid_id', 'vid_tag', 'sec_key', 'sec_msg']
#
#     final_vid_details_dict = []
#
#     for val in final_vid_details_list:
#         vid_details_dict = dict(zip(vid_details_dict_key_list, val))
#         final_vid_details_dict.append(vid_details_dict)
#
#     print(final_vid_details_dict)

# app = QApplication(sys.argv)
# table = TableView(final_vid_details_dict)
# table.show()
# sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()
