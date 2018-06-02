class Status(object):
    @classmethod
    def convert_dic(cls, status_array):
        return dict(
            user_id=status_array[0],
            name=status_array[1],
            obesity=status_array[2],
            serious=status_array[3],
            hot=status_array[4],
            strong=status_array[5],
            kind=status_array[6]
        )

    @classmethod
    def select_from(cls, db, user_id):
        status = db.execute('select * from statuses where user_id=(?)', [user_id]).fetchone()
        return cls.convert_dic(status)

    def insert_to(self, db):
        cursor = db.cursor()
        cursor.execute('insert into statuses values (?, ?, ?, ?, ?, ?, ?)', [self.user_id, "charname", 0, 0, 0, 0, 0])
        db.commit()
        return self.user_id

    def __init__(self, user_id, name, obesity, serious, hot, strong, kind):
        self.user_id = user_id
        self.name = name
        self.obesity = obesity
        self.serious = serious
        self.hot = hot
        self.strong = strong
        self.kind = kind
