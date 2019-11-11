import networkx as nx
import pyodbc


G = nx.Graph()


# This file builds the nodes with there datas and edges!
def ConnectToDb():
    cnxn = pyodbc.connect(driver='{SQL Server}', host='(local)', database='Virtual_map', trusted_connection='yes',
                          user='', password='')
    return cnxn.cursor()


def BuildNodes(cursor):
    cursor.execute("SELECT * from Node")
    records = cursor.fetchall()
    for row in records:
        G.add_node(row[0], data=str(row[1]) + '/' + str(row[2]) + '/' + str(row[3]) + '/' + str(row[4]))


def BuildEdges(cursor):
    cursor.execute("SELECT ID1,ID2 from HotSpot")
    row = cursor.fetchone()
    while row:
        G.add_edge(row[0], row[1],wieght=1)
        row = cursor.fetchone()


def BuildAll():
    cursor = ConnectToDb()
    BuildNodes(cursor)
  #  print("Nodes of graph "": ")
   # print(G.nodes().data())
    #print(G.edges.data())
    BuildEdges(cursor)
    # nx.draw(G)
    # plt.show()
    return G

BuildAll()
