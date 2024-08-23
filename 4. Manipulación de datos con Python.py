#4. Manipulación de datos con Python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://usuario:contraseña@host:puerto/base_de_datos')
query = "SELECT order_id, amount_total, customer_name FROM orden_venta"
df = pd.read_sql(query, engine)
df_filtro = df[df['amount_total'] > 1000]

print(df_filtro)