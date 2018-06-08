url = 'postgres://kofrxrfklpeeku:38d19e37dbeaf312961fe84b0fe3dcb5ac9adc1c8b1342b2f6c7725d3e194d3d@ec2-54-204-44-140.compute-1.amazonaws.com:5432/ddcebjdne2t85m'
secret = '6d78418a981c1dadaa1798156123f488'
token = 'PxpPl5fThdhV9SzTpYkS4whB+ADwsD4HcdwD58PyjQ4cR/JjtfGlawEM2tj6fK4yWGm/AqeeKrxmcLiKxWxU3mAXPIfcR7EVBmux1Bh1FIFLLbY6q/xIyKkCdBgKYQBdUMhqZKme/ZUPXodRx5WR2AdB04t89/1O/w1cDnyilFU='

config = {
    'NAME': 'ddcebjdne2t85m', 
    'USER': 'kofrxrfklpeeku', 
    'PASSWORD': '38d19e37dbeaf312961fe84b0fe3dcb5ac9adc1c8b1342b2f6c7725d3e194d3d', 
    'HOST': 'ec2-54-204-44-140.compute-1.amazonaws.com', 
    'PORT': 5432, 
    'CONN_MAX_AGE': 0, 
    'ENGINE': 'django.db.backends.postgresql_psycopg2'
    }

import psycopg2

def get_all():
    connection = psycopg2.connect(host=config['HOST'], port=config['PORT'], database=config['NAME'], user=config['USER'], password=config['PASSWORD'])
    cur = connection.cursor()
    cur.execute("select * from reply_map")
    out = {}
    for row in cur:
        out[row[0]] = row[1]
    connection.commit()
    return out

def insert(key, value):
    connection = psycopg2.connect(host=config['HOST'], port=config['PORT'], database=config['NAME'], user=config['USER'], password=config['PASSWORD'])
    cur = connection.cursor()
    try:
        cur.execute("insert into reply_map values('{}', '{}')".format(key, value))
        connection.commit()
    except:
        pass

if __name__ == '__main__':
    connection = psycopg2.connect(host=config['HOST'], port=config['PORT'], database=config['NAME'], user=config['USER'], password=config['PASSWORD'])
    cur = connection.cursor()
    cur.execute("create table reply_map(key text not null unique, value text not null)")
    connection.commit()
