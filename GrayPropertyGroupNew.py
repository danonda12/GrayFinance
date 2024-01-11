import streamlit as st
import pandas as pd

st. set_page_config(layout="wide")
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

with st.expander("Pro Forma Analysis"):
    col1, col2, col3 = st.columns(3)
    with col1:
        scheduled_rental_income_asIs = st.number_input("Scheduled Rental Income ($) - As-Is", value=1275)
        scheduled_rental_income_asIs = 12*scheduled_rental_income_asIs*8
        msg = "Scheduled Rental Income: "+str(scheduled_rental_income_asIs)
        st.warning(msg)
        laundry_income_asIs = st.number_input("Laundry Income ($) - As-Is", value=0)
        petRent_asIs = st.number_input("Pet Rent ($) - As-Is", value=0)
        parkingFess_asIs = st.number_input("Parking Fees ($) - As-Is", value=0)
        otherIncome_asIs = st.number_input("Other Income ($) - As-Is", value=0)
        total_asIs = "Total Scheduled Income As-Is: "+str(scheduled_rental_income_asIs + laundry_income_asIs + petRent_asIs + parkingFess_asIs + otherIncome_asIs)
        st.info(total_asIs)
    with col2:
        scheduled_rental_income_rentBump = st.number_input("Scheduled Rental Income ($) - Rent Bump", value=1350)
        scheduled_rental_income_rentBump = 12*scheduled_rental_income_rentBump*8
        msg = "Scheduled Rental Income: "+str(scheduled_rental_income_rentBump)
        st.warning(msg)
        laundry_income_rentBump = st.number_input("Laundry Income ($) - Rent Bump", value=0)
        petRent_rentBump = st.number_input("Pet Rent ($) - Rent Bump", value=0)
        parkingFess_rentBump = st.number_input("Parking Fees ($) - Rent Bump", value=0)
        otherIncome_rentBump = st.number_input("Other Income ($) - Rent Bump", value=0)
        total_rentBump = "Total Scheduled Income - Rent Bump: "+str(scheduled_rental_income_rentBump + laundry_income_rentBump + petRent_rentBump + parkingFess_rentBump + otherIncome_rentBump)
        st.info(total_rentBump)
    with col3:
        scheduled_rental_income_renovated = st.number_input("Scheduled Rental Income ($) - Renovated", value=1850)
        scheduled_rental_income_renovated = 12*scheduled_rental_income_renovated*8
        msg = "Scheduled Rental Income: "+str(scheduled_rental_income_renovated)
        st.warning(msg)
        laundry_income_renovated = st.number_input("Laundry Income ($) - Renovated", value=0)
        petRent_renovated = st.number_input("Pet Rent ($) - Renovated", value=4)
        petRent_renovated = 12*petRent_renovated*30
        parkingFess_renovated = st.number_input("Parking Fees ($) - Renovated", value=0)
        otherIncome_renovated = st.number_input("Other Income ($) - Renovated", value=0)
        total_renovated = "Total Scheduled Income - Renovated: "+str(scheduled_rental_income_renovated + laundry_income_renovated + petRent_renovated + parkingFess_renovated + otherIncome_renovated)
        st.info(total_renovated)
with st.expander("Unrealized Income"):
    vacancy_rate = 0.02
    credit_loss_rate = 0.005

    st.warning("Vacancy Rate: 2% | Credit Loss Rate: 0.5%")
    col1, col2, col3 = st.columns(3)
    with col1:
        vacancy_loss_asIs = st.number_input("Vacancy Loss ($) - As-Is", value=scheduled_rental_income_asIs*vacancy_rate)
        credit_loss_asIs = st.number_input("Credit Loss ($) - As-Is", value=scheduled_rental_income_asIs*credit_loss_rate)
        total_realized_income_as_is = scheduled_rental_income_asIs - vacancy_loss_asIs - credit_loss_asIs
        t = "Total Realized Income ($) - As-Is: "+str(total_realized_income_as_is)
        st.info(t)
    with col2:
        vacancy_loss_rentBump = st.number_input("Vacancy Loss ($) - Rent Bump", value=scheduled_rental_income_rentBump*vacancy_rate)
        credit_loss_rentBump = st.number_input("Credit Loss ($) - Rent Bump", value=scheduled_rental_income_rentBump*credit_loss_rate)
        total_realized_income_rentBump = scheduled_rental_income_rentBump - vacancy_loss_rentBump - credit_loss_rentBump
        t = "Total Realized Income ($) - Rent Bump: "+str(total_realized_income_rentBump)
        st.info(t)
    with col3:
        vacancy_loss_renovated = st.number_input("Vacancy Loss ($) - Renovated", value=scheduled_rental_income_renovated*vacancy_rate)
        credit_loss_renovated = st.number_input("Credit Loss ($) - Renovated", value=scheduled_rental_income_renovated*credit_loss_rate)
        total_realized_income_renovated = scheduled_rental_income_renovated - vacancy_loss_renovated - credit_loss_renovated
        t = "Total Realized Income ($) - Renovated: "+str(total_realized_income_renovated)
        st.info(t)

with st.expander("Operating Expenses"):
    property_management_fee = 0.08
    property_tax_rate = 0.01811
    property_tax_assessment = 850000
    property_tax = property_tax_assessment*property_tax_rate
    st.warning("Property Management Fee: 8% | Property Tax Rate: 1.811%")
    col1, col2, col3 = st.columns(3)
    with col1:
        prop_management_asIs = st.number_input("Property Management ($) - As-Is", value=total_realized_income_as_is*property_management_fee)
        property_tax_asIs = st.number_input("Property Tax ($) - As-Is", value=property_tax)
        property_insurrance_asIs = st.number_input("Property Insurrance ($) - As-Is", value=4800, key = 3)
        repairs_maintenace_asIs = st.number_input("Property Insurrance ($) - As-Is", value=7500, key = 6)
        unit_turns_asIs = st.number_input("Unit Turns ($) - As-Is", value=750)
        unit_turns_asIs = unit_turns_asIs * 3
        water_sewer_asIs = st.number_input("Water and& Sewer ($) - As-Is", value=0)
        fuel_asIs = st.number_input("Fuel ($) - As-Is", value=0)
        electricity_asIs = st.number_input("Electricity ($) - As-Is", value=225)
        electricity_asIs = electricity_asIs * 12
        grounds_asIs = st.number_input("Grounds ($) - As-Is", value=3500, key = 9)
        trash_service_asIs = st.number_input("Trash Service ($) - As-Is", value=1800)
        janitorial_asIs = st.number_input("Janitorial ($) - As-Is", value=0)
        general_administration_asIs = st.number_input("General Administration ($) - As-Is", value=500)
        total_operating_expenses_asIs = prop_management_asIs + property_tax_asIs + general_administration_asIs + janitorial_asIs + trash_service_asIs + property_insurrance_asIs + repairs_maintenace_asIs + unit_turns_asIs + water_sewer_asIs + fuel_asIs + electricity_asIs + grounds_asIs 
        tt_asIs = "Total Operating Expenses: "+str(total_operating_expenses_asIs)
        st.info(tt_asIs)
    with col2:
        prop_management_rentBump = st.number_input("Property Management ($) - Rent Bump", value=total_realized_income_rentBump*property_management_fee)
        property_tax_rentBump = st.number_input("Property Tax ($) - Rent Bump", value=property_tax, key=1)
        property_insurrance_rentBump = st.number_input("Property Insurrance ($) - Rent Bump", value=4800, key = 4)
        repairs_maintenace_rentBump = st.number_input("Repairs and Maintenance ($) - Rent Bump", value=7500, key = 7)
        unit_turns_rentBump = st.number_input("Unit Turns ($) - Rent Bump", value=750)
        unit_turns_rentBump = unit_turns_rentBump * 3
        water_sewer_rentBump = st.number_input("Water and& Sewer ($) - Rent Bump", value=0)
        fuel_rentBump = st.number_input("Fuel ($) - Rent Bump", value=0)
        electricity_rentBump = st.number_input("Electricity ($) - Rent Bump", value=225)
        electricity_rentBump = electricity_rentBump * 12
        grounds_rentBump = st.number_input("Grounds ($)", value=3500, key = 10)
        trash_service_rentBump = st.number_input("Trash Service ($) - Rent Bump", value=1800)
        janitorial_rentBump = st.number_input("Janitorial ($) - Rent Bump", value=0)
        general_administration_rentBump = st.number_input("General Administration ($) - Rent Bump", value=500)
        total_operating_expenses_rentBump = prop_management_rentBump + property_tax_rentBump + general_administration_rentBump + janitorial_rentBump + trash_service_rentBump + property_insurrance_rentBump + repairs_maintenace_rentBump + unit_turns_rentBump + water_sewer_rentBump + fuel_rentBump + electricity_rentBump + grounds_rentBump
        tt_rentBump = "Total Operating Expenses: "+str(total_operating_expenses_rentBump)
        st.info(tt_rentBump)
    with col3:
        prop_management_renovated = st.number_input("Property Management ($) - Renovated", value=total_realized_income_renovated*property_management_fee)
        property_tax_renovated = st.number_input("Property Tax", value=property_tax, key=2)
        property_insurrance_renovated = st.number_input("Property Insurrance ($)", value=4800, key = 5)
        repairs_maintenace_renovated = st.number_input("Repairs and Maintenance ($)", value=7500, key = 8)
        unit_turns_renovated = st.number_input("Unit Turns ($) - Renovated", value=750)
        unit_turns_renovated = unit_turns_renovated * 3
        water_sewer_renovated = st.number_input("Water and& Sewer ($) - Renovated", value=0)
        fuel_renovated = st.number_input("Fuel ($) - Renovated", value=0)
        electricity_renovated = st.number_input("Electricity ($) - Renovated", value=225)
        electricity_renovated = electricity_renovated * 12
        grounds_renovated = st.number_input("Grounds ($)", value=3500, key = 11)
        trash_service_renovated = st.number_input("Trash Service ($) - Renovated", value=1800)
        janitorial_renovated = st.number_input("Janitorial ($) - Renovated", value=0)
        general_administration_renovated = st.number_input("General Administration ($) - Renovated", value=500)
        total_operating_expenses_renovated = prop_management_renovated + property_tax_renovated + general_administration_renovated + janitorial_renovated + trash_service_renovated + property_insurrance_renovated + repairs_maintenace_renovated + unit_turns_renovated + water_sewer_renovated + fuel_renovated + electricity_renovated + grounds_renovated
        tt_renovated = "Total Operating Expenses: "+str(total_operating_expenses_renovated)
        st.info(tt_renovated)

with st.expander("Net Operating Income"):
    # bank mortgage payment
    def excel_formula(B10, B9, B6, B4):
        if B10 == "IO":
            result = B9 * (B6 * B4)
        else:
            result = (B9 * (B6 * B4)) / (1 - (1 + B9) ** (-B10))
        
        return result
    
    # seller mortgage payment
    def excel_formula2(B12, B14, B13):
        if B12 == "N/A":
            result = 0
        else:
            if B14 == "IO":
                result = B13 * B12
            else:
                result = (B13 * B12) / (1 - (1 + B13) ** (-B14))
        
        return result
        
    # Mortgage Insurance
    def excel_formula3(B16, B19, B4, B5, J41):
        if B16 == "Yes" and B19/B4 < 0.2:
            result = J41 * (B4 + B5 - B19)
        else:
            result = 0
        
        return result

    # bank mortgage payment
    B10_value = bank_loan_term
    B9_value = bank_apr
    B6_value = bank_purchase_financing
    B4_value = purchase_price
    bmp = excel_formula(B10_value, B9_value, B6_value, B4_value)

    # seller mortgage payment
    B12_value = seller_mortgage_principal
    B14_value = seller_loan_term
    B13_value = seller_apr
    smp = excel_formula2(B12_value, B14_value, B13_value)

    # Mortgage Insurance
    B16_value = private_mortgage_insurance
    B19_value = total_capital_investment
    B4_value = purchase_price
    B5_value = upfront_rehab
    mortgage_Insurance_Rate = 0.85
    J41_value = mortgage_Insurance_Rate
    mi = excel_formula3(B16_value, B19_value, B4_value, B5_value, J41_value)

    col1, col2, col3 = st.columns(3)
    with col1:
        net_operating_income_asIs = st.number_input("Net Operating Income ($) - As Is", value=total_realized_income_as_is-total_operating_expenses_asIs)
        non_operating_expenses_asIs = st.number_input("Non Operating Expenses - As Is", value=0)
        bank_mortgage_payment_asIs = st.number_input("Bank Mortgage Payment ($) - As Is", value=bmp)
        seller_mortgage_payment_asIs = st.number_input("Seller Mortgage Payment ($) - As Is", value=smp)
        mortgage_insurance_asIs = st.number_input("Mortgage Insurance ($) - As Is", value=mi)
        capital_expenditure_reserve_asIs = st.number_input("Capital Expenditure Reserve ($) - As Is", value=7500)
        total_non_operating_expenses_asIs = bank_mortgage_payment_asIs + seller_mortgage_payment_asIs + mortgage_insurance_asIs + capital_expenditure_reserve_asIs
        desc = "Total Non-Operating Expenses ($) - As Is: "+str(round(total_non_operating_expenses_asIs,2))
        st.info(desc)
    with col2:
        net_operating_income_rentBump = st.number_input("Net Operating Income ($) - Rent Bump", value=total_realized_income_rentBump-total_operating_expenses_rentBump)
        non_operating_expenses_rentBump = st.number_input("Non Operating Expenses - Rent Bump", value=0)
        bank_mortgage_payment_rentBump = st.number_input("Bank Mortgage Payment ($) - Rent Bump", value=bmp)
        seller_mortgage_payment_rentBump = st.number_input("Seller Mortgage Payment ($) - Rent Bump", value=smp)
        mortgage_insurance_rentBump = st.number_input("Mortgage Insurance ($) - Rent Bump", value=mi)
        capital_expenditure_reserve_rentBump = st.number_input("Capital Expenditure Reserve ($) - RentBump", value=7500)
        total_non_operating_expenses_rentBump = bank_mortgage_payment_rentBump + seller_mortgage_payment_rentBump + mortgage_insurance_rentBump + capital_expenditure_reserve_rentBump
        desc = "Total Non-Operating Expenses ($) - Rent Bump: "+str(round(total_non_operating_expenses_rentBump,2))
        st.info(desc)
    with col3:
        net_operating_income_renovated = st.number_input("Net Operating Income ($) - Renovated", value=total_realized_income_renovated-total_operating_expenses_renovated)
        non_operating_expenses_renovated = st.number_input("Non Operating Expenses - Renovated", value=0)
        bank_mortgage_payment_renovated = st.number_input("Bank Mortgage Payment ($) - Renovated", value=bmp)
        seller_mortgage_payment_renovated = st.number_input("Seller Mortgage Payment ($) - renovated", value=smp)
        mortgage_insurance_renovated = st.number_input("Mortgage Insurance ($) - Renovated", value=mi)
        capital_expenditure_reserve_renovated = st.number_input("Capital Expenditure Reserve ($) - Renovated", value=7500)
        total_non_operating_expenses_renovated = bank_mortgage_payment_renovated + seller_mortgage_payment_renovated + mortgage_insurance_renovated + capital_expenditure_reserve_renovated
        desc = "Total Non-Operating Expenses ($) - Renovated: "+str(round(total_non_operating_expenses_renovated, 2))
        st.info(desc)
with st.expander("Net Cash Flow"):
    col1, col2, col3 = st.columns(3)
    with col1:
        net_cash_flow_asIs = "Net Cash Flow ($) - As Is: "+str(round(net_operating_income_asIs - total_non_operating_expenses_asIs, 2))
        st.info(net_cash_flow_asIs)
    with col2:
        net_cash_flow_rentBump = "Net Cash Flow ($) - Rent Bump: "+str(round(net_operating_income_rentBump - total_non_operating_expenses_rentBump, 2))
        st.info(net_cash_flow_rentBump)
    with col3:
        net_cash_flow_renovated = "Net Cash Flow ($) - Renovated: "+str(round(net_operating_income_renovated - total_non_operating_expenses_renovated, 2))
        st.info(net_cash_flow_renovated)
    

        

# Create a download button to export the variables and their values as a CSV report
# if st.button("Export Variables as CSV"):
# Create a Pandas DataFrame from the dictionary
variables_df = pd.DataFrame(list(variables_data.items()), columns=["Variable Name", "Value"])
st.dataframe(variables_df)

@st.experimental_memo
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
