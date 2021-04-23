import mysql.connector
from data import EnsembleClass


class EnsembleDatabaseConnector:

    def __init__(self):
        self.conn = mysql.connector.connect(host="ensembldb.ensembl.org",
                                            user='anonymous',
                                            password='',
                                            db='homo_sapiens_core_98_38')

    def searchGenes(self, zoekTerm):
        cursor = self.conn.cursor()

        cursor.execute(f"select gene_id,"
                       f"seq_region_start,"
                       f"seq_region_end,"
                       f"seq_region_strand,"
                       f"description from gene where description "
                       f"like '%{zoekTerm}%'")

        return self.makeObjects(cursor)

    def makeObjects(self, cursor):
        resultList = []

        for i in cursor:
            resultList.append(EnsembleClass(i[0], i[1], i[2], i[3], i[4]))

        resultList.sort()
        return resultList
