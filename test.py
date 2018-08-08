import pandas as pd
from sqlalchemy import create_engine

# engine = create_engine("postgresql://root@localhost/circle_test")

df = pd.DataFrame({"A": [1, 2]})
url = "postgresql+psycopg2://postgres@localhost/pandas_nosetest"

engine = create_engine(url)

df.to_sql('test_a', engine)
