import pymysql
import os
from dotenv import load_dotenv
load_dotenv()
from itemadapter import ItemAdapter

class CostcoOnlinePipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host="localhost",
            user=os.environ['MYSQLUSER'],
            passwd=os.environ['MYSQLPASS'],
            database="cotlog",
            charset="utf8mb4"
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        # 重複チェック
        check_title_id = item["Item_Number"]
        find_qry = "SELECT `item_number` FROM `costco_online` WHERE `item_number` = %s"
        is_done = self.cursor.execute(find_qry, check_title_id)

        # 登録先分岐
        if (is_done == 0):
            insert_qry = "INSERT INTO `costco_online` (`item_number`, `category`, `sub_category`, `title`, `price`, `description`, `url`, `img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        else:
            insert_qry = "INSERT INTO `duplication_item_number` (`item_number`, `category`, `sub_category`, `title`, `price`, `description`, `url`, `img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            
        self.cursor.execute(insert_qry, (item["Item_Number"], item["category"], item["sub_category"], item["title"], item["price"], item["description"], item["url"], item["img"]))
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.connection.close()
