'''Created on 15 feb 2018@author: Serena Sensini'''from builtins import objectfrom sqlalchemy import Table, Column, Integer, String, Text, MetaData, create_engine, UniqueConstraint#from geoalchemy2 import Geometryfrom ..hff_system__conn_strings import Connectionfrom ...utility.hff_system__OS_utility import Hff_OS_Utilityclass Site_line_table(object):    # connection string postgres"    internal_connection = Connection()    # create engine and metadata    engine = create_engine(internal_connection.conn_str(), echo=True, convert_unicode=True)    metadata = MetaData(engine)    # define tables    siteline = Table('site_line', metadata,                       Column('id', Integer, primary_key=True),                                              Column('location', Text),                       Column('name_f_l', Text),                       Column('photo1', String(200)),                       Column('photo2', String(200)),                       Column('photo3', String(200)),                       Column('photo4', String(200)),                       Column('photo5', String(200)),                       Column('photo6', String(200)),                                              Column('the_geom', Text),#Geometry('MULTIPOLYGON',-1)),                       Column('coord', Text),                       # explicit/composite unique constraint.  'name' is optional.                       UniqueConstraint('name_f_l','location', name='ID_sito_line_unico')                       )    metadata.create_all(engine)