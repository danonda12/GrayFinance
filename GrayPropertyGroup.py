import streamlit as st
import pandas as pd

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www.distributiondirect.com/wp-content/uploads/2020/08/bigstock-Financial-objects-5150660.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

#set_bg_hack_url()

# Title
st.title("Gray Property Group - Multifamily Financial Analysis")

# Acquisition & Initial Financing Terms
with st.expander("Acquisition & Initial Financing Terms"):
    purchase_price = st.number_input("Purchase Price ($)", value=850000, key="purchase_price")
    upfront_rehab = st.number_input("Upfront Rehab ($)", value=150000, key="upfront_rehab")
    bank_purchase_financing = st.number_input("Bank Purchase Financing (%)", min_value=0.0, max_value=100.0, value=75.0, key="bank_purchase_financing") / 100
    bank_rehab_financing = st.number_input("Bank Rehab Financing (%)", min_value=0.0, max_value=100.0, value=75.0, key="bank_rehab_financing") / 100
    bank_mortgage_principal = purchase_price * bank_purchase_financing
    bank_apr = st.number_input("Bank Mortgage APR (%)", min_value=0.0, value=4.0, key="bank_apr") / 100
    bank_loan_term = st.number_input("Bank Mortgage Loan Term (years or IO)", value=25, key="bank_loan_term")
    bank_interest_only_period = st.number_input("Bank Interest Only Period (years)", value=0, key="bank_interest_only_period")
    seller_mortgage_principal = 0  # This value can be calculated based on your inputs
    seller_apr = st.number_input("Seller Mortgage APR (%)", min_value=0.0, value=5.0, key="seller_apr") / 100
    seller_loan_term = st.selectbox("Seller Mortgage Loan Term (years or IO)", ["IO", 5, 10, 15, 20, 25], key="seller_loan_term")
    purchase_rehab_down_payment = st.number_input("Purchase & Rehab Down Payment ($)", value=250000, key="purchase_rehab_down_payment")
    private_mortgage_insurance = st.radio("Private Mortgage Insurance?", ("Yes", "No"), key="private_mortgage_insurance")
    closing_costs = st.number_input("Closing Costs ($)", value=10000, key="closing_costs")
    seller_credits = 0  # This value can be calculated based on your inputs
    total_capital_investment = purchase_price + upfront_rehab
    escrow_required_reserves = st.number_input("Escrow & Required Reserves ($)", value=40000, key="escrow_required_reserves")
    cash_required_to_close = purchase_rehab_down_payment + closing_costs

    # Display Acquisition & Initial Financing Terms
    st.write(f"Bank Mortgage Principal ($): {bank_mortgage_principal}")
    st.write(f"Seller Mortgage Principal ($): {seller_mortgage_principal}")
    st.write(f"Total Capital Investment ($): {total_capital_investment}")
    st.write(f"Cash Required to Close ($): {cash_required_to_close}")

# Re-Finance Terms
with st.expander("Re-Finance Terms"):
    year_of_refinance = st.number_input("Year of Re-Finance (year or N/A)", min_value=0, key="year_of_refinance")
    valuation = st.number_input("Valuation ($)", value=1739287, key="valuation")
    ltv_financing = st.number_input("LTV Financing (%)", min_value=0.0, max_value=100.0, value=75.0, key="ltv_financing") / 100
    new_mortgage_principal = valuation * ltv_financing
    bank_mortgage_payoff = st.number_input("Bank Mortgage Pay-Off ($)", value=649369, key="bank_mortgage_payoff")
    seller_mortgage_payoff = 0  # This value can be calculated based on your inputs
    closing_costs_refinance = st.number_input("Closing Costs ($)", value=10000, key="closing_costs_refinance")
    cash_out_in = new_mortgage_principal - bank_mortgage_payoff
    new_mortgage_apr = st.number_input("New Mortgage APR (%)", min_value=0.0, value=4.0, key="new_mortgage_apr") / 100
    mortgage_loan_term = st.number_input("Mortgage Loan Term (years or IO)", value=25, key="mortgage_loan_term")
    new_annual_debt_service = new_mortgage_principal * (new_mortgage_apr / 12) / (1 - (1 + new_mortgage_apr / 12) ** (-mortgage_loan_term * 12))
    dscr = valuation / new_annual_debt_service

    # Display Re-Finance Terms
    st.write(f"New Mortgage Principal ($): {new_mortgage_principal}")
    st.write(f"Bank Mortgage Pay-Off ($): {bank_mortgage_payoff}")
    st.write(f"Seller Mortgage Pay-Off ($): {seller_mortgage_payoff}")
    st.write(f"Cash Out (In) ($): {cash_out_in}")
    st.write(f"New Annual Debt Service ($): {new_annual_debt_service}")
    st.write(f"Debt Service Coverage Ratio: {dscr:.2f}")

# Sale Terms
with st.expander("Sale Terms"):
    year_of_sale = st.number_input("Year of Sale (years)", min_value=0, key="year_of_sale")
    sale_price = st.number_input("Sale Price ($)", value=2820077, key="sale_price")
    mortgage_payoff_sale = st.number_input("Mortgage Pay-Off ($)", value=660214, key="mortgage_payoff_sale")
    closing_costs_sale = st.number_input("Closing Costs ($)", value=169205, key="closing_costs_sale")
    capital_gain_tax = st.number_input("Capital Gain Tax ($)", value=247631, key="capital_gain_tax")
    depreciation_recapture = st.number_input("Depreciation Re-Capture ($)", value=146909, key="depreciation_recapture")
    net_sale_revenue = sale_price - mortgage_payoff_sale - closing_costs_sale - capital_gain_tax - depreciation_recapture

    # Display Sale Terms
    st.write(f"Net Sale Revenue ($): {net_sale_revenue}")

# Create a dictionary to store variable names and their values
variables_data = {
    "Purchase Price ($)": purchase_price,
    "Upfront Rehab ($)": upfront_rehab,
    "Bank Purchase Financing (%)": bank_purchase_financing,
    "Bank Rehab Financing (%)": bank_rehab_financing,
    "Bank Mortgage Principal ($)": bank_mortgage_principal,
    "Bank Mortgage APR (%)": bank_apr,
    "Bank Mortgage Loan Term (years or IO)": bank_loan_term,
    "Bank Interest Only Period (years)": bank_interest_only_period,
    "Seller Mortgage Principal ($)": seller_mortgage_principal,
    "Seller Mortgage APR (%)": seller_apr,
    "Seller Mortgage Loan Term (years or IO)": seller_loan_term,
    "Purchase & Rehab Down Payment ($)": purchase_rehab_down_payment,
    "Private Mortgage Insurance?": private_mortgage_insurance,
    "Closing Costs ($)": closing_costs,
    "Seller Credits ($)": seller_credits,
    "Total Capital Investment ($)": total_capital_investment,
    "Escrow & Required Reserves ($)": escrow_required_reserves,
    "Cash Required to Close ($)": cash_required_to_close,
    "Year of Re-Finance (year or N/A)": year_of_refinance,
    "Valuation ($)": valuation,
    "LTV Financing (%)": ltv_financing,
    "New Mortgage Principal ($)": new_mortgage_principal,
    "Bank Mortgage Pay-Off ($)": bank_mortgage_payoff,
    "Seller Mortgage Pay-Off ($)": seller_mortgage_payoff,
    "Closing Costs (Refinance) ($)": closing_costs_refinance,
    "Cash Out (In) ($)": cash_out_in,
    "New Mortgage APR (%)": new_mortgage_apr,
    "Mortgage Loan Term (years or IO)": mortgage_loan_term,
    "New Annual Debt Service ($)": new_annual_debt_service,
    "Debt Service Coverage Ratio": dscr,
    "Year of Sale (years)": year_of_sale,
    "Sale Price ($)": sale_price,
    "Mortgage Pay-Off (Sale) ($)": mortgage_payoff_sale,
    "Closing Costs (Sale) ($)": closing_costs_sale,
    "Capital Gain Tax ($)": capital_gain_tax,
    "Depreciation Re-Capture ($)": depreciation_recapture,
    "Net Sale Revenue ($)": net_sale_revenue,
}

# Create a download button to export the variables and their values as a CSV report
# if st.button("Export Variables as CSV"):
# Create a Pandas DataFrame from the dictionary
variables_df = pd.DataFrame(list(variables_data.items()), columns=["Variable Name", "Value"])

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(variables_df)

st.download_button(
   "Download Report",
   csv,
   "report.csv",
   "text/csv",
   key='download-csv'
)
