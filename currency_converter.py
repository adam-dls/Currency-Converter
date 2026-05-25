import requests 
import streamlit as st 
import os 
from dotenv import load_dotenv

# get the API info
load_dotenv()
api_key = os.getenv('API_Key')
url = os.getenv('BASE_URL')

# Get and test request to the API
try:
    response = requests.get(url)
    response_json = response.json()
    
except:
    st.error(body="No response from the API")
    st.stop()

# Put all rates in a dictonnairy
dic_rates = {item["quote"] : item['rate'] for item in response_json}

# Add the base value fixe to 1
dic_rates.update({response_json[0]['base'] : 1})

# Make a list with all currencies symbols
Currency_symbol = [item["quote"] for item in response_json] + ['EUR']

st.title(body="Currency Converter", text_alignment='center')
st.divider()

def currency_converter_main():

    with st.form(key='form1'):
        
        currency_from = st.selectbox(label='Select a from currency', options=Currency_symbol)
        currency_to = st.selectbox(label='Select a to currency', options=Currency_symbol)
        amount = st.number_input("Enter an amount: ")

        if st.form_submit_button(label='submit'):
            if currency_from == currency_to:
                st.write(f"{amount} {currency_from} equals {amount} {currency_to}")

            else:
                # Get the info from the API
                try:
                    rate_from = dic_rates[currency_from]
                    rate_to = dic_rates[currency_to]

                    # Calculation of the result
                    convert = format(amount/rate_from*rate_to, '.2f')
    
                # Error gestion
                except KeyError:
                    convert = None
                    st.error(body="currency not found")
                
                except ZeroDivisionError:
                    convert = None
                    st.error(body="Divided by zero")
                
                st.write(f"{amount} {currency_from} equals {convert} {currency_to}")
    
    return 

currency_converter_main()