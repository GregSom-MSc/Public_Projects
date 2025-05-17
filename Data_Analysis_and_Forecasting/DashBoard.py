import yfinance as yf
import pandas as pd
from prophet import Prophet
import plotly.express as px
import streamlit as st

# Download S&P 500 Index
df = yf.download('^GSPC', period='5y', interval='1d')

# Reset index and keep only Date and Close
df = df.reset_index()

# Flatten MultiIndex if needed
if isinstance(df.columns, pd.MultiIndex):
    df.columns = ['_'.join(col).strip() if isinstance(
        col, tuple) else col for col in df.columns]

# Rename columns to match Prophet's requirement
df = df.rename(
    columns={col: 'y' for col in df.columns if 'close' in col.lower()})
df = df.rename(
    columns={col: 'ds' for col in df.columns if 'date' in col.lower()})

# Clean up
df = df[['ds', 'y']].dropna()
df['y'] = pd.to_numeric(df['y'], errors='coerce')
df = df.dropna()

print(df.head(5))

# Step 2: Forecast with Prophet
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

# Step 3: Plot forecast
fig = px.line(forecast, x='ds', y='yhat',
              title='S&P 500 Forecast (Next 12 Months)')
fig.update_layout(
    annotations=[
        dict(
            text='Note: GSPC, 12mo forecast. SGMS 2025.',
            xref='paper', yref='paper',
            x=1.0, y=.08,  # slightly above the title
            showarrow=False,
            font=dict(size=12)
        )
    ]
)
st.plotly_chart(fig)
