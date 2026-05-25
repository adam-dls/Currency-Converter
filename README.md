# Currency-Converter

This project aims to convert an amount from one currency into another currency, it's my first python project so I hope it won't be too bad...

## About The Project

This project is a basic currency converter in real time by using a public API, It is used via an interface made with **Streamlit**

## Build With 

language : python 3.13.7
requests : to get the API informations
Streamlit : for the visual interface (framework)
python-dotenv :  to manage the security (useless bc it's a public API but I want to train myself on it)

## How To Use It

1. **clone the repository**:
    open git bash and write:
        git clone https://github.com/adam-dls/Currency-Converter.git
    
    Then enter into the folder:
        cd Currency-Converter

2. **Create a virtual environment**
        python -m venv venv

    # Windows
        venv\Scripts\activate
    
    # macOS/Linux
        source venv/bin/activate

3.  **Install Dependencies** :
    In a bash terminal : 
        pip install -r requirements.txt

4.  **Configure Environment Variables** :
    Create a file .env in the project folder and write down your API key (if it's necessary, with the frankfurter it's not required) and the API URL:

    API_Key=votre_cle_api_ici
    BASE_URL=https://api.frankfurter.dev/v2/rates
    
    *(The API used in this project is public, but its structure could work even if it were a secure API.).*

5.  **Lancer l'application** :
    In a bash terminal:
        streamlit run currency_converter.py

*Developped by Adam, mathematics undergraduate student in France*