sql_select = "select * from institution where status = 'A'"
sql_select_id = "select * from institution where status = 'A' and id = :id"




class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def get_institution_by_id(self, id):
        with self.session_factory() as session:
            result = session.execute(sql_select_id, {"id":id})
            row = result.fetchone()
            return row