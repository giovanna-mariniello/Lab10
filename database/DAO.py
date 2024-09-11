from database.DB_connect import DBConnect
from model.stato import Stato
from model.confine import Confine


class DAO():

    @staticmethod
    def getAllStati(anno):
        cnx = DBConnect.get_connection()

        result = []

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT c.CCode, c.StateAbb, c.StateNme
                    FROM country c, contiguity c1
                    WHERE c1.'year' <= %s
                    AND c1.state1no = c.CCode
                    GROUP BY c.state1no
                    ORDER BY StateAbb
                    """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        cnx.close()

        return result

    @staticmethod
    def getAllConfini(id_map_stati, anno):
        cnx = DBConnect.get_connection()

        result = []

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT c.state1no, c.state2no
                    FROM contiguity c
                    WHERE c.'year' <= %s AND c.conttype = 1 """

        cursor.execute(query, (anno,))

        for row in cursor:
            s1 = id_map_stati[row["state1no"]]
            s2 = id_map_stati[row["state2no"]]

            if s1 is not None and s2 is not None:
                result.append(Confine(s1, s2))

        cursor.close()
        cnx.close()

        return result





