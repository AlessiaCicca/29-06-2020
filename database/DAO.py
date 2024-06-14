from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.partita import Partita


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi(mese):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from matches m 
        where month (m.`Date`)=%s"""

        cursor.execute(query,(mese,))

        for row in cursor:
            result.append(Partita(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni(minuti):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct m2,m1, count(distinct g2) as peso
from (select a.PlayerID as g2 ,a.MatchID as m2
from actions a 
where a.TimePlayed>%s)as t2,(select a.PlayerID as g1 ,a.MatchID as m1
from actions a 
where a.TimePlayed>%s)as t1
where t2.g2=t1.g1 and t2.m2!=t1.m1 
group by m2,m1 """

        cursor.execute(query,(minuti,minuti,))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getMatch():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from matches m 
        """

        cursor.execute(query)

        for row in cursor:
            result.append(Partita(**row))

        cursor.close()
        conn.close()
        return result
