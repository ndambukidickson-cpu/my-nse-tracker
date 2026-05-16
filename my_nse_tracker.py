import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.title("📈 Live Nairobi Securities Exchange Portfolio Tracker")
st.markdown("### Powered by Live Market Signals")

# 1. Complete Database of Active NSE Listings (Grouped by Sector)
nse_data = {
    # TELECOMMUNICATIONS
    "SCOM":   {"name": "Safaricom Plc", "price": 30.05, "change": -0.45, "score": 4.2},
    
    # BANKING
    "ABSA":   {"name": "Absa Bank Kenya Plc", "price": 28.75, "change": -0.35, "score": 4.3},
    "BKG":    {"name": "BK Group Plc", "price": 51.50, "change": -1.00, "score": 4.0},
    "DTK":    {"name": "Diamond Trust Bank Kenya", "price": 149.25, "change": -0.25, "score": 4.1},
    "EQTY":   {"name": "Equity Group Holdings", "price": 75.00, "change": 0.00, "score": 4.7},
    "HFCK":   {"name": "HF Group Ltd", "price": 9.24, "change": -0.08, "score": 3.2},
    "IMH":    {"name": "I&M Group Plc", "price": 50.25, "change": 0.00, "score": 4.2},
    "KCB":    {"name": "KCB Group Plc", "price": 66.75, "change": 0.00, "score": 4.7},
    "NCBA":   {"name": "NCBA Group Plc", "price": 88.50, "change": 0.00, "score": 4.8},
    "SBIC":   {"name": "Stanbic Holdings Plc", "price": 294.50, "change": -0.75, "score": 4.4},
    "SCBK":   {"name": "Standard Chartered Bank", "price": 341.25, "change": +2.50, "score": 4.6},
    "COOP":   {"name": "Co-operative Bank of Kenya", "price": 32.50, "change": -0.15, "score": 4.4},

    # ENERGY & PETROLEUM
    "KEGN":   {"name": "KenGen Plc", "price": 9.18, "change": 0.00, "score": 4.1},
    "KPLC":   {"name": "Kenya Power & Lighting", "price": 15.35, "change": -0.35, "score": 3.0},
    "TOTL":   {"name": "TotalEnergies Marketing", "price": 45.45, "change": -0.20, "score": 4.2},
    "UMME":   {"name": "Umeme Ltd", "price": 7.32, "change": 0.00, "score": 3.8},

    # MANUFACTURING & ALLIED
    "BAT":    {"name": "British American Tobacco", "price": 513.00, "change": -3.00, "score": 4.5},
    "BOC":    {"name": "BOC Kenya Ltd", "price": 158.00, "change": +1.75, "score": 3.9},
    "CARB":   {"name": "Carbacid Investments", "price": 29.55, "change": +0.15, "score": 4.0},
    "EABL":   {"name": "East African Breweries", "price": 243.25, "change": +6.25, "score": 4.3},
    "EVRD":   {"name": "Eveready East Africa", "price": 1.13, "change": -0.01, "score": 1.5},
    "UNGA":   {"name": "Unga Group Ltd", "price": 27.00, "change": +0.10, "score": 3.1},

    # AGRICULTURAL
    "EGAD":   {"name": "Eaagads Ltd", "price": 34.25, "change": +2.65, "score": 3.4},
    "KUKZ":   {"name": "Kakuzi Plc", "price": 417.50, "change": +0.75, "score": 4.0},
    "KAPC":   {"name": "Kapchorua Tea Company", "price": 256.00, "change": +2.50, "score": 4.1},
    "LIMT":   {"name": "Limuru Tea Company", "price": 480.00, "change": 0.00, "score": 3.5},
    "SASN":   {"name": "Sasini Plc", "price": 28.50, "change": -0.15, "score": 3.6},
    "WTK":    {"name": "Williamson Tea Kenya", "price": 135.00, "change": +1.75, "score": 4.2},

    # COMMERCIAL AND SERVICES
    "XPRS":   {"name": "Express Kenya Ltd", "price": 7.06, "change": +0.06, "score": 2.1},
    "KQ":     {"name": "Kenya Airways Ltd", "price": 6.22, "change": -0.08, "score": 1.5},
    "LKL":    {"name": "Longhorn Publishers Ltd", "price": 2.83, "change": -0.24, "score": 3.0},
    "NMG":    {"name": "Nation Media Group", "price": 13.15, "change": -0.05, "score": 3.5},
    "SCAN":   {"name": "WPP Scangroup Plc", "price": 2.15, "change": 0.00, "score": 2.8},
    "SGL":    {"name": "Standard Group Ltd", "price": 6.42, "change": +0.38, "score": 2.0},
    "TPSE":   {"name": "TPS Eastern Africa (Serena)", "price": 15.60, "change": -0.20, "score": 3.2},
    "UCHM":   {"name": "Uchumi Supermarket", "price": 1.73, "change": -0.06, "score": 1.2},

    # CONSTRUCTION & ALLIED
    "BAMB":   {"name": "Bamburi Cement PLC", "price": 54.00, "change": 0.00, "score": 3.8},
    "CRWN":   {"name": "Crown Paints Kenya PLC", "price": 62.25, "change": +0.50, "score": 3.7},
    "CABL":   {"name": "East African Cables PLC", "price": 1.71, "change": 0.00, "score": 2.2},
    "PORT":   {"name": "E.A. Portland Cement", "price": 78.00, "change": +0.50, "score": 2.5},

    # INSURANCE
    "BRIT":   {"name": "Britam Holdings Ltd", "price": 12.50, "change": -0.05, "score": 3.6},
    "CIC":    {"name": "CIC Insurance Group", "price": 4.22, "change": -0.09, "score": 3.5},
    "JUB":    {"name": "Jubilee Holdings Ltd", "price": 372.25, "change": -7.75, "score": 4.4},
    "KNRE":   {"name": "Kenya Re-Insurance Corp", "price": 3.35, "change": -0.01, "score": 3.9},
    "LBTY":   {"name": "Liberty Kenya Holdings", "price": 9.80, "change": -0.04, "score": 3.4},
    "SLAM":   {"name": "Sanlam Kenya Plc", "price": 8.60, "change": -0.22, "score": 2.6},

    # INVESTMENT & INVESTMENT SERVICES
    "CTUM":   {"name": "Centum Investment Co", "price": 13.85, "change": +0.20, "score": 3.6},
    "NSE":    {"name": "Nairobi Securities Exchange", "price": 19.85, "change": 0.00, "score": 4.4},
    "OCH":    {"name": "Olympia Capital Holdings", "price": 6.94, "change": +0.10, "score": 2.9},
    "TCL":    {"name": "TransCentury Plc", "price": 1.12, "change": 0.00, "score": 1.8},
    "HAFR":   {"name": "Home Afrika Ltd", "price": 1.34, "change": 0.00, "score": 1.6},
    "NBV":    {"name": "Nairobi Business Ventures", "price": 1.36, "change": +0.01, "score": 2.7},
    "CGEN":   {"name": "Car & General Kenya PLC", "price": 79.25, "change": 0.00, "score": 3.8}
}

# 2. Your actual verified stock holding balances
my_portfolio = {
    "KCB":    {"shares": 8,    "my_buy_price": 40.00, "yf_ticker": "KCB.KE"},
    "KEGN":   {"shares": 30,   "my_buy_price": 4.00,  "yf_ticker": "KEGN.KE"},
    "LKL":    {"shares": 150,  "my_buy_price": 3.10,  "yf_ticker": "LKL.KE"},
    "NCBA":   {"shares": 9,    "my_buy_price": 41.50, "yf_ticker": "NCBA.KE"},
    "NSE":    {"shares": 31,   "my_buy_price": 8.20,  "yf_ticker": "NSE.KE"},
    "UCHM":   {"shares": 200,  "my_buy_price": 0.30,  "yf_ticker": "UCHM.KE"},
    "COOP":   {"shares": 10,   "my_buy_price": 13.00, "yf_ticker": "COOP.KE"},
    "ABSA":   {"shares": 5,    "my_buy_price": 14.00, "yf_ticker": "ABSA.KE"},
    "SCOM":   {"shares": 700,  "my_buy_price": 29.50, "yf_ticker": "SCOM.KE"}
}

# 3. Process Live Data Download & Math Operations
portfolio_rows = []
total_invested_capital = 0.0
total_current_portfolio_value = 0.0

st.info("🔄 Connecting to market order books and downloading live prices...")

for ticker, details in my_portfolio.items():
    try:
        stock_ticker_data = yf.Ticker(details["yf_ticker"])
        live_price_history = stock_ticker_data.history(period="1d")
        
        if not live_price_history.empty:
            market_price = float(live_price_history['Close'].iloc[-1])
        else:
            market_price = details["my_buy_price"]
            
        fundamental_score = nse_data[ticker]["score"]
        
        total_cost = details["shares"] * details["my_buy_price"]
        current_value = details["shares"] * market_price
        profit_or_loss = current_value - total_cost
        
        total_invested_capital += total_cost
        total_current_portfolio_value += current_value
        
        if fundamental_score <= 2.2:
            signal = "🚨 LIQUIDATE / AVOID"
        elif market_price < details["my_buy_price"] * 0.95 and fundamental_score >= 4.2:
            signal = "🟢 BUY THE DIP"
        elif market_price > details["my_buy_price"] * 1.25:
            signal = "💰 TAKE PROFIT"
        else:
            signal = "⏳ HOLD"
            
        portfolio_rows.append({
            "Ticker": ticker,
            "Shares": details["shares"],
            "Avg Cost": details["my_buy_price"],
            "Live Market Price": market_price,
            "Current Value": current_value,
            "Profit / Loss": profit_or_loss,
            "Tactical Action": signal
        })
    except Exception as error_msg:
        st.warning(f"Could not load live updates for {ticker}.")

# 4. Display the Clean Executive Dashboard Overview
if portfolio_rows:
    df_portfolio = pd.DataFrame(portfolio_rows)
    
    # Financial KPI summary cards
    col1, col2, col3 = st.columns(3)
    net_gain_loss = total_current_portfolio_value - total_invested_capital
    gain_percentage = (net_gain_loss / total_invested_capital * 100) if total_invested_capital > 0 else 0.0
    
    col1.metric("Total Value", f"KSh {total_current_portfolio_value:,.2f}")
    col2.metric("Total Invested", f"KSh {total_invested_capital:,.2f}")
    col3.metric("Net Return", f"KSh {net_gain_loss:,.2f}", f"{gain_percentage:+.2f}%")
    
    st.write("---")
    
    # Display table for active holdings
    df_display = df_portfolio.copy()
    df_display["Avg Cost"] = df_display["Avg Cost"].map("KSh {:.2f}".format)
    df_display["Live Market Price"] = df_display["Live Market Price"].map("KSh {:.2f}".format)
    df_display["Current Value"] = df_display["Current Value"].map("KSh {:,.2f}".format)
    df_display["Profit / Loss"] = df_display["Profit / Loss"].map("KSh {:+,.2f}".format)
    
    st.subheader("📊 My Active Portfolio Summary")
    st.dataframe(df_display, use_container_width=True, hide_index=True)
    
    st.write("---")
    
    # 5. Mobile Responsive Bar Graph Layout
    st.subheader("📊 Capital Distribution Breakdown")
    df_sorted = df_portfolio.sort_values(by="Current Value", ascending=True)
    
    fig = px.bar(
        df_sorted, 
        x='Current Value', 
        y='Ticker', 
        orientation='h',
        title='Total Portfolio Value per Holding (KSh)',
        labels={'Current Value': 'Total Value (KSh)', 'Ticker': 'Stock'},
        text='Current Value',
        color='Current Value',
        color_continuous_scale=px.colors.sequential.Blugrn
    )
    fig.update_traces(texttemplate='KSh %{text:,.2f}', textposition='outside')
    fig.update_layout(
        margin=dict(l=50, r=50, t=40, b=40),
        showlegend=False,
        coloraxis_showscale=False,
        xaxis_tickformat=',.0f'
    )
    st.plotly_chart(fig, use_container_width=True)

st.write("---")

# 6. RESTORED: Global Market Scanner Index (Displays all 50+ tickers)
st.subheader("🌐 Global Market Reference Index")
market_rows = []
for ticker, info in nse_data.items():
    market_rows.append({
        "Ticker": ticker,
        "Company Name": info["name"],
        "Current Baseline Price (KSh)": info["price"],
        "Daily Change": f"{info['change']:+.2f}",
        "Fundamental Rating (/5)": info["score"]
    })

df_market = pd.DataFrame(market_rows).sort_values(by="Ticker")
st.dataframe(df_market, use_container_width=True, hide_index=True)