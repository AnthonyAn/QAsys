from neo4j.v1 import GraphDatabase

uri = "bolt://123.207.231.220/:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "syl123123"))

session=driver.session()